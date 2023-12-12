import os

#location of this file
this_dir = '/home/jtverhoog/BEP/skeleton_annotation/Pipeline/config.py'

# location of mmdetection folder (don't end with a dash)
mmdet_folder = '/home/jtverhoog/BEP/skeleton_annotation/mmdetection'

# location of mmpose folder (don't end with a dash)
mmpose_folder = '/home/jtverhoog/BEP/skeleton_annotation/mmpose'

# detection threshold for person detection
det_threshold = 0.8

# pose detection configuration file for Neural Network
config_file = f'{mmpose_folder}/configs/body_2d_keypoint/integral_regression/coco/ipr_res50_debias-8xb64-210e_coco-256x256.py'

# trained state of pose detection model
checkpoint_file = 'https://download.openmmlab.com/mmpose/v1/body_2d_keypoint/integral_regression/coco/ipr_res50_debias-8xb64-210e_coco-256x256-055a7699_20220913.pth'

def get_directory_path(dir_name):
    base_path = os.path.dirname(__file__)  # Gets the current directory where this script is located
    dir_path = os.path.join(base_path, dir_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    return dir_path

# create all paths
get_directory_path('0_input_dataset')
get_directory_path('1_detection/preds')
get_directory_path('1_detection/vis')
get_directory_path('2_cut_out_bb')
get_directory_path('3_pose_annotation/preds_npy')
get_directory_path('3_pose_annotation/vis')
get_directory_path('4_labelme_readables')

def base_dir():
    return this_dir.split('config.py')[0]

def get_mmdet_folder():
    return mmdet_folder

def detection_threshold():
    return det_threshold

def get_mmpose_setup():
    cut_out_bb = get_directory_path('2_cut_out_bb')
    pose_npy_pred_out = get_directory_path('3_pose_annotation/preds_npy')
    pose_vis_out = get_directory_path('3_pose_annotation/vis')
    return config_file, checkpoint_file, pose_vis_out, pose_npy_pred_out, cut_out_bb

def get_json_setup():
    base_labelme = get_directory_path('good_labelme.json')
    cut_out_bb = get_directory_path('2_cut_out_bb')
    pose_npy_pred_out = get_directory_path('3_pose_annotation/preds_npy')
    output_labelme = get_directory_path('4_labelme_readables')
    return cut_out_bb, pose_npy_pred_out, base_labelme, output_labelme

def print_separator():
    print('\n#############################################################################################################\n')

    


