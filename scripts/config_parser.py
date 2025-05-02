import json


conversion_table = {
    "bed_temperature": 'hot_plate_temp',
    "bridge_fan_speed": 'overhang_fan_speed',
    "chamber_temperature": 'chamber_temperature',
    "disable_fan_first_layers": 'close_fan_the_first_x_layers',
    "end_filament_gcode": 'filament_end_gcode',
    "external_perimeter_fan_speed": 'overhang_fan_threshold',
    "extrusion_multiplier": 'filament_flow_ratio',
    "fan_always_on": 'reduce_fan_stop_start_freq',
    "fan_below_layer_time": 'fan_cooling_layer_time',
    "fan_speedup_time": 'fan_speedup_time',
    "fan_speedup_overhangs": 'fan_speedup_overhangs',
    "fan_kickstart": 'fan_kickstart',
    "filament_colour": '',
    "filament_cost": 'filament_cost',
    "filament_density": 'filament_density',
    "filament_deretract_speed": 'filament_deretraction_speed',
    "filament_diameter": 'filament_diameter',
    "filament_max_volumetric_speed": 'filament_max_volumetric_speed',
    "filament_notes": 'filament_notes',
    "filament_retract_before_travel": 'filament_retraction_minimum_travel',
    "filament_retract_before_wipe": 'filament_retract_before_wipe',
    "filament_retract_layer_change": 'filament_retract_when_changing_layer',
    "filament_retract_length": 'filament_retraction_length',
    "filament_retract_lift": 'filament_z_hop',
    "filament_retract_lift_above": 'filament_retract_lift_above',
    "filament_retract_lift_below": 'filament_retract_lift_below',
    "filament_retract_restart_extra": 'filament_retract_restart_extra',
    "filament_retract_speed": 'filament_retraction_speed',
    "filament_shrink": 'filament_shrink',
    "filament_soluble": 'filament_soluble',
    "filament_type": 'filament_type',
    "filament_wipe": 'filament_wipe',
    "first_layer_bed_temperature": 'hot_plate_temp_initial_layer',
    "first_layer_temperature": 'nozzle_temperature_initial_layer',
    "full_fan_speed_layer": 'full_fan_speed_layer',
    "inherits": 'inherits',
    "max_fan_speed": 'fan_max_speed',
    "min_fan_speed": 'fan_min_speed',
    "min_print_speed": 'slow_down_min_speed',
    "slowdown_below_layer_time": 'slow_down_layer_time',
    "start_filament_gcode": 'filament_start_gcode',
    "support_material_interface_fan_speed": 'support_material_interface_fan_speed',
    "temperature": 'nozzle_temperature',
    "compatible_printers_condition": '',
    "compatible_printers": 'compatible_printers',
    "compatible_prints_condition": 'compatible_prints_condition',
    "compatible_prints": 'compatible_prints',
    "filament_vendor": 'filament_vendor',
    "filament_minimal_purge_on_wipe_tower": 'filament_minimal_purge_on_wipe_tower',

    # # ignores
    # "filament_settings_id": "",
    "filament_loading_speed": "",
    "filament_loading_speed_start": "",
    "filament_unloading_speed": "",
    "filament_unloading_speed_start": "",
    "filament_toolchange_delay": "",
    "filament_cooling_moves": "",
    "filament_cooling_initial_speed": "",
    "filament_cooling_final_speed": "",
    "filament_load_time": "",
    "filament_unload_time": "",
    "filament_ramming_parameters": "",
    "filament_spool_weight": "",
    "filament_abrasive": "",
    "renamed_from": "",
    "enable_dynamic_fan_speeds": "",
    "overhang_fan_speed_0": "",
    "overhang_fan_speed_1": "",
    "overhang_fan_speed_2": "",
    "overhang_fan_speed_3": "",

    "idle_temperature": "idle_temperature",
    "chamber_minimal_temperature": "chamber_temperature",

    'filament_infill_max_speed': "",
    'filament_infill_max_crossing_speed': "",
    'filament_purge_multiplier': "",
    'filament_stamping_distance': "",
    'filament_stamping_loading_speed': "",
    'filament_multitool_ramming': "",
    'filament_multitool_ramming_volume': "",
    'filament_multitool_ramming_flow': "",
    'filament_retract_length_toolchange': "",

    "filament_settings_id": "",

    "cooling": "cooling",

    "filament_travel_slope": "",
    "filament_travel_ramping_lift": "filament_z_hop_types",

    "filament_travel_max_lift": "filament_z_hop",

}

