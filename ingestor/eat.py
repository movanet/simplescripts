import os
import subprocess
import docx

def get_all_files(directory):
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def convert_docx_to_txt(docx_file):
    doc = docx.Document(docx_file)
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)
    return '\n'.join(full_text)

def is_supported_file(file):
    return file.endswith('.txt') or file.endswith('.pdf')

directory = '.'  # Change this to the path of your directory if needed
all_files = get_all_files(directory)

# Convert .docx files to plain text
converted_files = []
for file in all_files:
    if file.endswith('.docx'):
        txt_file = os.path.splitext(file)[0] + '.txt'
        converted_files.append(txt_file)
        text = convert_docx_to_txt(file)
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write(text)

# Filter out unsupported files and include converted .docx files
files_to_process = list(filter(is_supported_file, all_files)) + converted_files

command = ['semantra'] + files_to_process
subprocess.run(command)

# Clean up temporary files
for temp_file in converted_files:
    os.remove(temp_file)
