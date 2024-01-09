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

1. git clone https://github.com/g-ch/skeleton_annotation.git

2. Within skeleton_annotation clone mmpose and mmdetection libraries, see: 
  - https://mmpose.readthedocs.io/en/latest/installation.html
  - https://mmdetection.readthedocs.io/en/latest/get_started.html

3. Create a conda environment with the first lines in requirements.txt

4. Change the three directories in config.py.
![Stap 1](https://github.com/g-ch/skeleton_annotation/assets/126026624/a225f19a-d5b7-43df-a696-56fbbdccf796)

5. Within the terminal cd to ~/Pipeline/ and run config.py. Now you can customise the parameters for detection, pose estimation and output format.
![Stap 2](https://github.com/g-ch/skeleton_annotation/assets/126026624/dc926c66-f232-4921-a3d7-82aef349887b)

6. Insert the desired pictures in the '0_input_dataset' folder.
![Stap 3 simpel](https://github.com/g-ch/skeleton_annotation/assets/126026624/9134fcb3-94f5-4995-91b9-3a796a497a87)

7. Run runner.py. Output is verbose so possible warnings will be shown.
![stap 4 simpel deel 1](https://github.com/g-ch/skeleton_annotation/assets/126026624/da884f0d-9e86-42b3-ab18-9444a3d9f9e6)
![stap 4 simpel deel 2](https://github.com/g-ch/skeleton_annotation/assets/126026624/094421af-4f50-4829-b225-404d10d6d200)

OPTIONAL (output correction in LabelMe):
1. Create a new environment to avoid conflicts and install labelme.
2. Open the outputted .json file from step 8 above.
![LabelMe simpel](https://github.com/g-ch/skeleton_annotation/assets/126026624/575d5d12-2266-4b96-a352-b4bfc17fe362)
3. Manually re-adjust any points and save the corrected file.



# Customisation

## Detection
To change the configuration of the detection model adjust 1_detction.py line 14.

## Cropping images
The threshold for cropping a detected bounding box can be adjusted in config.py line 13.
To cut out other detected objects, line 22 in 2_cut_bb.py can be adjusted to select a different label for the cutting of bounding boxes.

## Pose estimation
The configuration and checkpoint file used for the pose estimation can be adjusted in config.py lines 16 and 19.
For further customisation of the top-down pose inferencer the arguments in 3_pose.py can be adjusted.
Beware: if changing to a different annotation than the Coco-format, the .json file created for LabelMe will stop working.

## Pose correction
For pose correction LabelMe must be installed. The joints can  then be dragged individually to their correct placement.







