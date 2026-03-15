import json
import os


def parent_folder_details():
    get_current_folder = os.getcwd()
    get_parent_folder_path = os.path.dirname(get_current_folder)
    return get_parent_folder_path

def get_data_from_input_file(key):
    file_path = os.path.join(parent_folder_details(), "data", "input.json")
    with open(file_path, "r") as file:
        data = json.load(file)
        return data[key]

