# simplescripts
Simple Python Script I use to augment my research

Document Converter
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
