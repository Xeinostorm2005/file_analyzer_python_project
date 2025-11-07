# Import necessary packages
from datetime import datetime
import shutil
import os
import json

# Export analysis results to multiple file formats using templates
# Supported formats: TXT, MD, JSON, HTML
def export_results():

    # A dictionary to store the data that will be loaded from analyzed.json
    data = {}

    # A Dictionary to store the templates before exporting
    templates = {
        "txt": [],
        "md": [],
        "html": []
    }

    # A dictionary for placeholders:
    # Key = placeholder, Value = path to the value in data dictionary
    placeholders = {
        "file_name": "file_name",
        "file_path": "file_path",
        "file_size": "file_size",
        "file_analyzed_at": "file_analyzed_at",
        "total_number_of_lines": "basic_statistics.total_number_of_lines",
        "total_number_of_paragraphs": "basic_statistics.total_number_of_paragraphs",
        "total_number_of_sentences": "basic_statistics.total_number_of_sentences",
        "total_number_of_words": "basic_statistics.total_number_of_words",
        "total_number_of_unique_words": "basic_statistics.total_number_of_unique_words",
        "total_number_of_characters": "basic_statistics.total_number_of_characters",
        "total_number_of_characters_without_spaces": "basic_statistics.total_number_of_characters_without_spaces",
        "average_words_per_line": "basic_statistics.average_words_per_line",
        "average_word_length": "basic_statistics.average_word_length",
        "average_words_per_sentence": "basic_statistics.average_words_per_sentence",
        "longest_word_text": "word_analysis.longest_word_text",
        "longest_word_length": "word_analysis.longest_word_length",
        "shortest_word_text": "word_analysis.shortest_word_text",
        "shortest_word_length": "word_analysis.shortest_word_length",
        "number_of_words_appearing_only_once": "word_analysis.number_of_words_appearing_only_once",
        "read_ability_score": "word_analysis.read_ability_score",
        "read_ability_level": "word_analysis.read_ability_level",
        "top_10_common_words": "word_analysis.top_10_common_words",
        "longest_sentence_text": "sentence_analysis.longest_sentence_text",
        "longest_sentence_length": "sentence_analysis.longest_sentence_length",
        "shortest_sentence_text": "sentence_analysis.shortest_sentence_text",
        "shortest_sentence_length": "sentence_analysis.shortest_sentence_length",
        "sentence_length_distribution": "sentence_analysis.sentence_length_distribution",
        "total_number_of_letters": "character_analysis.total_number_of_letters",
        "total_number_of_letters_in_percent": "character_analysis.total_number_of_letters_in_percent",
        "total_number_of_digits": "character_analysis.total_number_of_digits",
        "total_number_of_digits_in_percent": "character_analysis.total_number_of_digits_in_percent",
        "total_number_of_spaces": "character_analysis.total_number_of_spaces",
        "total_number_of_spaces_in_percent": "character_analysis.total_number_of_spaces_in_percent",
        "total_number_of_punctuations": "character_analysis.total_number_of_punctuations",
        "total_number_of_punctuations_in_percent": "character_analysis.total_number_of_punctuations_in_percent",
        "top_10_common_letters": "character_analysis.top_10_common_letters",
    }

    

    # Loads data to the dictionary, from analyzed.json
    with open("./src/temp/analyzed.json") as file:

        # Converts from JSON Format to python object
        data = json.load(file)

    # Loads then updates placeholders in the templates
    for file_type in templates:

        # Opens template file
        with open(f'./src/templates/template.{file_type}', 'r', encoding="utf-8") as file:

            # Reads line by line from file
            for current_line in file:

                # Skips unnecessary lines
                if current_line.startswith("<start_") or current_line.startswith("</end_"):
                    continue

                # Reads placeholder from placeholders
                for placeholder in placeholders:

                    # Checks if placeholder is in the current_line
                    # If it is then change it to real value
                    if placeholder in current_line:
                        # Gets the value from data dictionary using the path that is stored in placeholder dictionary
                        value = get_value_from_data(data, placeholders[placeholder])

                        if file_type == 'html':
                            readability_score_in_percent = round(data['word_analysis']['read_ability_score'] / 55 * 100, 2)
                            current_line = current_line.replace('{read_ability_score_in_percent}', f'{readability_score_in_percent}%')
                        
                        # Checks if the value is a dictionary
                        if type(value) == dict:

                            # Rewrites the value as a string for exporting
                            value = rewrite_top_entries(value, file_type) 

                            # Replaces the placeholder
                            current_line = current_line.replace(f"{{{placeholder}}}", f"{value}")
                        
                        else:

                            # Replaces the placeholder with value that isn't a dictionary
                            current_line = current_line.replace(f"{{{placeholder}}}", f"{value}")
                
                # Adds the updated line to the template storage for a specific file_type
                templates[file_type].append(current_line)
    


    # Temporary Variables
    current_time = datetime.now().strftime('%Y-%m-%d-%H-%M')
    export_path = f"./exports/{data["file_name"]}-{current_time}"

    # Create the folder [name]-[date]/ inside of export
    os.makedirs(export_path, exist_ok=True)

    # Creates the file then write the data
    for file_type in templates:
        with open(f'{export_path}/{data['file_name']}.{file_type}', 'w', encoding='utf-8') as file:
            file.writelines(templates[file_type])


    # Copies the JSON and HTML files from temp and templates
    shutil.copy("./src/temp/analyzed.json", f'{export_path}/results.json')



    print(f"Successfully exported results! You will be able to find them at: {export_path}/")



