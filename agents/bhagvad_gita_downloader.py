# Please use python3
# Below code is generated by ChatGPT: https://chatgpt.com/share/672825ed-6b3c-8004-a74b-d9cbd06a84f2

import os
import shutil
import subprocess
import sys

def main():
    # Step 1: Ask for the folder path
    folder_path = input("Enter the folder path to create: ")

    # Step 2: Check if the folder path already exists
    if os.path.exists(folder_path):
        print(f"Fatal error: The folder '{folder_path}' already exists.")
        sys.exit(1)  # Exit with a fatal error

    # Create the folder
    os.makedirs(folder_path)
    print(f"Created folder: {folder_path}")

    # Change directory to the new folder
    os.chdir(folder_path)

    # Step 3: Clone the repository
    try:
        subprocess.run(["git", "clone", "git@github.com:mkrjn99/FairyTaleDB.git"], check=True)
        print("Cloned the repository.")
    except subprocess.CalledProcessError as e:
        print(f"Error while cloning the repository: {e}")
        sys.exit(1)

    # Step 4: Change directory to the cloned repo and checkout the commit
    repo_name = "FairyTaleDB"
    os.chdir(repo_name)
    try:
        subprocess.run(["git", "checkout", "20d04cb0c0a96c8667d385c0e0e17f9cce8b1d3d"], check=True)
        print("Checked out to the specified commit.")
    except subprocess.CalledProcessError as e:
        print(f"Error while checking out the commit: {e}")
        sys.exit(1)

    # Step 5: Copy the PDF file to the original directory where the script is written
    original_directory = os.path.dirname(os.path.abspath(__file__))
    source_file = os.path.join(os.getcwd(), "scriptures", "bhagvad_gita.pdf")
    destination_file = os.path.join(original_directory, "bhagvad_gita.pdf")

    try:
        shutil.copy(source_file, destination_file)
        print(f"Copied 'bhagvad_gita.pdf' to {original_directory}.")
    except FileNotFoundError:
        print("The specified PDF file does not exist in the expected path.")
        sys.exit(1)
    except Exception as e:
        print(f"Error while copying the file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()