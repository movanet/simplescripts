# simplescripts
Simple Python Script I use to augment my research. GPT-4 created this script, with my "direction" :)

# Document Converter

Go to the Converter folder

This python script will convert various document types into plain text and splits the content into chunks based on a user-specified token limit. The supported document types are:

Plain text files (.txt)
Microsoft Word documents (.docx, .doc)
Microsoft Excel spreadsheets (.xls, .xlsx)
Microsoft PowerPoint presentations (.ppt, .pptx)
Portable Document Format (.pdf)
Comma Separated Values (.csv)
Each chunk of text is written to an output text file, with a custom end-of-chunk identifier.

Dependencies
This script relies on several python libraries:

os, argparse, csv, datetime, typing
pdfplumber
xlrd
python-docx
python-pptx
If not already installed, they can be added using pip:

```
pip install pdfplumber xlrd python-docx python-pptx
```

Note: Depending on your environment, you might need to use pip3 instead of pip.


Usage
The script is run from the command line and takes three arguments:

--input_folder (required): The directory containing the files to be processed.
--output_folder (required): The directory where the output text file will be saved.
--token_limit (required): The maximum number of tokens per chunk.
The script can be invoked as follows:

```
python3 convert.py --input_folder /path/to/input --output_folder /path/to/output --token_limit 1000
```

Replace /path/to/input with the path to your input directory, /path/to/output with the path to your output directory, and 1000 with your desired token limit.

Error Handling
The script will print an error message and skip any files that are not in the supported formats or cannot be processed for any reason. It will also enforce a positive integer for the --token_limit argument.

Output
The script will create an output text file in the output directory. Each chunk of text is preceded by the name of the original file and a chunk number. After each chunk, the script writes a custom end-of-chunk identifier. After processing all files, the script will print the total number of files processed, chunks created, and the name of the output file.


# Ingest all files to be passed to Semantra

Go to Ingestor folder

This repository contains a Python script that:

- Converts .docx files in a specified directory to plain text.
- Filters out unsupported files (.txt and .pdf files are supported, and converted .docx files).
- Runs a command semantra with the filtered files as arguments.
- Cleans up the converted temporary files.

The script is useful for preprocessing documents for semantic analysis with the semantra tool.

### Prerequisites
To run this script, you need:

- Python 3.6+
- python-docx package: This is used for reading .docx files.
- semantra: This is assumed to be a command-line tool installed in your system.

### Installation
#### Python
If you don't have Python installed, download it from the official site:

https://www.python.org/downloads/

#### python-docx

To install python-docx, run the following command in your terminal:

```
pip install python-docx
```

### Semantra
The installation instructions for semantra is available here https://github.com/freedmand/semantra

### Usage

```
python eat.py
```

Note: The script will perform the described steps in the current directory if the directory variable is not modified.

### Function Descriptions

get_all_files(directory: str) -> list:
This function takes a directory path as input and returns a list of all files in that directory and its subdirectories.

convert_docx_to_txt(docx_file: str) -> str:
This function takes a .docx file path as input and returns its content as a string.

is_supported_file(file: str) -> bool:
This function takes a file path as input and returns a boolean indicating whether the file has a supported format (.txt or .pdf).
