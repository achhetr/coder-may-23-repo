# file handling
# read, writing and appending

import os

dummy_file_path = "dummy.txt1"

def file_exists(file_path):
    if os.path.exists(file_path):
        return True
    else:
        raise Exception(f"{file_path} does not exist")

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def write_file(file_path):
    with open(file_path, 'w') as file:
        file.write("Hello from the app")

def append_file(file_path):
    with open(file_path, 'a') as file:
        file.write("\nAppending, Hello from the app")

try:
    file_exists(dummy_file_path)
    dummy_content = read_file(dummy_file_path)
    print(dummy_content)
    write_file(dummy_file_path)
    append_file(dummy_file_path)
except Exception as err:
    print(str(err))
    # create new files
