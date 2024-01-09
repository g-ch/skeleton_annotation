# Skeleton annotation

## Description

A pipeline to annotate skeletons on a dataset of pictures from any dataset. The pipeline consists of four distinct steps and is highly customisable. The output skeletons can also be exported into LabelMe format so they can be manually adjusted.

## Features

- Person and object detection (with customisable models)
- Extracting the image of certain persons or objects
- Predicting the pose annotation (with customisable models)
- Exporting the predicted pose annotation to LabelMe-readable files for manual readjustment

## Installation and first run

Tested on Ubuntu 22.04, python 3.8, mmengine 2.0.0

### 1. Clone the repository with 'git clone https://github.com/g-ch/skeleton_annotation.git'.

### 2. Within the folder 'skeleton_annotation' clone mmpose and mmdetection libraries, see: 
https://mmpose.readthedocs.io/en/latest/installation.html
https://mmdetection.readthedocs.io/en/latest/get_started.html

### 3. Create a conda environment with the first lines in 'requirements.txt'.

### 4. Change the three directories in 'config.py'.
![Stap 1](https://github.com/g-ch/skeleton_annotation/assets/126026624/a225f19a-d5b7-43df-a696-56fbbdccf796)

### 5. Within the terminal cd to ~/Pipeline/ and run 'config.py'. Now you can customise the parameters for detection, pose estimation and output format.
![Stap 2](https://github.com/g-ch/skeleton_annotation/assets/126026624/dc926c66-f232-4921-a3d7-82aef349887b)

### 6. Insert the desired pictures in the '0_input_dataset' folder.
![Stap 3 simpel](https://github.com/g-ch/skeleton_annotation/assets/126026624/9134fcb3-94f5-4995-91b9-3a796a497a87)

### 7. Run 'runner.py'. Output is verbose so possible warnings will be shown.
![stap 4 simpel deel 1](https://github.com/g-ch/skeleton_annotation/assets/126026624/da884f0d-9e86-42b3-ab18-9444a3d9f9e6)
![stap 4 simpel deel 2](https://github.com/g-ch/skeleton_annotation/assets/126026624/094421af-4f50-4829-b225-404d10d6d200)

### 8. All final results and intermediate files can be found in the working tree:
![simpel worktree](https://github.com/g-ch/skeleton_annotation/assets/126026624/fbc5f58f-105c-4c58-978f-f425c29ea4c4)

**OPTIONAL** (output correction in LabelMe):
1. Create a new environment to avoid conflicts and install labelme.
2. Open the outputted .json file from step 8 above.
![LabelMe simpel](https://github.com/g-ch/skeleton_annotation/assets/126026624/575d5d12-2266-4b96-a352-b4bfc17fe362)
3. Manually re-adjust any points and save the corrected file.



# Customisation

## Detection
The detection model can be easily changed by choosing a different one and entering it into the config. The built in models are found in the MMDetection ModelZoo (https://mmdetection.readthedocs.io/en/latest/model_zoo.html). If a personally trained model is prefereerd the path to this model can also be specified. 

## Cropping images
After the person detection is done, the individuals are made into seperate cropped pictures by their bounding boxes. The threshold for the creation of these cropped images is the certainty of the detection model. This can be changed in 'config.py' and should be a value between 0.0 and 1.0, representing a threshold of between 0% and 100% certainty. If it is desired to cut out other objects, line 22 in 'cut_out_bb.py' can be changed to another label. Note that this makes the next part of the pipeline useless.

## Pose estimation
Within 'config.py' the model used for the pose estimation can also be customised. For built in 2D person pose estimation models, see: https://github.com/open-mmlab/mmpose/tree/main/configs/body_2d_keypoint. This works best if also a trained state of the model, checkpoiny file, is provided. If a personally trained model is preferred the directory can be provided. Furthermore the visualisation output options can be changed, a heatmap can be added and the threshold for the visualisation of keypoints can be adjusted.
Beware: if changing to a different annotation than the Coco-format, the .json file created for LabelMe will stop working.

## Pose correction
Within 'çonfig.py' there are two options for the format of the .json file that is created. One where solely the keypoints are visible and one where the connecting lines between the keypoints are also visualised. To alter the output it is required to manually move keypoints by drag and dropping. When the connecting lines are also visualised the endpoints of these need to be moved seperate to the keypoints by drag and dropping as well.







