"""
Automation Script: DirectoryFileSearch.py

This script performs the following:
Accept directory name and file extension. Display all files with that extension.
"""

import os
import shutil
import sys
import logging

# Setup logging
logging.basicConfig(filename="DirectoryFileSearch.log", level=logging.INFO, format='%(asctime)s - %(message)s')

def log_and_print(message):
    logging.info(message)

def validate_directory(directory):
    if not os.path.exists(directory):
        log_and_print(f"Directory does not exist: {directory}")
        sys.exit(1)

def create_directory(directory):
    try:
        os.makedirs(directory, exist_ok=True)
        log_and_print(f"Created directory: {directory}")
    except Exception as e:
        log_and_print(f"Error creating directory {directory}: {e}")
        sys.exit(1)


def search_files_by_extension(directory, extension):
    validate_directory(directory)
    files_found = [f for f in os.listdir(directory) if f.endswith(extension)]
    for file in files_found:
        log_and_print(f"Found file: {file}")


if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        log_and_print("Usage: DirectoryFileSearch.py <directory> <extension>")
        sys.exit(1)
    dir_name = sys.argv[1]
    file_ext = sys.argv[2]
    search_files_by_extension(dir_name, file_ext)

