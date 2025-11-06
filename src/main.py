# Import functions from /src 
from src.functions.common import branding
from src.functions.common import color
from src.functions.file_selection import file_selection
from src.functions.show_results import dashboard

# Initialize stages - This function controls which functions to display
def main():

    # Possible values: 'file_selection', 'dashboard' or 'exit'
    stage = 'file_selection'

    # Main application loop - It makes the program keep running until the user chooses to exit
    while True:
        
        # Displays the application branding/header
        branding()

        # STAGE 1: File Selection
        if stage == 'file_selection':

            # Executes the file_selection then waits for it's response
            # Returns 'completed', 'empty' or 'exit'
            status = file_selection()
            
            # Handle Different Responses from file-selection
            match status:

                # Files were successfully selected and analyzed!
                case 'completed':
                    stage = 'dashboard'
                    continue
                
                # No files found in the import directory
                case 'empty':
                    # Error message in red color
                    message = color('Error: No files found in "import" directory!', fg='255; 0; 0')
                    print(message)
                    print('Add a txt file to the input directory.')
                    # Waits for the user to press Enter.
                    # This will be re-displayed if the user haven't added a txt file
                    input('Press Enter to continue...')
                    continue
                
                # User chose to exit the program
                case 'exit':
                    stage = 'exit'
                    continue
        
        # STAGE 2: Dashboard/Results
        if stage == 'dashboard':

            # Display the dashboard
            # Returns 'exit' when user wants to exit the program
            status = dashboard()

            # User chose to exit the program
            if status == 'exit':
                stage = 'exit'
                continue

        # STAGE 3: Exit the Application
        if stage == 'exit':
            d = "     .------------------------------.\n     |  Thank you for using our     |\n     |      file analyzer!          |\n     '------------------------------'\n       \\                      ______\n        \\                  ,-'//__\\\\`-.\n         \\               ,'  ____      `.\n          \\_________O   /   / ,-.-.      \\\n                       (/# /__`-'_| || || )\n                       ||# []/()] O || || |\n                     __`------------------'__\n                    |--| |<=={_______}=|| |--|\n                    |  | |-------------|| |  |\n                    |  | |={_______}==>|| |  |\n                    |  | |   |: _ :|   || |  |\n                    > _| |___|:===:|   || |__<\n                    :| | __| |: - :|   || | |:\n                    :| | ==| |: _ :|   || | |:\n                    :| | ==|_|:===:|___||_| |:\n                    :| |___|_|:___:|___||_| |:\n                    :| |||   ||/_\\|| ||| -| |:\n                    ;I_|||[]_||\\_/|| ||| -|_I;\n                    |_ |__________________| _|\n                    | `\\\\\\___|____|____/_//' |\n                    J : |     \\____/     | : L\n                   _|_: |      |__|      | :_|_\n                 -/ _-_.'    -/    \\-    `.-_- \\-\n                 /______\\    /______\\    /______\\\n\n\n"
            print(color(d, fg="0; 100; 255"))
            break


