import json
from deepdiff import DeepDiff

# Define the paths for the two JSON files
streamlined_theme_path = './helpers/output/streamlined_theme.json'
original_theme_path = './helpers/working_version/original_theme.json'

# Load the JSON files
with open(streamlined_theme_path, 'r') as file:
    streamlined_theme = json.load(file)
    # Print the file name and the first 5 lines of the file
    print(f'File: {streamlined_theme_path}')
    print('\n'.join(json.dumps(streamlined_theme, indent=4).split('\n')[:5]))

with open(original_theme_path, 'r') as file:
    original_theme = json.load(file)
    # Print the file name and the first 5 lines of the file
    print(f'File: {original_theme_path}')
    print('\n'.join(json.dumps(original_theme, indent=4).split('\n')[:5]))

# Compare the two JSON files
diff = DeepDiff(original_theme, streamlined_theme)

# Extract the changes related to hex colors
hex_changes = {k: v for k, v in diff.items() if '#' in str(v)}

# Format the changes in a user-friendly way
formatted_changes = json.dumps(hex_changes, indent=4)

# Output the changes as a new JSON file
with open('changes.json', 'w') as file:
    file.write(formatted_changes)

# Print the changes
print(formatted_changes)