def read_input_file(filename="input.txt"):
    """
    Read the input.txt file and separate the word search and words
    Parameters:
    filename (str): The name of the file to be read. Default is "input.txt"
    Returns:
    -soup_matrix (list): A list of lists, where each internal list corresponds to a row of the alphabet soup,
    and each item on the internal list is a letter.
    -words (list): A list of words to look for in the word search.

    """
    with open(filename, 'r') as file:
        content = file.read().strip().split('---')
        
        # process of the soup
        soup_lines = content[0].strip().split('\n')
        soup_matrix = [list(line.strip().split()) for line in soup_lines]
        
        # Process word 
        words = content[1].strip().split('\n')
        
        return soup_matrix, words