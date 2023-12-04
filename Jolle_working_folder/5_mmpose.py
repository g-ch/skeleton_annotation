import os

# replace with own directory
os.chdir('/home/jtverhoog/BEP/skeleton_annotation/mmpose')
from mmpose.apis import MMPoseInferencer

# replace these with your own  directories
input_folder = '/home/jtverhoog/BEP/skeleton_annotation/Jolle_working_folder/cut_out_bb/'  
output_folder = '/home/jtverhoog/BEP/skeleton_annotation/Jolle_working_folder/mmpose_output'

# instantiate the inferencer
inferencer = MMPoseInferencer('human', device='cpu')

# inference images
result_generator = inferencer(input_folder, black_background=False, out_dir=output_folder,show=False)

# loop tthrough results to save them all
results = [result for result in result_generator]


# Voor meer parameters en finetuning, zie: https://github.com/open-mmlab/mmpose/blob/main/docs/en/user_guides/inference.md