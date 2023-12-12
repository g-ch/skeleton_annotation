import os
import numpy as np
import json
import base64
import io
import PIL.ExifTags
import PIL.Image
import PIL.ImageOps
from PIL import Image
import codecs
import copy
from pathlib import Path
from config import get_json_setup, print_separator

cut_out_bb, folder_path, good_label_me_file_path, output_folder = get_json_setup()

# Function definitions
def encodeImageForJson(image):
    img_pil = PIL.Image.fromarray(image, mode='RGB')
    f = io.BytesIO()
    img_pil.save(f, format='PNG')
    data = f.getvalue()
    encData = codecs.encode(data, 'base64').decode()
    encData = encData.replace('\n', '')
    return encData

def create_output_file(filename, data):
    filename_clean, _ = os.path.splitext(filename)
    
    # File path where you want to save the JSON file
    json_file_path = f'{output_folder}/{filename_clean}.json'

    # Writing JSON data
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)
        
    print('Succesfully created LabelMe Readable JSON file at ', json_file_path)
    print_separator()
    return

def change_json(numpy_data, image_path):
    new_json = copy.deepcopy(base_data)

    # Map labels to their corresponding indices in the numpy_data array
    label_to_index = {
        'nose': 0, 'right_eye': 1, 'left_eye': 2, 'right_ear': 3, 'left_ear': 4,
        'right_hip': 5, 'left_hip': 6, 'right_knee': 7, 'left_knee': 8,
        'right_ankle': 9, 'left_ankle': 10, 'shoulder_right': 11, 
        'shoulder_left': 12, 'elbow_right': 13, 'elbow_left': 14, 
        'hand_right': 15, 'hand_left': 16
    }

    for shape in new_json['shapes']:
        label = shape['label']
        if label in label_to_index:
            index = label_to_index[label]
            shape['points'][0][0] = numpy_data[0][index][0]
            shape['points'][0][1] = numpy_data[0][index][1]

    # Read an image and convert to a NumPy array
    image = np.array(Image.open(image_path))

    new_json['imageData'] = encodeImageForJson(image)
    new_json['imagePath'] = str(image_path)  # Convert Path object to string

    return new_json


# Main processing logic
try:
    with open(good_label_me_file_path, 'r') as file:
        base_data = json.load(file)

    for filename in os.listdir(folder_path):
        if filename.endswith('.npy'):
            # Construct full file path
            file_path = os.path.join(folder_path, filename)
            image_path = os.path.join(cut_out_bb, f'{os.path.splitext(filename)[0]}.jpg')
                
            # Load the .npy file
            numpy_data = np.load(file_path)

            # Check if the image file exists for the current npy array of keypoints
            if os.path.exists(image_path):
                print_separator()
                print(f'Matching IMG file found in {image_path}')
                # image_path, numpy_data en base_data
                new_dict = change_json(numpy_data, image_path)
                create_output_file(filename, new_dict)
            else:
                print(f"Warning: No corresponding image file found for {filename}.npy")
except Exception as e:
    print(f"Error occurred: {e}")
