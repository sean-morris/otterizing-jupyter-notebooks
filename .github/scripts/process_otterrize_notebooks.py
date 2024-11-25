import os
import subprocess
from pathlib import Path


NOTEBOOK_DIR = "raw_notebooks"
OUTPUT_DIR = "generated_notebooks"


def get_ipynb_files(directory):
    """
    Get all .ipynb files in the specified directory and its subdirectories.
    Args:
        directory (str): Path to the directory to search.
    Returns:
        list: List of paths to .ipynb files.
    """
    ipynb_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".ipynb"):
                ipynb_files.append(os.path.join(root, file))
    return ipynb_files


def get_changed_files():
    """
    Get the list of changed files in the last commit.
    """
    result = subprocess.run(["git", "diff", "--name-only", "HEAD~1", "HEAD"],
                            stdout=subprocess.PIPE, text=True, check=True)
    return result.stdout.splitlines()


def process_subfolders(folders_to_otterize, notebook_dir, output_dir):
    """
    Process subfolders, check if changes are detected, and run otter assign.
    """
    for full_folder_path in folders_to_otterize:
        relative_subfolder = str(full_folder_path).replace(f"{notebook_dir}/", "", 1)
        output_subfolder_path = Path(output_dir) / relative_subfolder
        output_subfolder_path.mkdir(parents=True, exist_ok=True)

        print(f"::notice::Otter Assign on {relative_subfolder}")
        noteboooks = get_ipynb_files(full_folder_path)
        try:
            for notebook in noteboooks:
                subprocess.run(
                    [
                        "python3", "-m", "otter", "assign",
                        notebook,
                        str(output_subfolder_path),
                        "-v"
                    ],
                    check=True
                )
        except subprocess.CalledProcessError as e:
            print(f"Error while running otter assign: {e}")


if __name__ == "__main__":
    changed_files = get_changed_files()
    folders_to_otterize = sorted(
        set(
            "/".join(path.split("/")[:3]) for path in changed_files if path.startswith(f"{NOTEBOOK_DIR}/")
        ))
    print(f"Folders to Otterize: {folders_to_otterize}")
    process_subfolders(folders_to_otterize, NOTEBOOK_DIR, OUTPUT_DIR)
