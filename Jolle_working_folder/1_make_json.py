from mmdet.apis import DetInferencer
import os
os.chdir('/home/jtverhoog/BEP/skeleton_annotation/mmdetection')

input_folder = '/home/jtverhoog/BEP/skeleton_annotation/Dataset_selection/' 
output_folder = '/home/jtverhoog/BEP/skeleton_annotation/Jolle_working_folder/det_output/'

# Initialize the DetInferencer
inferencer = DetInferencer(model='mask-rcnn_r101-syncbn-gcb-r16-c3-c5_fpn_1x_coco', device='cpu')

# Perform inference
result = inferencer(input_folder, out_dir=output_folder, no_save_pred=False)
