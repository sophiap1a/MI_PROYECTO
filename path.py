import json
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_PATH, "words.json")

words = {} # created dictonary

def load_words():
    """
    Load existing words into the JSON file
    Returns:
    dict: A dictionary with the words loaded from the JSON file. If an error occurs, an empty dictionary is returned
    """
    try:
        with open(JSON_PATH, "r") as j:
            data = json.load(j)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    return data

def save_words(new_words):
    """
    Save the word dictionary in the JSON file
    Parameters:
    new_words (dict): Dictionary with the words you want to save
    Returns:
    Nothing, just save the data in the archive
    """
    with open(JSON_PATH, "w", encoding='utf-8') as f:
        json.dump(new_words, f, indent=2, ensure_ascii=False)

words = load_words() # load