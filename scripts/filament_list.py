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
    configs = []
    if not files:
        print(f"The directory '{directory}' is empty.")
    else:
        print(f"Files in '{directory}':")
        for file in files:
            configs.append({
                "name": file.replace(".json", ""),
                "sub_path": os.path.join("filament", file),
            })

    # sort by configs "name", group by the information before the @ sign, then by length after at sign, then alphabetically after at sign
    configs.sort(key=lambda x: (x["name"].split("@")[0], len(x["name"].split("@")[1:]), x["name"].split("@")[1:]))

    for config in configs:
        print(json.dumps(config, indent=4)+",")

if __name__ == "__main__":
    # Get the directory from command line arguments
    if len(sys.argv) != 2:
        print("Usage: python list_files_in_directory.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    
    # List files in the specified directory
    list_files_in_directory(directory)