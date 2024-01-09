# Skeleton Annotation

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation and Setup](#installation-and-setup)
4. [Usage](#usage)
5. [Customisation](#customisation)
6. [References](#references)

## Introduction
Skeleton Annotation is a customizable pipeline designed for annotating human skeletons in image datasets. This tool is ideal for researchers and developers working in computer vision, particularly in pose estimation and person/object detection. It integrates seamlessly with popular libraries like LabelMe, offering export options for manual adjustments.

## Features
- **Person and Object Detection**: Utilizes customizable models for accurate detection.
- **Image Extraction**: Capable of extracting images of specific persons or objects.
- **Pose Prediction**: Supports pose annotation prediction with customizable models.
- **LabelMe Integration**: Export pose annotations to LabelMe format for manual adjustments.

<p align="center">
  <img src="https://github.com/g-ch/skeleton_annotation/assets/126026624/228a7489-5fee-4912-be95-6b828ba524ea" width="300" />
  <img src="https://github.com/g-ch/skeleton_annotation/assets/126026624/e1b0d790-6835-4257-8c42-ae0a24f477f9" width="300" /> 
</p>

<p align="center">
  On the left the original image and on the right the visualisation of the object/person detection 
</p>

<p align="center">
  <img src="https://github.com/g-ch/skeleton_annotation/assets/126026624/30b797d3-5ed0-4138-a384-f7ea27d04681" width="200" />
  <img src="https://github.com/g-ch/skeleton_annotation/assets/126026624/855c3d25-10e6-43a6-ac45-478d20d392df" width="200" /> 
  <img src="https://github.com/g-ch/skeleton_annotation/assets/126026624/d82d13c6-a989-42a6-9e24-317bb3a9518f" width="200" />
</p>

<p align="center">
  On the left the input image for pose estimation, in the middle the pose estimation and on the right the annotaion converted to LabelMe format
</p>

## Installation and Setup
### Prerequisites
- Ubuntu 22.04
- Python 3.8
- mmengine 2.0.0

### Step-by-Step Installation
1. **Clone Repository**: `git clone https://github.com/g-ch/skeleton_annotation.git`.
2. **Clone Libraries**: Inside 'skeleton_annotation', clone `mmpose` and `mmdetection` libraries. Visit [MMPose Installation](https://mmpose.readthedocs.io/en/latest/installation.html) and [MMDetection Installation](https://mmdetection.readthedocs.io/en/latest/get_started.html) for more details.
3. **Create Conda Environment**: Use the first lines in 'requirements.txt' to create an environment.
4. **Configure Paths**: Modify the three directories in 'config.py'.
   ![Configuration Step](https://github.com/g-ch/skeleton_annotation/assets/126026624/a225f19a-d5b7-43df-a696-56fbbdccf796)
5. **Run Config**: Navigate to ~/Pipeline/ in the terminal and execute 'config.py' to customize detection, pose estimation, and output format settings.
   ![Setup Process](https://github.com/g-ch/skeleton_annotation/assets/126026624/dc926c66-f232-4921-a3d7-82aef349887b)

## Usage
1. **Prepare Dataset**: Place your images in the '0_input_dataset' folder.
   ![Dataset Preparation](https://github.com/g-ch/skeleton_annotation/assets/126026624/9134fcb3-94f5-4995-91b9-3a796a497a87)
2. **Execute Runner**: Run 'runner.py'. The output is verbose, showing any warnings.
   ![Execution Step](https://github.com/g-ch/skeleton_annotation/assets/126026624/da884f0d-9e86-42b3-ab18-9444a3d9f9e6)
   ![stap 4 simpel deel 2](https://github.com/g-ch/skeleton_annotation/assets/126026624/5395c813-e99f-49d4-b984-55e46015f336)

4. **View Results**: Check the final results and intermediate files in the working tree.
   ![Results](https://github.com/g-ch/skeleton_annotation/assets/126026624/fbc5f58f-105c-4c58-978f-f425c29ea4c4)

**Optional: LabelMe Output Correction**
1. Create a new environment and install LabelMe.
2. Open and manually adjust the .json files.
   ![LabelMe Adjustment](https://github.com/g-ch/skeleton_annotation/assets/126026624/575d5d12-2266-4b96-a352-b4bfc17fe362)

## Customisation
### - **Detection**: Change the detection model in the config. Built-in models are available in the [MMDetection ModelZoo](https://mmdetection.readthedocs.io/en/latest/model_zoo.html).
The detection model can be easily changed by choosing a different one and entering it into the config. The built in models are found in the MMDetection ModelZoo (https://mmdetection.readthedocs.io/en/latest/model_zoo.html). If a personally trained model is prefereerd the path to this model can also be specified. 
### - **Cropping Images**: Adjust the threshold for creating cropped images in 'config.py'.
After the person detection is done, the individuals are made into seperate cropped pictures by their bounding boxes. The threshold for the creation of these cropped images is the certainty of the detection model. This can be changed in 'config.py' and should be a value between 0.0 and 1.0, representing a threshold of between 0% and 100% certainty. If it is desired to cut out other objects, line 22 in 'cut_out_bb.py' can be changed to another label. Note that this makes the next part of the pipeline useless.
### - **Pose Estimation**: Customize the pose estimation and visualisation model in 'config.py'. See [MMPose Configs](https://github.com/open-mmlab/mmpose/tree/main/configs/body_2d_keypoint).
Within 'config.py' the model used for the pose estimation can also be customised. For built in 2D person pose estimation models, see: https://github.com/open-mmlab/mmpose/tree/main/configs/body_2d_keypoint. This works best if also a trained state of the model, checkpoiny file, is provided. If a personally trained model is preferred the directory can be provided. Furthermore the visualisation output options can be changed, a heatmap can be added and the threshold for the visualisation of keypoints can be adjusted.
Beware: if changing to a different annotation than the Coco-format, the .json file created for LabelMe will stop working.
### - **Pose Correction**: Choose between different .json output formats in 'config.py'.
Within 'çonfig.py' there are two options for the format of the .json file that is created. One where solely the keypoints are visible and one where the connecting lines between the keypoints are also visualised. To alter the output it is required to manually move keypoints by drag and dropping. When the connecting lines are also visualised the endpoints of these need to be moved seperate to the keypoints by drag and dropping as well.

## References
1. Zhang, Arthur and Eranki, Chaitanya and Zhang, Christina and Hong, Raymond and Kalyani, Pranav and Kalyanaraman, Lochana and Gamare, Arsh and Bagad, Arnav and Esteva, Maria and Biswas, Joydeep; "UT Campus Object Dataset (CODa)", Texas Data Repository, 2023
