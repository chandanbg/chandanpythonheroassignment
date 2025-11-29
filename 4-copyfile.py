# Chandan
# Hero Vired Assigned 1 - Python Programming

# Q4. Sample Command: python backup.py /path/to/source /path/to/destination
# By running the script with the appropriate source and destination directories,
# it should create backups of the files in the source directory, ensuring unique file names 
# in the destination directory.


import sys
import os
import shutil
from datetime import datetime


def make_timestamped_name(filename):
    """
    Append a timestamp before the file extension.
    example.txt -> example_20251129_134500.txt
    """
    base, ext = os.path.splitext(filename)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # [web:33][web:43]
    return f"{base}_{timestamp}{ext}"


def backup_files(src_dir, dst_dir):
    # Check if source directory exists
    if not os.path.isdir(src_dir):
        print(f"Error: Source directory '{src_dir}' does not exist.")
        return

    # Check if destination directory exists
    if not os.path.isdir(dst_dir):
        print(f"Error: Destination directory '{dst_dir}' does not exist.")
        return

    # List all entries in source directory
    try:
        entries = os.listdir(src_dir)  # [web:36][web:41]
    except OSError as e:
        print(f"Error: Could not list files in '{src_dir}': {e}")
        return

    if not entries:
        print("Source directory is empty. Nothing to backup.")
        return

    for name in entries:
        src_path = os.path.join(src_dir, name)

        # Skip subdirectories; only copy files as per simple requirement
        if not os.path.isfile(src_path):
            continue

        dst_path = os.path.join(dst_dir, name)

        # If file already exists in destination, create a timestamped name
        if os.path.exists(dst_path):  # [web:34][web:45]
            new_name = make_timestamped_name(name)
            dst_path = os.path.join(dst_dir, new_name)

        try:
            # copy2 preserves metadata (timestamps, etc.)
            shutil.copy2(src_path, dst_path)  # [web:36][web:41][web:38]
            print(f"Copied: {src_path} -> {dst_path}")
        except OSError as e:
            print(f"Error copying '{src_path}' to '{dst_path}': {e}")

    print("Backup completed.")


def main():
    # sys.argv: [script_name, src_dir, dst_dir]
    if len(sys.argv) != 3:  # [web:39][web:42][web:51]
        print("Usage: python backup.py <source_dir> <destination_dir>")
        sys.exit(1)

    src_dir = sys.argv[1]
    dst_dir = sys.argv[2]

    backup_files(src_dir, dst_dir)


if __name__ == "__main__":
    main()
