# Imports packages
import os

# A function that colors the provided text (ONLY FOR THE TERMINAL)
def color(
    text: str, fg: str | None = None,
    bg: str | None = None, bold: bool | str= False,
    end_fg: str | None= None, end_bg: str | None = None,
    end_bold: bool | str= False, reset: bool = True
) -> str:
    

    # Sets to store temporary values
    bold = '1' if bold else '0'
    end_bold = '1' if end_bold else '0'
    fg = fg.replace(" ", "") if fg else None
    bg = bg.replace(" ", "") if bg else None
    end_fg = end_fg.replace(" ", "") if end_fg else None
    end_bg = end_bg.replace(" ", "") if end_bg else None
    ends = ''

    # Checks if the user wants to reset the color or choose different color for the text that comes after the provided text
    if reset:
        ends = '\033[0m'
    if end_fg and end_bg:
        ends = f'\033[{end_bold};38;2;{end_fg};48;2;{end_bg}m'
    elif end_fg:
        ends = f'\033[{end_bold};38;2;{end_fg}m'
    elif end_bg:
        ends = f'\033[{end_bold};48;2;{end_bg}m'


    # Checks if the user wants to change both foreground and background or only one
    if fg and bg:
        return f'\033[{bold};38;2;{fg};48;2;{bg}m{text}{ends}'
    elif fg:
        return f'\033[{bold};38;2;{fg}m{text}{ends}'
    elif bg:
        return f'\033[{bold};48;2;{bg}m{text}{ends}'
    

    return f'\033[{bold}m{text}{ends}'


# Prints meta data like logo, title and description
def branding():

    # Meta Data
    META = {
        'title': 'Text Analysis - Python Project',
        'description': 'A Python-based text analysis tool that processes large books or documents. \nThe program supports exporting results to multiple file types (TXT, Json, HTML and XML)',
        "logo": "\n\n████████╗███████╗██╗  ██╗████████╗     █████╗ ███╗   ██╗ █████╗ ██╗  ██╗   ██╗███████╗██╗███████╗\n╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝    ██╔══██╗████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝██╔════╝██║██╔════╝\n   ██║   █████╗   ╚███╔╝    ██║       ███████║██╔██╗ ██║███████║██║   ╚████╔╝ ███████╗██║███████╗\n   ██║   ██╔══╝   ██╔██╗    ██║       ██╔══██║██║╚██╗██║██╔══██║██║    ╚██╔╝  ╚════██║██║╚════██║\n   ██║   ███████╗██╔╝ ██╗   ██║       ██║  ██║██║ ╚████║██║  ██║███████╗██║   ███████║██║███████║\n   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚═╝╚══════╝"
    }

    # Clears the terminal and Changes the title
    os.system('cls' if os.name == 'nt' else 'clear')

    # Colors then prints the Meta Data
    print(color(text=META['logo'], fg='255; 205; 0' ))
    print("\n\n—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————\n")
    print(f"{META['title']} \n{color(text=META['description'], fg='94; 94; 94')}")
    print("\n—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————\n")


# A function that extracts N (max_entries) entries from a sorted dictionary (sorted by values)
def get_top_entries_from_dictionary(dictionary: dict, max_entries: int, sort_descending: bool = False):
    
    # A dictionary for the top (max_entries) entries
    top_entries = {}

    # Sort dictionary by value
    sorted_dictionary = sort_dictionary_by_value(dictionary, sort_descending)

    # Keeps track of how many entries we have added to top_entries
    entry_counter = 0

    # Extracts an item from the sorted dictionary then adds them to the top_entries
    for key in sorted_dictionary:
        
        # Checks if the entry_counter reached the max entries wanted. Breaks if reached
        if entry_counter == max_entries:
            break
        
        # Adds the entry to the top_entries dictionary
        top_entries[key] = sorted_dictionary[key]

        # Increases the counter
        entry_counter += 1
    
    return top_entries

# A function that sorts dictionary by values, in descending or ascending order
def sort_dictionary_by_value(dictionary: dict, descending: bool = False) -> dict:
    
    # Returns the value from an item in the dictionary.
    def get_value_for_sorting(item): # item = (key, value)
        return item[1]
    
    # Converts dictionary to tuples in tuple, then converts to list of tuples
    # Dictionary {"...": "..."} -> Tuples inside a tuple ((..., ...), (..., ...)) -> Tuples inside a list [(..., ...), (..., ...)]
    dictionary_items_list = list(dictionary.items()) 

    # Sorts the list by using the sort helper (BUILT-IN)
    dictionary_items_list.sort(key=get_value_for_sorting, reverse=descending)
    
    # Converts the sorted list of tuples to dictionary then returns the dictionary
    return dict(dictionary_items_list)



# A function that removes punctuations from a text
def remove_punctuations(text: str) -> str:
    
    # List of punctuations
    punctuations = "\\/!@\"#£$¤%&/{([=?+´`^¨~*'_.:,;<>|½§])}\u201c\u201d\u2018\u2019"

    # Removes each punctuation from text
    for punctuation in punctuations:
        text = text.replace(punctuation, "")
    
    # Removes not needed spaces
    text = text.strip()

    return text


# Calculates the readability score (LiX) for the analyzed text
# Returns LiX score (Int) and Level (str)
def LiX_Score(total_number_of_words: int, total_number_of_sentences: int, number_of_hard_words: int):

    # Stores the readability level
    level = 'UNKNOWN'

    # A formula to calculate the score of the readability score (LiX)
    LiX = ( total_number_of_words / total_number_of_sentences) + ( (number_of_hard_words / total_number_of_words) * 100)

    # Rounds and removes decimals
    LiX = round(LiX)

    # Updates the readability level depending on the LiX score
    if LiX >= 55:
        level = 'Very Difficult'
    elif LiX <= 54 and LiX >= 45:
        level = 'Difficult'
    elif LiX <= 44 and LiX >= 35:
        level = 'Medium'
    elif LiX <= 34 and LiX >= 25:
        level = 'Easy'
    else:
        level = 'Very Easy'
    
    # Returns both readability score & level
    return LiX, level


# A function that converts the size of the file into a string with a specific unit.
def format_file_size(size: float) -> str:

    # Different units for file sizes
    units = ["B", "KB", "MB", "GB"]

    # Default format
    formatted = f"{size} {units[0]}"
    
    # Loops in units until found the best unit for the current file size
    for i in range(len(units)):

        # Converts the size from bytes to KB and so on
        resized = round(size / 1024 ** i, 2)

        if resized < 1:
            break
        
        # Update the variable
        formatted = f'{resized} {units[i]}'

    # Return file size with a suitable unit
    return formatted