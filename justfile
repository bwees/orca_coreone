install-macos:
    # copy all the files in Prusa to the ORCA_DIR/system/ directory, preserving directory structure
    cp -R Prusa/* ~/Library/Application\ Support/OrcaSlicer/system/Prusa/

    # copy the new Prusa.json file to the ORCA_DIR/Contents/Resources/profiles directory
    cp Prusa.json ~/Library/Application\ Support/OrcaSlicer/system/Prusa.json