def export_results_in_terminal(category: str) -> None:

    # Here we store the analyzed data
    data = {}

    # Opens the JSON file where we saved our analyzed data
    with open('./src/temp/analyzed.json', 'r', encoding='utf-8') as file:

        # Loads the JSON format into the data dictionary
        data = json.load(file)


    # A variable to keep track if current_line is within range of <start_xxxxx> and </end_xxxxx> x is the category
    current_line_with_in_range = False

    # Stores data for a specific category
    category_data = data[category]

    # Stores the format
    format = []

    # Opens the file that has format for each category
    with open("./src/templates/template.txt", 'r', encoding="utf-8") as file:

        # Read line by line from the format file
        for current_line in file:

            # Locates when the format begins and ends for a specific category
            if current_line == f"<start_{category}>\n":
                current_line_with_in_range = True
                continue
            elif current_line == f"</end_{category}>\n":
                current_line_with_in_range = False
                continue
            
            # If current line is within range then it means that it's the correct format for the category
            if current_line_with_in_range:

                # Checks each key and updates the current line to show real data
                for key in category_data:

                    # Skips if key is not inside the current_line
                    if f"{{{key}}}" not in current_line:
                        continue

                    # Stores the value of each key
                    value = category_data[key]

                    # Checks if the value is a dictionary to rewrite it in another way
                    if type(value) == dict:

                        # Rewrites the value as a string for exporting
                        value = rewrite_top_entries(value) 

                        # Replaces the placeholder
                        current_line = current_line.replace(f"{{{key}}}", f"{value}")
                    else:
                        # Replaces the placeholder with value that isn't a dictionary
                        current_line = current_line.replace(f"{{{key}}}", f"{value}")

                # Adds the line to the format
                format.append(current_line)
    
    # Prints the format
    print("".join(format))



# A function that returns the data from a specific directory.
# Parameters needed are data and path. Data is a dictionary and path is string
# e.g: Path = "basic_statistics.total_number_of_sentences"
def get_value_from_data(data: dict, path: str):

    # Divides path into multiple steps
    keys = path.split(".") 

    # Stores the current data of each step
    current_data = data

    # Updates current_data for each step
    for key in keys: 
        current_data = current_data[key] 

    # Returns the last value where path led to.
    return current_data

# A function that handles rewriting the top entires dictionary for it to look good in the format
def rewrite_top_entries(dictionary: dict, file_type: str = 'txt') -> str:
    # Stores each value of the dictionary with specific format
    lst = [] # -> ["1. ~~~~", "2.~~~"]

    # Read key by key from dictionary and saves the index
    for i, key in enumerate(dictionary):
        
        # Checks what type of format we should use for re-writing
        if file_type == 'html':
            style = f"""<div class="flex items-center gap-3 mt-3">
                            <span class="text-sm font-bold text-slate-400 w-6">{i + 1}</span>
                            <div class="flex-1">
                                <div class="flex justify-between mb-1">
                                    <span class="text-sm font-medium text-slate-700">{key}</span>
                                    <span class="text-sm font-bold text-primary">{dictionary[key]}</span>
                                </div>
                            </div>
                        </div>
                    """
            lst.append(style)
        else:
            lst.append(f"{i +1:>4}. {key:<35} {dictionary[key]}")
    
    # Converts the list to a string and each value ends with \n then returns it
    return "\n".join(lst) # -> "1. ~~~\n2. ~~~~\n" 
















