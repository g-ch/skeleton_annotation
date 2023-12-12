import os
import subprocess
import sys
from config import base_dir

def run_command(command):
    print('Running:', ' '.join(command))
    try:
        subprocess.run(command, check=True)
        print(f'{command[1]} execution successful.')
    except subprocess.CalledProcessError as e:
        print(f'Error executing {command[1]}: {e}')

def process_folder():
    os.chdir(base_dir())

    files = [
        '1_detection.py',
        '2_cut_bb.py',
        '3_pose.py',
        '4_json.py'
    ]

    python_executable = sys.executable  # Path to the current Python interpreter

    for cmd in files:
        cmd_path = os.path.join(base_dir(), cmd)
        if os.path.exists(cmd_path):
            run_command([python_executable, cmd_path])
        else:
            print(f"File not found: {cmd_path}")

    print("\nProcessing complete.")

if __name__ == "__main__":
    process_folder()
