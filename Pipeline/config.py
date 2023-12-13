




### CHANGE THESE THREE DIRECTORIES

#location of this file
this_dir = '/home/jtverhoog/BEP/skeleton_annotation/Pipeline/config.py'

# location of mmdetection folder (don't end with a dash)
mmdet_folder = '/home/jtverhoog/BEP/skeleton_annotation/mmdetection'

# location of mmpose folder (don't end with a dash)
mmpose_folder = '/home/jtverhoog/BEP/skeleton_annotation/mmpose'






###############################################################################################################################
### More configuration possibilities

# device used, use cpu if no videocard available
device = 'cpu'

# detection threshold for person detection
det_threshold = 0.8

# model used for person detection
detection_model = 'mask-rcnn_r101-syncbn-gcb-r16-c3-c5_fpn_1x_coco'

# pose detection configuration file for Neural Network
config_file = f'{mmpose_folder}/configs/body_2d_keypoint/integral_regression/coco/ipr_res50_debias-8xb64-210e_coco-256x256.py'

# trained state of pose detection model
checkpoint_file = 'https://download.openmmlab.com/mmpose/v1/body_2d_keypoint/integral_regression/coco/ipr_res50_debias-8xb64-210e_coco-256x256-055a7699_20220913.pth'

# More options for visualisation of pose estimation
draw_heatmap = False          # Visualize the predicted heatmap
show_kpt_idx = True           # Whether to show the index of keypoints
skeleton_style = 'mmpose'     # Skeleton style selection, can be 'openpose' too
kpt_thr = 0.3                 # Visualizing keypoint thresholds
radius = 2                    # Keypoint radius for visualization in pixels
thickness = 1                 # Link thickness for visualization in pixels
alpha = 1.0                   # The transparency of bboxes (between 0.0 and 1.0)
show = False                  # Whether to show img during processing
save_kpt_score = False        # Whether to save the numpy array of keypoint scores


##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
import os


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

def get_vis_setup():
    return draw_heatmap, show_kpt_idx, skeleton_style, kpt_thr, radius, thickness, alpha, save_kpt_score, show, device

def get_json_setup():
    base_labelme = get_directory_path('good_labelme.json')
    cut_out_bb = get_directory_path('2_cut_out_bb')
    pose_npy_pred_out = get_directory_path('3_pose_annotation/preds_npy')
    output_labelme = get_directory_path('4_labelme_readables')
    return cut_out_bb, pose_npy_pred_out, base_labelme, output_labelme

def get_detection_model():
    return detection_model, device

def print_separator():
    print('\n#############################################################################################################\n')

    


