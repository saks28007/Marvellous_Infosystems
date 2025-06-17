"""
Automation Script: DirectoryCopyExt.py

This script performs the following:
Copy files with specific extension from one directory to another. Create target directory at runtime.
"""

import os
import shutil
import sys
import logging

# Setup logging
logging.basicConfig(filename="DirectoryCopyExt.log", level=logging.INFO, format='%(asctime)s - %(message)s')

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


def copy_files_by_extension(src_dir, dest_dir, extension):
    validate_directory(src_dir)
    create_directory(dest_dir)
    for filename in os.listdir(src_dir):
        if filename.endswith(extension):
            src_path = os.path.join(src_dir, filename)
            dest_path = os.path.join(dest_dir, filename)
            shutil.copy2(src_path, dest_path)
            log_and_print(f"Copied {src_path} to {dest_path}")


if __name__ == "__main__":
    
    if len(sys.argv) != 4:
        log_and_print("Usage: DirectoryCopyExt.py <source_directory> <target_directory> <extension>")
        sys.exit(1)
    src = sys.argv[1]
    dst = sys.argv[2]
    ext = sys.argv[3]
    copy_files_by_extension(src, dst, ext)

