"""
Automation Script: DirectoryRename.py

This script performs the following:
Rename all files in a directory from one extension to another.
"""

import os
import shutil
import sys
import logging

# Setup logging
logging.basicConfig(filename="DirectoryRename.log", level=logging.INFO, format='%(asctime)s - %(message)s')

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


def rename_files(directory, old_ext, new_ext):
    validate_directory(directory)
    for filename in os.listdir(directory):
        if filename.endswith(old_ext):
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, filename.replace(old_ext, new_ext))
            os.rename(old_path, new_path)
            log_and_print(f"Renamed {old_path} to {new_path}")


if __name__ == "__main__":
    
    if len(sys.argv) != 4:
        log_and_print("Usage: DirectoryRename.py <directory> <old_extension> <new_extension>")
        sys.exit(1)
    dir_name = sys.argv[1]
    old_ext = sys.argv[2]
    new_ext = sys.argv[3]
    rename_files(dir_name, old_ext, new_ext)

