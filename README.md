# Prusa CORE One OrcaSlicer Profiles

This repository houses work-in-progress OrcaSlicer print profiles for the Prusa CORE One. Each commit has a build action that creates orca_printer profiles for easy download and testing.

> [!WARNING]
> The following profiles are given as-is and could have bugs. We are not responsible for any damage done to your printer. Use with caution.

*Special thanks to LinksLab, jmac, Chris, Buns, and liberodark on the OrcaSlicer Discord for beta testing these profiles*

## Chamber Temperature Control

OrcaSlicer does not have the concept of a "minimal" and "nominal" print temperature like PrusaSlicer does. Thus, we must work around this limitation and use the chamber temperature controls that OrcaSlicer offers. The start G-Code of these profiles behaves in the following way:

- If the chamber temperature set is **<35C**
    - Use the print temperature as if it was set as "nominal" in PrusaSlicer. The minimal temperature is set to 0C
- If the chamber temperature set is **>35C**:
    - Use the print temperature as if it was set as "minimal" in PrusaSlicer. The nominal temperature is set to 0C

You may set the print temperature with the "Chamber temperature" setting for your filament. Do not check "Activate temperature control" for the filament. The start G-Code handles all commands for chamber temperature and checking this may cause unwanted behavior.