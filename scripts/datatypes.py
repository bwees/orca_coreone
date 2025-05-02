import json
import os

def get_param_types(file):
    data = json.load(file)
    param_types = {}

    for param in data:
        value = data[param]
        if param == "nozzle_temperature_initial_layer":
            print(f"param: {param}, value: {value}")
        if isinstance(value, str):
            param_types[param] = 'str'
        elif isinstance(value, int):
            param_types[param] = 'int'
        elif isinstance(value, float):
            param_types[param] = 'float'
        elif isinstance(value, bool):
            param_types[param] = 'bool'
        elif isinstance(value, list):
            param_types[param] = 'list'
        elif isinstance(value, dict):
            param_types[param] = 'dict'
        else:
            param_types[param] = 'unknown'

    return param_types


# go through all json files in directory /test

def get_json_files(directory):
    json_files = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            json_files.append(os.path.join(directory, filename))
    return json_files

types = []

for f in get_json_files("/Applications/OrcaSlicer.app/Contents/Resources/profiles/Prusa/filament/"):
    with open(f, 'r') as file:
        param_types = get_param_types(file)
        types.append(param_types)

# merge all of the types together, combining dissimilar types with |

def merge_types(types):
    list_t = []
    for param_types in types:
        for param, type in param_types.items():
            if type == 'list' and param not in list_t:
                list_t.append(param)

    return list_t

merged_types = merge_types(types)

print("Merged types:")
for param in merged_types:
    print("\"" + param + "\"," )