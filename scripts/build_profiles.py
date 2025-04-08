import json

conversion_table = {
    "overhang_speed_2": "overhang_2_4_speed",
    "support_material_threshold": "support_threshold_angle",
    "external_perimeter_acceleration": "outer_wall_acceleration",
    "perimeter_acceleration": "inner_wall_acceleration",
    "support_material_spacing": "support_base_pattern_spacing",
    "infill_speed": "sparse_infill_speed",
    "compatible_printers_condition": "compatible_printers_condition",
    "overhang_speed_3" :  "overhang_3_4_speed",
    "infill_acceleration" :  "sparse_infill_acceleration",
    "solid_infill_acceleration"  : "internal_solid_infill_acceleration",
    "travel_acceleration" : "travel_acceleration",
    "perimeter_speed" : "inner_wall_speed",
    "small_perimeter_speed" : "small_perimeter_speed",
    "external_perimeter_speed" : "outer_wall_speed",
    "support_material_interface_speed"  : "support_interface_speed",
    "support_material_speed" : "support_speed",
    "top_solid_infill_acceleration" : "top_surface_speed"
}

base = {
  "from": "system",
  "inherits": "",
  "instantiation": "true",
  "name": "",
  "type": "process"
}

def convert(file_path):
    with open(file_path, 'r') as file:

        profile = None
        snippet = None


        for line in file:
            line = line.strip()
            if line.startswith("#"): # Skip comments
                continue

            if line.startswith("["):
                if profile is not None:
                    profile.update(snippet)

                    # # write profile to file
                    # with open("c1_profiles/" + profile["name"] + ".json", 'w') as profile_file:
                    #     json.dump(profile, profile_file, indent=4)
                    print(json.dumps({
                        "name": profile["name"],
                        "sub_path": "process/" + profile["name"] + ".json"
                    }, indent=4) + ",")

                # new profile
                profile = base.copy()
                profile["name"] = line[1:-1].strip().replace("print:", "")
                

            # split by '=' and strip whitespace
            key_value = line.split('=', 1)
            key = key_value[0].strip()

            if (key == "") or (len(key_value) != 2):
                continue

            if key == "inherits":
                # handle inherits
                inherits_value = key_value[1].strip().split(";")

                base_profile = inherits_value[0].strip()

                snippets = inherits_value[1:]
                snippets = [s.strip().replace("*", "") for s in snippets if s.strip()]

                # print(f"Base profile: {base_profile}")
                # print(f"Snippets: {snippets}")

                profile["inherits"] = base_profile

                snippet = {}

                for s in snippets:
                    with open("c1_snippets/" + s + ".json", 'r') as snippet_file:
                        snippet_data = snippet_file.read()
                        
                        # parse json
                        snippet_json = json.loads(snippet_data)

                        # merge with snippet
                        snippet.update(snippet_json)

            else:
                new_key = conversion_table.get(key, key)
                profile.update({new_key: key_value[1].strip()})

            # print(f"{key_value[0].strip()} -> {new_key}")
            



convert('c1_profiles.ini')