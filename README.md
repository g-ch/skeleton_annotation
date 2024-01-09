# Skeleton Annotation

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation and Setup](#installation-and-setup)
4. [Usage](#usage)
5. [Customisation](#customisation)
6. [Troubleshooting](#troubleshooting)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact](#contact)

## Introduction
Skeleton Annotation is a customizable pipeline designed for annotating human skeletons in image datasets. This tool is ideal for researchers and developers working in computer vision, particularly in pose estimation and person/object detection. It integrates seamlessly with popular libraries like LabelMe, offering export options for manual adjustments.

## Features
- **Person and Object Detection**: Utilizes customizable models for accurate detection.
- **Image Extraction**: Capable of extracting images of specific persons or objects.
- **Pose Prediction**: Supports pose annotation prediction with customizable models.
- **LabelMe Integration**: Export pose annotations to LabelMe format for manual adjustments.

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
3. **View Results**: Check the final results and intermediate files in the working tree.
   ![Results](https://github.com/g-ch/skeleton_annotation/assets/126026624/fbc5f58f-105c-4c58-978f-f425c29ea4c4)

**Optional: LabelMe Output Correction**
1. Create a new environment and install LabelMe.
2. Open and manually adjust the .json files.
   ![LabelMe Adjustment](https://github.com/g-ch/skeleton_annotation/assets/126026624/575d5d12-2266-4b96-a352-b4bfc17fe362)

## Customisation
- **Detection**: Change the detection model in the config. Built-in models are available in the [MMDetection ModelZoo](https://mmdetection.readthedocs.io/en/latest/model_zoo.html).
- **Cropping Images**: Adjust the threshold for creating cropped images in 'config.py'.
- **Pose Estimation**: Customize the pose estimation model in 'config.py'. See [MMPose Configs](https://github.com/open-mmlab/mmpose/tree/main/configs/body_2d_keypoint).
- **Pose Correction**: Choose between different .json output formats in 'config.py'.

## Troubleshooting
(Provide common issues and solutions here)

## Contributing
Contributions are welcome! Please refer to our [Contribution Guidelines](CONTRIBUTION_LINK) for more information.

## License
This project is licensed under the [LICENSE_NAME](LICENSE_LINK).

## Contact
For support or inquiries, please email us at [your-email@example.com](mailto:your-email@example.com) or open an issue on our [GitHub Issues page](https://github.com/g-ch/skeleton_annotation
