# Import necessary packages
from datetime import datetime
import os
import json


# Import from /src
from src.functions.common import format_file_size, get_top_entries_from_dictionary, remove_punctuations, sort_dictionary_by_value, LiX_Score

def analyze(path):

    
    # Stores Basic Statistics
    lines = 0
    paragraphs = 0
    sentences = 0
    words = 0
    unique_words = 0
    characters = 0
    characters_no_spaces = 0
    words_per_line = 0
    word_length = 0
    word_per_sentence = 0

    # Stores Word Analysis
    longest_word = ""
    longest_word_length = 0
    shortest_word = ""
    shortest_word_length = float("inf")
    words_appearing_once = 0
    read_ability_score = 0
    read_ability_level = "UNKNOWN"
    
    # Stores Sentence Analysis
    longest_sentence_text = ''
    longest_sentence_word_count = 0
    shortest_sentence_text = ''
    shortest_sentence_word_count = float('inf')

    # Stores Character Analysis
    letters = 0
    letters_percent = 0
    digits = 0
    digits_percent = 0
    punctuations = 0
    punctuations_percent = 0
    spaces = 0
    spaces_percent = 0
    


    # Temporary variables
    analyzed_At = datetime.now().strftime('%Y-%m-%d %H:%M')
    alpha = "abcdefghijklmnopqrstuvwxyzàáâãäåāăąæçćĉċčđèéêëēĕėęěƒĝğġģĥħìíîïĩīĭįıĵķĸĺļľłñńņňŋòóôõöøōŏőœŕŗřśŝşšţťŧùúûüũūŭůűųŵýŷÿźżžßþ"
    punctuations_lst = "!.?,;:-_'—\\~´`*§½\"<>()[{}]/»«&^@=+"
    hard_words_count = 0
    current_word = ""
    unique_word_frequency = {}
    unique_letters = {}
    file_size = os.path.getsize(path)
    file_name = path.replace('./import/', '').replace('.txt','')
    empty_line_counter = 0

    # Punctuations that marks the ends and starts of a sentence
    sentence_ending_punctuation = ["!", "?", ".", "\u201d", "\u2019"] # ” ’
    sentence_starting_punctuation = ["\u201c", "\u2018"] # “ ‘

    # Temporary variables for building the complete analysis
    current_sentence = ''
    sentence_words_count_frequency = {}


