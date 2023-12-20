import json
import matplotlib.colors as mcolors
from colour import RGB_to_XYZ, XYZ_to_Lab, RGB_COLOURSPACES, CCS_ILLUMINANTS
from colour.difference import delta_E_CIE2000
import os

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

def find_similar_colors(colors):
    color_groups = {}
    for color in colors:
        try:
            color_rgb = mcolors.hex2color(color)
            color_xyz = RGB_to_XYZ(color_rgb, RGB_COLOURSPACES['sRGB'].whitepoint, CCS_ILLUMINANTS['cie_2_1931']['D65'])
            color_lab = XYZ_to_Lab(color_xyz, CCS_ILLUMINANTS['cie_2_1931']['D65'])
            for group_color, group in color_groups.items():
                group_color_rgb = mcolors.hex2color(group_color)
                group_color_xyz = RGB_to_XYZ(group_color_rgb, RGB_COLOURSPACES['sRGB'].whitepoint, CCS_ILLUMINANTS['cie_2_1931']['D65'])
                group_color_lab = XYZ_to_Lab(group_color_xyz, CCS_ILLUMINANTS['cie_2_1931']['D65'])
                if delta_E_CIE2000(color_lab, group_color_lab) < 0.01:
                    group.append(color)
                    break
            else:
                color_groups[color] = [color]
        except ValueError:
            print(f"Invalid color value: {color}")

    representative_colors = {}
    for group_color, group in color_groups.items():
        avg_color_rgb = [sum(mcolors.hex2color(c)[i] for c in group) / len(group) for i in range(3)]
        avg_color_hex = mcolors.rgb2hex(avg_color_rgb)
        representative_colors[group_color] = avg_color_hex

    return color_groups, representative_colors

def replace_colors(data, color_groups, representative_colors):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list, tuple)):
                replace_colors(value, color_groups, representative_colors)
            elif key == 'color':
                for group_color, group in color_groups.items():
                    if value in group:
                        data[key] = representative_colors[group_color]
                        break
    elif isinstance(data, (list, tuple)):
        for i in range(len(data)):
            if isinstance(data[i], (dict, list, tuple)):
                replace_colors(data[i], color_groups, representative_colors)
            else:
                for group_color, group in color_groups.items():
                    if data[i] in group:
                        data[i] = representative_colors[group_color]
                        break


def print_colors_in_json(file_path, colors):
    data = read_json_file(file_path)
    color_groups, streamlined_colors = find_similar_colors(colors)
    replace_colors(data, color_groups, streamlined_colors)
    output = json.dumps(data, indent=4)
    print(output)

    save_output = input("Do you want to save the output? (y/n): ")
    if save_output.lower() == 'y':
        use_default = input("Do you want to use the default filename streamlined_theme.json? (y/n): ")
        if use_default.lower() == 'y':
            output_file = 'streamlined_theme.json'
        else:
            output_file = input("Please enter the filename to save as (including extension): ")
        output_path = os.path.join('helpers', 'output', output_file)
        if os.path.exists(output_path):
            overwrite = input("File already exists. Do you want to overwrite it? (y/n): ")
            if overwrite.lower() != 'y':
                output_file = input("Please enter a new file name: ")
                output_path = os.path.join('helpers', 'output', output_file)
        with open(output_path, 'w') as file:
            file.write(output)

load_default = input("Do you want to load the helpers/working_version/original_theme.json file? (y/n): ")
if load_default.lower() == 'y':
    file_path = './helpers/working_version/original_theme.json'
else:
    file_path = input("Please enter the relative path to the initial file: ")

data = read_json_file(file_path)
colors = extract_unique_colors(data)
print_colors_in_json(file_path, colors)