### to put the skeleton on one 2D picture
import sys
sys.path.append('/home/jtverhoog/BEP/skeleton_annotation/mmpose/demo')

import inferencer_demo 

input_file = '/home/jtverhoog/BEP/skeleton_annotation/mmpose/tests/data/posetrack18/images/val/003418_mpii_test/000000.jpg'
output_folder = 'vis_results/posetrack18'
classifier = '--pose2d human'
third_command = '--vis-out-dir'
total = input_file + ' ' + classifier + ' ' + third_command + ' ' + output_folder
print(total)


