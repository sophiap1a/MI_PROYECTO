from path import words, save_words, JSON_PATH

def find_word(ls, word):
    """
    Look for a word in the word search at any address indicated
    Parameters:
    ls (list[list[str]]): Matrix representing the alphabet soup.
    word (str): The term that is tried to be found in the alphabet soup.
    Returns: bool: It returns True if the word is present in the alphabet soup, otherwise it returns False.
    
    """
    rows, cols = len(ls), len(ls[0])
    word_len = len(word)
    npc = False
    directions = [
        (0, 1),  # Horizontal left to right
        (0, -1), # Horizontal right to left
        (1, 0),  # Vertical from top to bottom
        (-1, 0), # Vertical from bottom to top
        (1, 1),  # Diagonal left to right and top to bottom
        (-1, -1),# Diagonal right to left and bottom to top
        (1, -1), # Diagonal right to left and top to bottom
        (-1, 1), # Diagonal left to right and bottom to top
    ]

    def is_word_at(i, j, dir_x, dir_y):
        """
        Check to see if the word is in a specific position in the word search and in a given direction.
        Parameters:
        i (int): Initial row where the word is to be verified.
        j (int): Initial column where the word is to be verified.
        dir_x (int): Direction on the x-axis (horizontal or diagonal).
        dir_y (int): Direction on the y-axis (vertical or diagonal).
        Returns: 
        bool: Return True if the word is fully present in the word search, following the directions,
        otherwise, False returns.
    
        """
        aux = True
        for k in range(word_len):
            new_i = i + k * dir_x
            new_j = j + k * dir_y
            if not (0 <= new_i < rows and 0 <= new_j < cols) or ls[new_i][new_j] != word[k]:
                aux = False
        return aux

    for i in range(rows):
        for j in range(cols):
            for dir_x, dir_y in directions:
                if is_word_at(i, j, dir_x, dir_y):
                    npc = True

    return npc


def find_words(ls, words):
    """
    Check to see if all the words in a list are present in the word search.
    Parameters:
    ls (list[list[str]]): Matrix representing the alphabet soup.
    words (list[str]): List of words to look for in the word search.
    Returns: 
    bool: Returns True if all words are present, False if at least one is missing.
    
    """
    count = 0
    npc = False
    for word in words:
        if find_word(ls, word):
            count += 1
    if count == len(words):
        npc = True

    return npc

def report_generator(ls, words):
    """
    Check to see if all the words in a list are present in the word search.
    Parameters:
    ls (list[list[str]]): Matrix representing the alphabet soup.
    words (list[str]):  List of words to check in the word search.
    Returns: 
    A dictionary where the keys are the words and the values are True (if the word is present) or False (if it is not).
    
    """
    dictionary = {}
    for word in words:
        dictionary[word] = find_word(ls, word)

    return dictionary


def save_word_results(s_matrix, search_words):
    """
    Look up the words in the word search and save the results in the JSON
    Parameters:
    s_matrix (list[list[str]]): Matrix representing the alphabet soup.
    search_words (list[str]): List of words to look for in the word search.

    Returns:
    Dictionary with the search results for each word (True or False).
    """
    # gGenerate report of get words
    results = report_generator(s_matrix, search_words)
    
    # Update the Global Dictionary
    for word in search_words:
        words[word] = results[word]
    
    # Save changes to the JSON file
    save_words(words)
    
    return results
