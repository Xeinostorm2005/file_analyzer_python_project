# Necessary packages
import matplotlib.pyplot as plt
import numpy as np
import json

# Import from /src 
from src.functions.common import edit_text

def visualize(category: str) -> None:

    # Stores analyzed data
    data = {}

    # Open the JSON file where we save the analyzed data then loads the json file to data dictionary
    with open("./src/temp/analyzed.json", 'r', encoding="utf-8") as file:
        data = json.load(file)

    # Show the correct graph for a specific analysis
    match category:
        case 'basic_statistics':
            basic_statistics(data[category])
        case 'word_analysis':
            word_analysis(data[category])
        case 'sentence_analysis':
            sentence_analysis(data[category])
        case 'character_analysis':
            character_analysis(data[category])
    
    
    
def basic_statistics(data: dict) -> None:
    
    # Stores what each graph will display x is for x-axel and y for y-axle
    x = [
        "total_number_of_lines", "total_number_of_paragraphs",
        "total_number_of_sentences", "total_number_of_words", 
        "total_number_of_unique_words"
    ]
    y = [] 

    # Fetches the data for each axel
    for i, key in enumerate(x):
        x[i] = edit_text(x[i], "total_number_of_", "_", " ", capitalize_words=True)
        y.append(data[key])

    # Create a figure with specified axes
    fig, ax = plt.subplots(figsize=(12, 6))

    # Creates graphs
    create_graph("bar_chart", x, y, ax, "Text Composition", "Count")

    # Showcase bar_chart
    plt.show()

def word_analysis(data: dict) -> None:

    # Stores what each graph will display x is for x-axel and y for y-axle
    # 1st Graph
    x1 = []
    y1 = []
    # 2nd Graph
    x2 = []
    y2 = []

    # Fetches the data for first graph
    for key in data["top_10_common_words"]:
        x1.append(key)
        y1.append(data["top_10_common_words"][key])

    # Fetches the data for the second graph
    for key in data["word_length_distribution"]:
        x2.append(key)
        y2.append(data['word_length_distribution'][key])

    # Create a figure with specified axes
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Custom xticks for second graph
    custom_xticks_2 = [i for i in range(0, 25, 5)]

    # Creates graphs
    create_graph(
        "bar_chart", 
        x1, y1, ax1, 
        "Top 10 Common Words",
        "Frequency", "Words",
    )
    create_graph(
        "bar_chart", 
        x2, y2, ax2, 
        "Word Length Distribution",
        "Frequency", "Words Length (Characters)", 
        custom_xticks=custom_xticks_2, 
        label_on_bar=False
    )

    # Showcase bar_chart
    plt.show()
    

def sentence_analysis(data: dict) -> None:
    
    # Stores what each graph will display x is for x-axel and y for y-axle
    # 1st Graph
    x1 = []
    y1 = []
    # 2nd Graph
    x2 = []
    y2 = []

    # Fetches the data for first graph
    for key in data["sentence_length_distribution"]:
        x1.append(key)
        y1.append(data["sentence_length_distribution"][key])

    # Fetches the data for the second graph
    for key in data["sentence_length_frequency"]:
        x2.append(key)
        y2.append(data['sentence_length_frequency'][key])

    # Create a figure with specified axes
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Custom xticks for second graph
    custom_xticks_2 = [i for i in range(0, 100, 20)]

    # Creates graphs
    create_graph(
        "bar_chart", 
        x1, y1, ax1, 
        "Most Common Sentence Lengths",
        "Frequency", "Sentence Length (Words)"
    )
    create_graph(
        "bar_chart", 
        x2, y2, ax2, 
        "Sentence Length Distribution", 
        "Number Of Sentences", "Sentence Length (Words)",
        custom_xticks=custom_xticks_2, 
        label_on_bar=False
    )

    # Showcase bar_chart
    plt.show()

def character_analysis(data: dict) -> None:
    # Stores what each graph will display x is for x-axel and y for y-axle
    # 1st Graph
    x1 = []
    y1 = []
    # 2nd Graph
    x2 = [
        "total_number_of_letters", "total_number_of_digits", 
        "total_number_of_spaces", "total_number_of_punctuations"
    ]
    y2 = []

    # Fetches the data for first graph
    for key in data["top_10_common_letters"]:
        x1.append(key)
        y1.append(data["top_10_common_letters"][key])

    # Fetches the data for the second graph
    for i, key in enumerate(x2):
        x2[i] = edit_text(x2[i], "total_number_of_", "_", " ", capitalize_words=True)
        y2.append(data[key])

    # Create a figure with specified axes
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))


    # Creates graphs
    create_graph(
        "bar_chart", 
        x1, y1, ax1, 
        "Top 10 Most Common Letters",
        "Frequency", "Letters"
    )
    create_graph(
        "pie_chart", 
        x2, y2, ax2, 
        "Character Type Distribution", 
    )

    # Showcase bar_chart
    plt.show()


def create_graph(type: str, x: list, y: list, ax, title: str, ylabel: str = '', xlabel: str = '', custom_xticks=None, label_on_bar: bool = True):
    # Changes the looks and color of the bars
    color_map = plt.get_cmap('Oranges')
    plt.rcParams['hatch.color'] = color_map(0.2)
    plt.rcParams['hatch.linewidth'] = 8

    # Checks which type of graph
    match type:
        case "bar_chart":
            # Draws the bars
            bars = ax.bar(x, y, color=color_map(0.6), hatch='/', width=0.5)

            # Check if label on bar is true
            if label_on_bar:
                # Add value labels above each bar
                for bar in bars:
            
                    # The hight of the bar
                    height = bar.get_height()

                    # Places the text above {height}
                    ax.text(
                        bar.get_x() + bar.get_width() / 2, 
                        height, f'{height:.0f}', 
                        ha='center', 
                        va='bottom', 
                        fontsize=10
                    )
        case "pie_chart":
            # Draws a pie chart
            ax.pie(y, labels=x, autopct='%1.1f%%')
    
    # Checks if there is custom_xticks
    if custom_xticks:
        labels = [str(label) for label in custom_xticks]
        plt.xticks(custom_xticks, labels)
    else:
        # Checks if the categories has a text that is longer than 6 characters, apply rotation if yes
        if max(len(c) for c in x) > 6 and len(y) > 10:
            plt.xticks(rotation=45, fontsize=9)
            plt.tight_layout
    
    
    # Set a name for axes and for the table
    ax.set_title(title)
    ax.set_ylabel(ylabel, fontsize=12, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=12, fontweight='bold')