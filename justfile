install-macos ORCA_APP:
    # copy all the files in Prusa to the ORCA_APP/Contents/Resources/profiles/Prusa directory, preserving directory structure
    cp -R Prusa/* ORCA_APP/Contents/Resources/profiles/Prusa/

    # copy the new Prusa.json file to the ORCA_APP/Contents/Resources/profiles directory
    cp Prusa.json ORCA_APP/Contents/Resources/profiles/