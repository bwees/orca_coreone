# converts gcode to a \n delimited string for json
import sys
import pyperclip

with open(sys.argv[1], "r") as f:
    code = f.read()

    
    # escape quotes, newlines
    code = code.replace("'", "\\'")
    code = code.replace('"', '\\"')
    code = code.replace("\n", "\\n")



    print(code)
    print()
    print("Copied to clipboard")
    
    pyperclip.copy(code)


