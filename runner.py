import os
import subprocess
os.chdir('/home/jtverhoog/BEP/skeleton_annotation/mmdetection')

### Deze file runt eigenlijk mot_demo.py voor elke foto in een map en stopt de resultaten in een andere map
### Deze code kan je in de terminal (om zelfde te doen als deze python-file) runnen in (openmmlab) ~/mmdetection$:
### python demo/mot_demo.py     demo/2d_rect_cam0_0_871.jpg     configs/sort/sort_faster-rcnn_r50_fpn_8xb2-4e_mot17halftrain_test-mot17halfval.py     --detector     https://download.openmmlab.com/mmtracking/mot/faster_rcnn/faster-rcnn_r50_fpn_4e_mot17-half-64ee2ed4.pth --device cpu --out demo/mot


def process_folder(input_folder, config_file, detector_model, output_folder, device):
    # Alle fotos in input_folder in een lijst
    image_files = [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.endswith('.jpg')]

    # demo_mot.py voor elke foto runnen en resultaat met Bounding boxes in output_folder zetten
    for image_file in image_files:
        cmd = [
            'python',
            'demo/mot_demo.py',
            image_file,
            config_file,
            '--detector',
            detector_model,
            '--device',
            device,
            '--out',
            output_folder
        ]

        subprocess.run(cmd)

    ### Hier moet nog iets komen om de bounding boxes uit te knippen met mmcv.imread() / .imcrop()
    ### Zie: https://mmcv.readthedocs.io/en/latest/understand_mmcv/data_process.html
    
    print("Processing complete.")

if __name__ == "__main__":
    # Deze directories aanpassen en ook die helemaal bovenaan
    input_folder = os.path.join(os.getcwd(), '/home/jtverhoog/BEP/skeleton_annotation/Jolle_working_folder/input_folder')
    config_file = 'configs/sort/sort_faster-rcnn_r50_fpn_8xb2-4e_mot17halftrain_test-mot17halfval.py'
    detector_model = os.path.join(os.getcwd(), '/home/jtverhoog/BEP/skeleton_annotation/Jolle_working_folder/NN/NN_checkpoint_file.pth')
    ### Deze detector model kan je downloaden op https://download.openmmlab.com/mmtracking/mot/faster_rcnn/faster-rcnn_r50_fpn_4e_mot17-half-64ee2ed4.pth
    output_folder = os.path.join(os.getcwd(), '/home/jtverhoog/BEP/skeleton_annotation/Jolle_working_folder/output_folder')
    device = 'cpu'

    process_folder(input_folder, config_file, detector_model, output_folder, device)
