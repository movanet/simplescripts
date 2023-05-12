import os
import subprocess

def get_all_files(directory):
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

directory = '.'  # Change this to the path of your directory if needed
files = get_all_files(directory)
command = ['semantra'] + files
subprocess.run(command)
