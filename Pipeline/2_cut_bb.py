import json
from PIL import Image
import os

from config import get_mmdet_folder, get_directory_path, detection_threshold, print_separator

folder_path = get_directory_path('0_input_dataset')
print_separator()

# Loop over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg'):
        image_path = os.path.join(folder_path, filename)
        json_path = os.path.join(get_directory_path('1_detection/preds/'), f'{os.path.splitext(filename)[0]}.json')

        if os.path.exists(json_path):
            with open(json_path, 'r') as file:
                json_data = json.load(file)

            j = 0
            for i, label in enumerate(json_data['labels']):
                if label == 0 and json_data['scores'][i] > detection_threshold():
                    bbox = json_data['bboxes'][i]
                    x, y, w, h = map(int, bbox)

                    img = Image.open(image_path)
                    cropped_img = img.crop((x, y, w, h))

                    img_name, _ = os.path.splitext(filename)
                    save_path = f'2_cut_out_bb/{img_name}_{j}.jpg'
                    cropped_img.save(save_path)
                    j += 1
            print(f'Made {j} cropped img of {img_name}')

            if j == 0:
                img_name, _ = os.path.splitext(filename)
                print(f'No people found in {img_name} with accuracy of more than {detection_threshold()}')
        else:
            print(f"Warning: No corresponding JSON file found for {filename}")
print_separator()