list_types = [
    "filament_flow_ratio",
"nozzle_temperature_initial_layer",
"nozzle_temperature",
"filament_max_volumetric_speed",
"enable_pressure_advance",
"pressure_advance",
# "compatible_printers",
"slow_down_layer_time",
"slow_down_min_speed",
"reduce_fan_stop_start_freq",
"slow_down_for_layer_cooling",
"fan_cooling_layer_time",
"overhang_fan_speed",
"overhang_fan_threshold",
"fan_max_speed",
"fan_min_speed",
"hot_plate_temp",
"hot_plate_temp_initial_layer",
"filament_type",
"filament_start_gcode",
"filament_end_gcode",
"filament_notes",
"close_fan_the_first_x_layers",
"full_fan_speed_layer",
"cool_plate_temp",
"eng_plate_temp",
"cool_plate_temp_initial_layer",
"eng_plate_temp_initial_layer",
"filament_soluble",
"filament_is_support",
"filament_density",
"filament_cost",
"temperature_vitrification",
"nozzle_temperature_range_low",
"nozzle_temperature_range_high",
"additional_cooling_fan_speed",
"chamber_temperature",
"filament_retraction_length",
# "filament_z_hop_types",
"idle_temperature",
"filament_multitool_ramming",
"filament_multitool_ramming_volume",
"filament_multitool_ramming_flow",
"filament_stamping_distance",
"filament_stamping_loading_speed",
"filament_retraction_speed",
"filament_deretraction_speed",
"filament_retraction_minimum_travel",
"filament_wipe",
"enable_overhang_bridge_fan",
"support_material_interface_fan_speed",
"filament_diameter",
"filament_minimal_purge_on_wipe_tower",
"filament_retract_before_wipe",
"filament_retract_when_changing_layer",
"filament_z_hop",
"filament_retract_restart_extra",
"filament_settings_id",
"filament_vendor",
"filament_wipe_distance",
"bed_type"
]



with open("c1_filaments.ini", "r") as f:
    lines = f.readlines()

    config = {}

    missing = {}

    building = None
    building_category = None

    for line in lines:
        if line.startswith(";") or line.startswith("#") or line.strip() == "":
            continue

        line = line.strip()

        # handle header case
        if line.startswith("[") and line.endswith("]"):
            if building is not None:
                if building_category not in config:
                    config[building_category] = []
                
                config[building_category].append(building)
                building = {}
            else:
                building_category = line[1:-1].strip().split(":")[0]
                building = {}

            building["name"] = line[1:-1].strip().split(":")[1]

        else:
            key, value = line.split("=", 1)

            key = key.strip()
            value = value.strip()

            if key.strip() in conversion_table:
                key = conversion_table[key.strip()]
            else:
                if key.strip() not in missing:
                    missing[key.strip()] = []

                missing[key.strip()].append(building["name"] + "=" + value)

            if key == "chamber_temperature":
                if value == "0" and "chamber_temperature" in building and building["chamber_temperature"] != "0":
                    continue

            if key == "cooling":
                if value == "0":
                    building["fan_max_speed"] = "0"
                    building["fan_min_speed"] = "0"
                continue

            if key == "filament_z_hop_types":
                building["filament_z_hop_types"] = [
                    "Slope Lift"
                ]

                continue

            if value == "nil":
                continue

            if key != "":
                building[key] = value


    config = config["filament"]

def find_config(name):
    for preset in config:
        if preset["name"] == name:
            return preset

    return None

