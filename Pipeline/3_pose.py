import logging
from argparse import ArgumentParser
import os
import numpy as np

from config import get_mmpose_setup, print_separator

from mmcv.image import imread
from mmengine.logging import print_log

from mmpose.apis import inference_topdown, init_model
from mmpose.registry import VISUALIZERS
from mmpose.structures import merge_data_samples


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--img', default=image_file, help='Image file')
    parser.add_argument('--output_folder', default=output_path, help='Output folder')
    parser.add_argument('--config', default=config_file, help='Config file')
    parser.add_argument('--checkpoint', default=checkpoint_file, help='Checkpoint file')
    parser.add_argument('--out-file', default=None, help='Path to output file')
    parser.add_argument(
        '--device', default='cpu', help='Device used for inference')
    parser.add_argument(
        '--draw-heatmap',
        default=False,
        action='store_true',
        help='Visualize the predicted heatmap')
    parser.add_argument(
        '--show-kpt-idx',
        action='store_true',
        default=False,
        help='Whether to show the index of keypoints')
    parser.add_argument(
        '--skeleton-style',
        default='coco',
        type=str,
        choices=['mmpose', 'openpose'],
        help='Skeleton style selection')
    parser.add_argument(
        '--kpt-thr',
        type=float,
        default=0.3,
        help='Visualizing keypoint thresholds')
    parser.add_argument(
        '--radius',
        type=int,
        default=0,
        help='Keypoint radius for visualization')
    parser.add_argument(
        '--thickness',
        type=int,
        default=1,
        help='Link thickness for visualization')
    parser.add_argument(
        '--alpha', type=float, default=0.8, help='The transparency of bboxes')
    parser.add_argument(
        '--show',
        action='store_true',
        default=False,
        help='whether to show img')
    args = parser.parse_args()
    return args


def run_pose_estimation(img_file, config_file, checkpoint_file, out_file='result.jpg'):
    args.out_file = out_file
    
    # build the model from a config file and a checkpoint file
    if args.draw_heatmap:
        cfg_options = dict(model=dict(test_cfg=dict(output_heatmaps=True)))
    else:
        cfg_options = None

    model = init_model(
        args.config,
        args.checkpoint,
        device=args.device,
        cfg_options=cfg_options)

    # init visualizer
    model.cfg.visualizer.radius = args.radius
    model.cfg.visualizer.alpha = args.alpha
    model.cfg.visualizer.line_width = args.thickness

    visualizer = VISUALIZERS.build(model.cfg.visualizer)
    visualizer.set_dataset_meta(
        model.dataset_meta, skeleton_style=args.skeleton_style)

    # inference a single image
    batch_results = inference_topdown(model, args.img)
    results = merge_data_samples(batch_results)

    pred_instances = batch_results[0].pred_instances
    
    keypoints = pred_instances.keypoints
    keypoint_scores = pred_instances.keypoint_scores # these are not saved but could be
    keypoints_vis = pred_instances.keypoints_visible # these are not saved but could be

    filename_clean = filename.split('.')[0]
    np.save(f'{pose_npy_pred_out}/{filename_clean}.npy', keypoints)
        
    # show the results
    img = imread(args.img, channel_order='rgb')
    visualizer.add_datasample(
        'result',
        img,
        data_sample=results,
        draw_gt=False,
        draw_bbox=True,
        kpt_thr=args.kpt_thr,
        draw_heatmap=args.draw_heatmap,
        show_kpt_idx=args.show_kpt_idx,
        skeleton_style=args.skeleton_style,
        show=args.show,
        out_file=args.out_file)

    if args.out_file is not None:
        print_log(
            f'the output image has been saved at {args.output_folder}',
            logger='current',
            level=logging.INFO)

if __name__ == '__main__':
    print_separator()
    config_file, checkpoint_file, output_folder_vis, pose_npy_pred_out, input_folder = get_mmpose_setup()
    
    if not os.path.exists(input_folder):
        print(f"Input folder {input_folder} does not exist.")
        exit(1)

    for filename in os.listdir(input_folder):
        try:
            image_file = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder_vis, filename)
            args = parse_args()
            run_pose_estimation(image_file, config_file, checkpoint_file, out_file=output_path)
        except Exception as e:
            print(f"An error occurred processing {filename}: {e}")
    print_separator()


