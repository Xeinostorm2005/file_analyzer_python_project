# Import necessary packages
import os

# Import from /src
from src.functions.common import color
from src.functions.analyze import analyze


message = {
    "title": "File Selection - Select a .txt file from the import directory",
    "found": "Found these files in the import directory:",
    "choose": "Select a file to analyze:",
    "errors": {
        "empty_file": "Error: The file you chose didn't contain any data.",
        "invalid_option": "Error: The option you entered isn't valid, please try again!"
    }
}


# Menu for file selection - Shows only found txt files in the import directory
# If there are no files returns an error!
def file_selection() -> str:

    # Prints stage title
    print(color(message["title"], fg="255; 205; 0"))

    # Find files in the import directory
    find_files = os.listdir("./import")

    # A list for found txt files
    txt_files = []

    # Find which files in the import directory is a txt file
    for file in find_files:
        if file.endswith('.txt'):
            txt_files.append(file)
    
    # Handle if txt_files is empty
    if len(txt_files) == 0:
        return 'empty'
    
    # Prints the file selection menu
    print(color(message["found"], end_fg="88; 88; 88"))

    # Displays the options of .txt files menu, as well as an option to exit the program
    for i, file in enumerate(txt_files):
        print(f"{i + 1} - {file}")

    print("0 - Exit")

    # Prints the "choose and option"
    print(color(message["choose"]), color(f"(0-{len(txt_files)})", fg="88; 88; 88"))

    # Keep asking the user until they answer correct
    while True:

        # Handles user input
        try:
            chosen = int(input(color('~> ', fg='255; 205; 0')))

            # Checks if the user input is smaller than 0 or larger than the length of the txt_files list
            if chosen < 0 or chosen > len(txt_files):
                raise ValueError
            
            # Handle response
            match chosen:
                case 0:
                    return 'exit'
                case _:
                    analyze(f'./import/{txt_files[chosen - 1]}')
                    return 'completed'
        
        # Handles specific errors
        except ValueError:
            print(color(message["errors"]['invalid_option'], fg="255; 0; 0"))

        except ZeroDivisionError:
            print(color(message["errors"]['empty_file'], fg="255; 0; 0"))