def get_preset(name, base="", finalize=False, special_hf=True):
    base_preset = {}

    if base != "":
        base_preset = get_preset(base)

    preset = find_config(name)
    if preset is None:
        raise ValueError(f"Preset '{name}' not found")
    
    concretized = {}

    # merge all of the inherits
    if "inherits" in preset:
        for inherit in preset["inherits"].split(";"):
            concretized.update(get_preset(inherit.strip()))

    # merge the base preset
    concretized.update(preset)

    if base != "":
        # find the keys that differ from the base preset
        ckeys = list(concretized.keys())
        for key in ckeys:
            if key in base_preset and base_preset[key] == concretized[key]:
                del concretized[key]

        concretized["inherits"] = base_preset["name"]

    if concretized["name"].startswith("Generic "):
        concretized["name"] = "Prusa " + concretized["name"]
            
    if finalize:
        print(concretized.keys())
        if "filament_type" in concretized:
            t = "pet" if concretized["filament_type"].lower() == "petg" else concretized["filament_type"].lower()
            concretized["inherits"] = "fdm_filament_" + t

        # update compatible_printers condition
        if special_hf:
            if concretized["name"].endswith("HF0.4"):
                concretized["compatible_printers"] = [
                    "Prusa COREONE HF0.4 nozzle"
                ]
            elif concretized["name"].endswith("HF0.5"):
                concretized["compatible_printers"] = [
                    "Prusa COREONE HF0.5 nozzle"
                ]
            elif concretized["name"].endswith("HF0.6"):
                concretized["compatible_printers"] = [
                    "Prusa COREONE HF0.6 nozzle"
                ]
            elif concretized["name"].endswith("HF0.8"):
                concretized["compatible_printers"] = [
                    "Prusa COREONE HF0.8 nozzle"
                ]
            elif concretized["name"].endswith("0.6"):
                concretized["compatible_printers"] = [
                    "Prusa COREONE 0.6 nozzle"
                ]
            elif concretized["name"].endswith("0.8"):
                concretized["compatible_printers"] = [
                    "Prusa COREONE 0.8 nozzle"
                ]
            elif concretized["name"].endswith("@COREONE"):
                concretized["compatible_printers"] = [
                    "Prusa COREONE 0.25 nozzle",
                    "Prusa COREONE 0.3 nozzle",
                    "Prusa COREONE 0.4 nozzle",
                    "Prusa COREONE 0.5 nozzle"
                ]
        else:
            if concretized["name"].endswith("0.6"):
                concretized["compatible_printers"] = [
                    "Prusa COREONE 0.6 nozzle",
                    "Prusa COREONE HF0.6 nozzle"
                ]
            elif concretized["name"].endswith("0.8"):
                concretized["compatible_printers"] = [
                    "Prusa COREONE 0.8 nozzle",
                    "Prusa COREONE HF0.8 nozzle"
                ]
            elif concretized["name"].endswith("@COREONE"):
                concretized["compatible_printers"] = [
                    "Prusa COREONE 0.25 nozzle",
                    "Prusa COREONE 0.3 nozzle",
                    "Prusa COREONE 0.4 nozzle",
                    "Prusa COREONE 0.5 nozzle",
                    "Prusa COREONE HF0.4 nozzle",
                    "Prusa COREONE HF0.5 nozzle"
                ]

        # orcaslicer needed params

        # "from": "system",
        # "setting_id": "GFSA04",
        # "type": "filament"
        # "instantiation": "true",

        concretized["from"] = "system"
        concretized["setting_id"] = "GFSA04"
        concretized["type"] = "filament"
        concretized["instantiation"] = "true"
        concretized["filament_id"] = concretized["name"]

        for key in concretized.keys():
            if key in list_types:
                concretized[key] = [concretized[key]]

        # alphabetize the keys
        keys = list(concretized.keys())
        keys.sort()
        sorted_concretized = {}
        for key in keys:
            sorted_concretized[key] = concretized[key]

        concretized = sorted_concretized


    return concretized


def create_bundle(base_name, hf=True, rename=None):
    bundle = {
        "base": get_preset(base_name, finalize=True, special_hf=hf),
        "0.6": get_preset(base_name + " 0.6", base_name, finalize=True, special_hf=hf),
        "0.8": get_preset(base_name + " 0.8", base_name, finalize=True, special_hf=hf),
    }

    if hf:
        bundle.update({
            "0.4hf": get_preset(base_name + " HF0.4", base_name, finalize=True, special_hf=hf),
            "0.5hf": get_preset(base_name + " HF0.5", base_name, finalize=True, special_hf=hf),
            "0.6hf": get_preset(base_name + " HF0.6", base_name, finalize=True, special_hf=hf),
            "0.8hf": get_preset(base_name + " HF0.8", base_name, finalize=True, special_hf=hf),
        })

    for preset in bundle.values():
        fn = preset["name"].replace(base_name, rename) if rename else preset["name"]
        with open(f"output/{fn}.json", "w") as f:
            data = json.dumps(preset, indent=4)
            if rename is not None:
                data = data.replace(base_name, rename)

            f.write(data)

create_bundle("Generic ABS @COREONE")
create_bundle("Generic PETG @COREONE")
create_bundle("Generic PLA @COREONE")
create_bundle("Generic FLEX @COREONE", hf=False, rename="Generic TPU @COREONE")
create_bundle("Generic PLA Silk @COREONE", hf=False)
create_bundle("Prusament ASA @COREONE")
create_bundle("Prusament ASA @COREONE", rename="Prusa Generic ASA @COREONE")
create_bundle("Prusament PLA @COREONE")
create_bundle("Prusament PA11 Carbon Fiber @COREONE", rename="Prusament PA-CF @COREONE", hf=False)
create_bundle("Prusament PC Blend @COREONE")
create_bundle("Prusament PC Blend Carbon Fiber @COREONE", rename="Prusament PC-CF @COREONE", hf=False)
create_bundle("Prusament PETG @COREONE")
create_bundle("Prusament PLA @COREONE")
create_bundle("Prusament PVB @COREONE", hf=False)
create_bundle("Prusament rPLA @COREONE", hf=False)
