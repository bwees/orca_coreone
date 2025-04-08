import json

filaments = json.load(open("filament_list.json"))

processed = []

with open("c1_filaments.ini", "r") as f:
    filament = None
    buff = []
    for line in f:
        if line.startswith("#"):
            continue

        if line.startswith("["):
            if filament != None:
                filament["lines"] = buff
                buff = []
                processed.append(filament)
            
            filament = {
                "name": line
            }
            continue
        
        else:
            if filament == None:
                continue

            
        if line.strip() == "":
            continue

        buff.append(line)

found = []

# find the filaments that are in filaments
for filament in processed:
    processed_name = filament["name"].split(":")[1].strip().replace("]", "")
    
    for fin in filaments:
        if processed_name in fin["name"]:
            found.append(filament)
            break

print(json.dumps(found, indent=4))
