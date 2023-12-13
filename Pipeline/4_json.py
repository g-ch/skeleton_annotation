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

cut_out_bb, folder_path, good_label_me_file_path, full_label_me, output_folder, add_skeleton = get_json_setup()

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
    # File path where you want to save the JSON file
    json_file_path = f'{output_folder}/{filename.replace("_kpts.npy", "")}.json'

    # Writing JSON data
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)
        
    print('Succesfully created LabelMe Readable JSON file at ', json_file_path)
    return

def change_json(numpy_data_kpts, numpy_data_indices, image_path):
    new_json = copy.deepcopy(base_data)
    
    # Map labels to their corresponding indices in the numpy_data_kpts array
    label_to_index = {
        'nose': 0, 'right_eye': 1, 'left_eye': 2, 'right_ear': 3, 'left_ear': 4,
        'right_hip': 11, 'left_hip': 12, 'right_knee': 13, 'left_knee': 14,
        'right_ankle': 15, 'left_ankle': 16, 'shoulder_right': 5, 
        'shoulder_left': 6, 'elbow_right': 7, 'elbow_left': 8, 
        'hand_right': 9, 'hand_left': 10
    }

    # adding keypoints
    for shape in new_json['shapes']:
        label = shape['label']
        if label in label_to_index:
            index = label_to_index[label]
            shape['points'][0][0] = numpy_data_kpts[0][index][0]
            shape['points'][0][1] = numpy_data_kpts[0][index][1]
    
    if add_skeleton:
        #adding lines between keypoints
        for shape in new_json['shapes']:
            # arms
            if shape['label'] == 'left_underarm':
                shape['points'][0] = new_json['shapes'][0]['points'][0]
                shape['points'][1] = new_json['shapes'][2]['points'][0]
            if shape['label'] == 'right_underarm':
                shape['points'][0] = new_json['shapes'][1]['points'][0]
                shape['points'][1] = new_json['shapes'][3]['points'][0]
            if shape['label'] == 'left_upperarm':
                shape['points'][0] = new_json['shapes'][2]['points'][0]
                shape['points'][1] = new_json['shapes'][4]['points'][0]
            if shape['label'] == 'right_upperarm':
                shape['points'][0] = new_json['shapes'][3]['points'][0]
                shape['points'][1] = new_json['shapes'][5]['points'][0]
            # legs
            if shape['label'] == 'left_lower_leg':
                shape['points'][0] = new_json['shapes'][6]['points'][0]
                shape['points'][1] = new_json['shapes'][8]['points'][0] 
            if shape['label'] == 'right_lower_leg':
                shape['points'][0] = new_json['shapes'][7]['points'][0]
                shape['points'][1] = new_json['shapes'][9]['points'][0]
            if shape['label'] == 'left_upper_leg':
                shape['points'][0] = new_json['shapes'][8]['points'][0]
                shape['points'][1] = new_json['shapes'][10]['points'][0]
            if shape['label'] == 'right_upper_leg':
                shape['points'][0] = new_json['shapes'][9]['points'][0]
                shape['points'][1] = new_json['shapes'][11]['points'][0]
            # head 
            if shape['label'] == 'left_shoulder_ear':
                shape['points'][0] = new_json['shapes'][12]['points'][0]
                shape['points'][1] = new_json['shapes'][4]['points'][0]
            if shape['label'] == 'right_shoulder_ear':
                shape['points'][0] = new_json['shapes'][13]['points'][0]
                shape['points'][1] = new_json['shapes'][5]['points'][0]
            if shape['label'] == 'left_ear_eye':
                shape['points'][0] = new_json['shapes'][12]['points'][0]
                shape['points'][1] = new_json['shapes'][14]['points'][0]
            if shape['label'] == 'right_ear_eye':
                shape['points'][0] = new_json['shapes'][13]['points'][0]
                shape['points'][1] = new_json['shapes'][15]['points'][0]
            if shape['label'] == 'left_eye_nose':
                shape['points'][0] = new_json['shapes'][14]['points'][0]
                shape['points'][1] = new_json['shapes'][16]['points'][0]
            if shape['label'] == 'right_eye_nose':
                shape['points'][0] = new_json['shapes'][15]['points'][0]
                shape['points'][1] = new_json['shapes'][16]['points'][0]
            # torso
            if shape['label'] == 'chest':
                shape['points'][0] = new_json['shapes'][4]['points'][0]
                shape['points'][1] = new_json['shapes'][5]['points'][0]
            if shape['label'] == 'left_torso':
                shape['points'][0] = new_json['shapes'][10]['points'][0]
                shape['points'][1] = new_json['shapes'][4]['points'][0]
            if shape['label'] == 'right_torso':
                shape['points'][0] = new_json['shapes'][11]['points'][0]
                shape['points'][1] = new_json['shapes'][5]['points'][0]
            if shape['label'] == 'hips':
                shape['points'][0] = new_json['shapes'][10]['points'][0]
                shape['points'][1] = new_json['shapes'][11]['points'][0]
                
    # Read an image and convert to a NumPy array
    image = np.array(Image.open(image_path))

    new_json['imageData'] = encodeImageForJson(image)
    new_json['imagePath'] = str(image_path) 

    return new_json


# Main processing logic
try:
    print_separator()
    if add_skeleton:
        with open(full_label_me , 'r') as file:
            base_data = json.load(file)
    else:
        with open(good_label_me_file_path, 'r') as file:
            base_data = json.load(file)

    for filename in os.listdir(folder_path):
        if filename.endswith('_kpts.npy'):
            # Construct full file path
            file_path = os.path.join(folder_path, filename)
            image_path = os.path.join(cut_out_bb, f'{filename.replace("_kpts.npy", "")}.jpg')
                
            # Load the .npy files
            numpy_data_kpts = np.load(file_path)
            indices_path = os.path.join(folder_path, filename.replace("_kpts.npy", "_indices.npy"))
            numpy_data_indices = np.load(indices_path)

            # Check if the image file exists for the current npy array of keypoints
            if os.path.exists(image_path):
                print(f'\nMatching IMG file found in {image_path}')
                # image_path, numpy_data en base_data
                new_dict = change_json(numpy_data_kpts, numpy_data_indices, image_path)
                create_output_file(filename, new_dict)
            else:
                print(f"Warning: No corresponding image file found for {filename}.npy")
    print_separator()
except Exception as e:
    print(f"Error occurred: {e}")
