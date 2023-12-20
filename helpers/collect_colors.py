import json
import numpy as np
import matplotlib.colors as mcolors

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def extract_unique_colors(data):
    colors = set()
    for key, value in data.items():
        if isinstance(value, dict):
            colors.update(extract_unique_colors(value))
        elif isinstance(value, str) and value.startswith('#'):
            colors.add(value)
    return colors

def find_closest_color(hex_color):
    target_rgb = np.array(mcolors.hex2color(hex_color))
    min_distance = float('inf')
    closest_color_name = None

    for name, rgb in mcolors.XKCD_COLORS.items():
        distance = np.linalg.norm(target_rgb - np.array(mcolors.hex2color(rgb)))
        if distance < min_distance:
            min_distance = distance
            closest_color_name = name

    return closest_color_name

def print_colors_in_json(colors):
    color_dict = {color: find_closest_color(color) for color in colors}
    output = json.dumps(color_dict, indent=4)
    print(output)

    save_output = input("Do you want to save the output? (y/n): ")
    if save_output.lower() == 'y':
        file_name = input("Please enter the filename to save as (with extension): ")
        with open(file_name, 'w') as file:
            file.write(output)

file_path = input("Please enter the path to the JSON file: ")
data = read_json_file(file_path)
colors = extract_unique_colors(data)
print_colors_in_json(colors)