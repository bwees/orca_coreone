# Prusa CORE One OrcaSlicer Profiles

![core one](docs/coreone.png)
![orcaslicer](docs/OrcaSlicer.png)

This repository was used for the development of the CORE One OrcaSlicer profiles. Since then, the CORE One profiles have been merged in to Orcaslicer and this repository is no longer needed. Thanks to everyone who helped develop, test, debug, and merge these profiles. This repository will remain open for additional changes to the profiles that come from Prusa.

## bgcode Support

bgcode is strongly recommended for Prusa Machines. It allows for compressed gcode to be sent to the printer. The WiFi on the Prusa machines is quite slow and this helps expedite print upload. OrcaSlicer does not support bgcode exports but, it can be easily added in the form of a Post-Processing script. I have developed [orca_bgcode](https://github.com/bwees/orca_bgcode) to do this. Follow the [install instructions](https://github.com/bwees/orca_bgcode/blob/main/README.md) in that repo to add bgcode support to this profile. You must set the post processing command for EACH print profile.
