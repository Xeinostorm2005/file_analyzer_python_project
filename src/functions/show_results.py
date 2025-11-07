
# Import from /src folder
from src.functions.common import color
from src.functions.common import branding
from src.functions.export import export_results, export_results_in_terminal
from src.functions.visualize import visualize

# Different messages for different steps
message = {
    "title": "Results - View Statistics & Graphs",
    "chosen": "You have chosen {option} option!",
    "choose": "Choose one of the following options:",
    "dashboard_options": [
        "1 - Basic Statistics", 
        "2 - Word Analysis",
        "3 - Sentence Analysis",
        "4 - Character Analysis",
        "5 - Export All",
        "0 - Exit",
    ],
    "results_options": [
        "1 - View Graph",
        "2 - Print in Terminal",
        "3 - Back",
    ],
    "select": "Select an option: ",
    "invalid_option": "Error: Invalid option. Please try again!",
    
}

# Dashboard menu
def dashboard():
    
    # Prints the dashboard messages
    print(color(message["title"], fg="255; 205; 0"))
    
    print(message["choose"])
    
    for option in message["dashboard_options"]:
        print(color(option, fg="88; 88; 88"))
    
    
    print(message["select"], color("(0-5)", fg="88; 88; 88"))

    # Keeps the input running until the user answered with a valid answer
    while True:
        try:
            chosen = int(input(color('~> ', fg='255; 205; 0')))

            # Handles the answer if it is more or less than tha interval
            if chosen < 0 or chosen > 5:
                raise ValueError
            
            # Match response with correct stage
            match chosen:
                case 0:
                    return 'exit'
                case 5:
                    export_results()
                case _:
                    return results(chosen - 1)
        # Handles value errors
        except ValueError:
            print(color(message["invalid_option"], fg= "255; 0; 0"))

# Results Menu
def results(option):

    # Available options
    options = ["Basic Statistics", "Word Analysis", "Sentence Analysis", "Character Analysis"]
    
    # Re-print the branding
    branding()

    # Print the menu with its options
    print(color(message["title"], fg="255; 205; 0"))
    
    print(color(message["chosen"].replace('{option}', options[option])))
    
    for optionsd in message['results_options']:
        print(color(optionsd, fg="88; 88; 88"))

    print(message['select'], color("(0-5)", fg="88; 88; 88"))

    # Keep the input alive until valid answer
    while True:
        try:
            chosen = int(input(color('~> ', fg='255; 205; 0')))

            # Checks if answer is within interval or not
            if chosen < 1 or chosen > 3:
                raise ValueError
            
            # Match response t
            match chosen:
                case 1:
                    category = options[option].replace(" ", "_").lower()
                    visualize(category) # TODO: Showcase the graph - matplotlib
                case 2:
                    category = options[option].replace(" ", "_").lower()
                    export_results_in_terminal(category) # TODO: Print results in terminal
                case 3:
                    return

        # Handle Value Error
        except ValueError:
            print(color(message["invalid_option"], fg="255; 0; 0"))
    