# Prusa CORE One OrcaSlicer Profiles

![core one](docs/coreone.png)
![orcaslicer](docs/OrcaSlicer.png)

This repository houses work-in-progress OrcaSlicer print profiles for the Prusa CORE One. Each commit has a build action that creates orca_printer profiles for easy download and testing. The end goal of this repo is to PR to OrcaSlicer upstream and be available as a built-in profile.

> [!WARNING]
> The following profiles are given as-is and could have bugs. We are not responsible for any damage done to your printer. Use with caution.

*Special thanks to LinksLab, jmac, Chris, Buns, and liberodark on the OrcaSlicer Discord for beta testing these profiles*

Download the latest profiles [here](https://github.com/bwees/orca_coreone/releases/latest)

## Chamber Temperature Control

OrcaSlicer does not have the concept of a "minimal" and "nominal" print temperature like PrusaSlicer does. Thus, we must work around this limitation and use the chamber temperature controls that OrcaSlicer offers. The start G-Code of these profiles behaves in the following way:

- If the chamber temperature set is **<35C**
    - Use the print temperature as if it was set as "nominal" in PrusaSlicer. The minimal temperature is set to 0C
- If the chamber temperature set is **>35C**:
    - Use the print temperature as if it was set as "minimal" in PrusaSlicer. The nominal temperature is set to 0C

![chamber temperature setting](docs/chamber_setting.png)

You may set the print temperature with the "Chamber temperature" setting for your filament. Do not check "Activate temperature control" for the filament. The start G-Code handles all commands for chamber temperature and checking this may cause unwanted behavior.

## bgcode Support

bgcode is strongly recommended for Prusa Machines. It allows for compressed gcode to be sent to the printer. The WiFi on the Prusa machines is quite slow and this helps expedite print upload. OrcaSlicer does not support bgcode exports but, it can be easily added in the form of a Post-Processing script. I have developed [orca_bgcode](https://github.com/bwees/orca_bgcode) to do this. Follow the [install instructions](https://github.com/bwees/orca_bgcode/blob/main/README.md) in that repo to add bgcode support to this profile. You must set the post processing command for EACH print profile.
