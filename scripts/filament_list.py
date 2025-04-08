# list all files in the filament directory

import os
import sys
import json

def list_files_in_directory(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    # List all files in the directory
    files = os.listdir(directory)
    if not files:
        print(f"The directory '{directory}' is empty.")
    else:
        print(f"Files in '{directory}':")
        for file in files:
            print(json.dumps({
                "name": file.replace(".json", ""),
                "sub_path": os.path.join("filament", file),
            }, indent=4) + ",")

if __name__ == "__main__":
    # Get the directory from command line arguments
    if len(sys.argv) != 2:
        print("Usage: python list_files_in_directory.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    
    # List files in the specified directory
    list_files_in_directory(directory)