# TODO: ADD COMMENTS


    with open(path, "r", encoding = "utf-8") as file:
        

        for current_line in file:
            lines += 1
            current_line_length = len(current_line)

            if current_line == "\n":
                empty_line_counter += 1
            elif current_line != "\n" and empty_line_counter >= 1:
                empty_line_counter = 0
                paragraphs += 1

            for character_index, current_character in enumerate(current_line):

                # ======================================== [ Word Analysis ] ========================================
               
                if (current_character.lower() in alpha or current_character in ["-", "_"]) and current_line != "\n":
                    current_word += current_character.lower()

                if current_character in [" ", "\n"] and current_word != "":

                    words += 1
                    current_word_length = len(current_word)

                    # Update Hard Words Count
                    if current_word_length > 5:
                        hard_words_count += 1
                        
                    # Updates/Adds Longest word text & count             
                    if current_word_length > longest_word_length:
                        longest_word = current_word
                        longest_word_length = current_word_length

                    # Updates/Adds Shortest word text & count
                    if current_word_length < shortest_word_length:
                        shortest_word = current_word
                        shortest_word_length = current_word_length

                    # Updates/Adds word into unique_word_frequency
                    if current_word in unique_word_frequency:
                        unique_word_frequency[current_word] += 1
                    else:
                        unique_word_frequency[current_word] = 1

                    current_word = ""

                # ======================================== [ Sentence Analysis ] ========================================

                # Builds Current_Sentence by adding characters (Skips empty lines)
                if current_line != "\n":
                    current_sentence += current_character
                
                # Checks if the current character is a punctuation that ends the sentence and checks if the index is less than the length of the line
                if current_character in sentence_ending_punctuation and character_index < current_line_length - 1:

                    # Stores the character that comes after current character
                    next_char = current_line[character_index + 1]

                    # Valid sentence endings: Punctuation followed by New Line or space with Uppercase/opening quote
                    isvalid_sentence_ending: bool = (
                        next_char == "\n" or (
                            next_char == " " and (
                                current_line[character_index + 2].isupper() or
                                current_line[character_index + 2] in sentence_starting_punctuation
                            )
                        )
                    )
                    
                    # Verify if it's a valid sentence end
                    if isvalid_sentence_ending:

                        # Increase the total number of sentences
                        sentences += 1
                        
                        # Rewrites the sentence and removes extra spaces
                        current_sentence = current_sentence.replace("\n", " ").strip()

                        # Make a list of words in a sentence and remove punctuations
                        words_in_current_sentence = remove_punctuations(current_sentence).strip().split(" ")       # Hello, this is... -> Hello this is -> ["Hello", "this", "is"]
                        words_in_current_sentence_count = len(words_in_current_sentence)

                        # Update longest sentence
                        if words_in_current_sentence_count > longest_sentence_word_count:
                            longest_sentence_word_count = words_in_current_sentence_count
                            longest_sentence_text = current_sentence

                        # Update shortest sentence
                        if words_in_current_sentence_count < shortest_sentence_word_count:
                            shortest_sentence_word_count = words_in_current_sentence_count
                            shortest_sentence_text = current_sentence

                        # Adds/Updates word count frequency in a sentence
                        if words_in_current_sentence_count in sentence_words_count_frequency:
                            sentence_words_count_frequency[words_in_current_sentence_count] += 1 
                        else:
                            sentence_words_count_frequency[words_in_current_sentence_count] = 1 

                        # Resets current_sentence for next sentence
                        current_sentence = ""

                # ======================================== [ Character Analysis ] ========================================
                
                characters += 1

                if current_character != " ":
                    characters_no_spaces += 1

                if current_character.lower() in alpha:
                    letters += 1
                    if current_character.lower() not in unique_letters:
                        unique_letters[current_character.lower()] = 1
                    else:
                        unique_letters[current_character.lower()] += 1
                if current_character.isdigit():
                    digits += 1
                
                if current_character == " ":
                    spaces += 1

                if current_character in punctuations_lst:
                    punctuations += 1

        # Basic Statistics
        unique_words = len(unique_word_frequency)
        words_per_line = round(words / lines, 1)
        word_length = round(letters / words, 1)
        word_per_sentence = round(words / sentences, 1)


        # Word Analysis
        top_10_words = get_top_entries_from_dictionary(
            unique_word_frequency,
            max_entries = 10,
            sort_descending = True
        )
        
        sorted_words = sort_dictionary_by_value(
            unique_word_frequency
            
        )

        for key in sorted_words:
            value = sorted_words[key]

            if value != 1:
                break
            words_appearing_once += 1

        read_ability_score, read_ability_level = LiX_Score(
            total_number_of_words = words,
            total_number_of_sentences = sentences,
            number_of_hard_words = hard_words_count
        )    
            

        # Sentence Analysis
        sentence_length_distribution = get_top_entries_from_dictionary(
            sentence_words_count_frequency,
            max_entries = 5,
            sort_descending = True
        )
        
        # Character Analysis
        letters_percent = round(letters / characters * 100, 2) 
        digits_percent = round(digits / characters * 100, 2)
        spaces_percent = round(spaces / characters * 100, 2)
        punctuations_percent = round(punctuations / characters * 100, 2)
        
        top_10_letters = get_top_entries_from_dictionary(
            unique_letters,
            max_entries = 10,
            sort_descending = True
        )
        
    

    data = {
        "file_name": file_name,
        "file_path": path,
        "file_size": format_file_size(file_size),
        "file_analyzed_at": analyzed_At,
        "basic_statistics": {
            "total_number_of_lines": lines, # Complete
            "total_number_of_paragraphs": paragraphs, # Completed
            "total_number_of_sentences": sentences, # Easy-Mid
            "total_number_of_words": words, # RIP
            "total_number_of_unique_words": unique_words, # RIP
            "total_number_of_characters": characters,  # Complete
            "total_number_of_characters_without_spaces": characters_no_spaces, # Complete
            "average_words_per_line": words_per_line, # RIP
            "average_word_length": word_length, # RIP
            "average_words_per_sentence": word_per_sentence # RIP
        },
        "word_analysis": {
            "top_10_common_words": top_10_words, # RIP
            "longest_word_text": longest_word, # RIP
            "longest_word_length": longest_word_length, # RIP
            "shortest_word_text": shortest_word, # RIP
            "shortest_word_length": shortest_word_length, # RIP
            "number_of_words_appearing_only_once": words_appearing_once, # RIP
            "read_ability_score": read_ability_score, # RIP
            "read_ability_level": read_ability_level # RIP
        },
        "sentence_analysis": {
            "longest_sentence_text": longest_sentence_text, # Easy - Mid
            "longest_sentence_length": longest_sentence_word_count, # Easy - Mid
            "shortest_sentence_text": shortest_sentence_text, # Easy - Mid
            "shortest_sentence_length": shortest_sentence_word_count, # Easy - Mid
            "sentence_length_distribution": sentence_length_distribution # Easy - Mid
        },
        "character_analysis": {
            "total_number_of_letters": letters, # Complete
            "total_number_of_letters_in_percent": f"{letters_percent}%", # Completed
            "total_number_of_digits": digits, # Complete
            "total_number_of_digits_in_percent": f"{digits_percent}%", # Completed
            "total_number_of_spaces": spaces, # Complete
            "total_number_of_spaces_in_percent": f"{spaces_percent}%", # Completed
            "total_number_of_punctuations": punctuations, # Complete
            "total_number_of_punctuations_in_percent": f"{punctuations_percent}%", # Completed
            "top_10_common_letters": top_10_letters, # Completed
        }
    }

    # Export the analyzed data to json.
    # Path: "./src/temp/analyzed.json"
    with open("./src/temp/analyzed.json", "w", encoding = "utf-8") as file:
        file.write(json.dumps(data, indent = 4))
    