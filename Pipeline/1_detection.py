from mmdet.apis import DetInferencer
from config import get_mmdet_folder, get_directory_path, print_separator, get_detection_model
import os


os.chdir(get_mmdet_folder())
input_folder = get_directory_path('0_input_dataset')
output_folder = get_directory_path('1_detection')
detection_model, device = get_detection_model()

print_separator()
# Initialize the Detection Inferencer
print('Initialising detection inferencer...\n')

inferencer = DetInferencer(model=detection_model, device=device)

# Perform inference
result = inferencer(input_folder, out_dir=output_folder, no_save_pred=False)

print('\nDetection complete')
print_separator()