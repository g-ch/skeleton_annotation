# Skeleton annotation

## Description

A pipeline to annotate skeletons on a dataset of pictures from any dataset. The pipeline consists of four distinct steps and is highly customisable. The output skeletons can also be exported into LabelMe format so they can be manually adjusted.

## Features

- Person and object detection (with customisable models)
- Extracting the image of certain persons or objects
- Predicting the pose annotation (with customisable models)
- Exporting the predicted pose annotation to LabelMe-readable files for manual readjustment

## Installation

Tested on Ubuntu 22.04, python 3.8, mmengine 2.0.0

git clone https://github.com/g-ch/skeleton_annotation.git

Within skeleton_annotation clone mmpose and mmdetection libraries, see: 
- https://mmpose.readthedocs.io/en/latest/installation.html
- https://mmdetection.readthedocs.io/en/latest/get_started.html

cd skeleton_annotation/Pipeline/config.py
- Set the path in line 4 to the current file (~Pipeline/config.py)
- Set the path in lines 7 and 10 to the just cloned mmpose and mmdetection folders (~skeleton_annotation/mmpose & ~skeleton_annotation/mmdetection)

run config.py

place pictures in 0_input_dataset

run runner.py

# Customisation

## Detection
To change the configuration of the detection model adjust 1_detction.py line 14

## Cropping images
The threshold for cropping a detected bounding box can be adjusted in config.py line 13
To cut out other detected objects, line 22 in 2_cut_bb.py can be adjusted to select a different label for the cutting of bounding boxes

## Pose estimation
The configuration and checkpoint file used for the pose estimation can be adjusted in config.py lines 16 and 19
For further customisation of the top-down pose inferencer the arguments in 3_pose.py can be adjusted
Beware: if changing to a different annotation than the Coco-format, the .json file created for LabelMe will stop working

## Pose correction
For pose correction LabelMe must be installed. The joints can  then be dragged individually to their correct placement







