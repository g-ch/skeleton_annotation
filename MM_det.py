import sys
sys.path.append('/home/jtverhoog/BEP/skeleton_annotation/mmdetection')

import mmcv
from mmdet.apis import init_detector, inference_detector
import cv2
import os
import numpy as np

### Deze is zoals het zou moeten, met de API's. Voor info zie:
### https://mmdetection.readthedocs.io/en/v2.0.0/api.html#module-mmdet.apis
### https://mmdetection.readthedocs.io/en/v2.24.1/api.html

### Alle directories aanpassen
input_folder = 'Jolle_working_folder/input_folder'
output_folder = 'Jolle_working_folder/output_folder'
folder_config_checkpoint = 'Jolle_working_folder/NN'

### manually copy the .py and .pth files to working_folder/NN. Download the .pth en copy .py from directory
### config_file= '/home/jtverhoog/BEP/skeleton_annotation/mmdetection/configs/sort/sort_faster-rcnn_r50_fpn_8xb2-4e_mot17halftrain_test-mot17halfval.py'
### checkpoint_file = 'https://download.openmmlab.com/mmtracking/mot/faster_rcnn/faster-rcnn_r50_fpn_4e_mot17-half-64ee2ed4.pth'
### then change the names of these files to: NN_config_file and NN_checkpoint_file

config_file = '/home/jtverhoog/BEP/skeleton_annotation/Jolle_working_folder/NN/NN_config_file.py'
checkpoint_file = '/home/jtverhoog/BEP/skeleton_annotation/Jolle_working_folder/NN/NN_checkpoint_file'

image_files = [os.path.join(input_folder,file) for file in os.listdir(input_folder) if file.endswith(('.jpg','.jpeg','.png'))]
images = [mmcv.imread(file) for file in image_files]
image_array = np.array(images)
### array of all images

model = init_detector(config_file, checkpoint_file, device='cpu') ###mmdet.apis.init_detector(config, device='cpu')
detection_results = inference_detector(model, image_array)

### Deze print geeft sowieso niks maar de detection_results.bb voor bounding box wel vgm
print(detection_results)


### Hieronder heb ik een begin gemaakt met hoe de bounding boxes knippen moet gaan werken ongeveer (denk ik)
"""
x1,y1,x2,y2 = 0,0,0,0
bboxes = np.array([x1,y1,x2,y2])        ### x1,y1 top left and x2,y2 right bottom of bounding box
patch = mmcv.imcrop(img, bboxes)        ### crop image


output_name = ' '
mmcv.imwrite(picture, output_name)
"""

