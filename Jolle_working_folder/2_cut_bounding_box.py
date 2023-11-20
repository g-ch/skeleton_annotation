import json
from PIL import Image
import numpy as np
import os

# Specify the folder path
folder_path = '/home/jtverhoog/BEP/skeleton_annotation/Dataset_selection'

# Threshold for person detection certainty
threshold = 0.5

# Loop over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg'):
        # Construct the paths for the image and JSON files
        image_path = os.path.join(folder_path, filename)
        json_path = os.path.join('/home/jtverhoog/BEP/skeleton_annotation/Jolle_working_folder/det_output/preds/', f'{os.path.splitext(filename)[0]}.json')

        # Check if the JSON file exists for the current image
        if os.path.exists(json_path):
            # Your existing code to process the image and JSON files goes here
            original_image = image_path
            json_file_path = json_path

            with open(json_file_path, 'r') as file:
                json_data = json.load(file)

            # Loop through each detection
            j = 0
            for i, label in enumerate(json_data['labels']):
                if label == 0 and json_data['scores'][i] > threshold:
                    # Get bounding box coordinates
                    bbox = json_data['bboxes'][i]
                    x, y, w, h = map(int, bbox)

                    # Load and crop the image 
                    img_path = original_image
                    img = Image.open(img_path)
                    cropped_img = img.crop((x, y, w, h))

                    # Save the cropped image
                    img_name = img_path.split('.')[0].rsplit('/')[-1]
                    save_path = f'{img_name}_{j}.jpg'
                    cropped_img.save(f'cut_out_bb/{save_path}')
                    j += 1
                    print('Made ',j,' cropped img of ', img_name)
            if j == 0:
                img_name = original_image.split('.')[0].rsplit('/')[-1]
                print('No people found in', img_name, 'with accuracy of more than ', threshold)
            # process_image(original_image, json_file_path)
        else:
            print(f"Warning: No corresponding JSON file found for {filename}")