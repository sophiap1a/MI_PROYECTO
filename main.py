from reader import read_input_file
from soup import save_word_results

def main(): 
    """
    Main function that coordinates the reading of the file, search for words and save results.  
    Returns:
    It doesn't return anything, it just runs the program and handles errors 
    Excepciones:
    FileNotFoundError: If you can't find input.txt
    Exception: For any other errors during execution
    """      
    try:
        soup_matrix, words = read_input_file()
        
        save_word_results(soup_matrix, words)
                
    except FileNotFoundError:
        print("Error: No se encontró el archivo input.txt")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
