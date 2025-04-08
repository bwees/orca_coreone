# replace the string "@Prusa COREONE" with "@COREONE" in all files in the directory "Prusa/process/"

import os
import re

def rename_files_in_directory(directory):
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        os.rename(os.path.join(directory, filename), os.path.join(directory, filename.replace("@Prusa COREONE", "@COREONE")))

if __name__ == "__main__":
    # Define the directory to search for files
    directory = "Prusa/process/"
    
    # Call the function to rename files
    rename_files_in_directory(directory)
    
    print("Renaming completed.")