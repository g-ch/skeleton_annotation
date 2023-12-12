from mmdet.apis import DetInferencer
from config import get_mmdet_folder, get_directory_path, print_separator
import os


os.chdir(get_mmdet_folder())
input_folder = get_directory_path('0_input_dataset')
output_folder = get_directory_path('1_detection')

print_separator()
# Initialize the Detection Inferencer
print('Initialising detection inferencer...\n')

inferencer = DetInferencer(model='mask-rcnn_r101-syncbn-gcb-r16-c3-c5_fpn_1x_coco', device='cpu')

# Perform inference
result = inferencer(input_folder, out_dir=output_folder, no_save_pred=False)

print('\nDetection complete')
print_separator()