import os

def list_directory_contents(path='.'):
    try:
        # List all files and directories in the given path
        contents = os.listdir(path)
        print(f"Contents of directory '/New folder':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{path}'.")

# Example usage
list_directory_contents()  # Lists contents of the current directory
