"""This module contains the fitness function for the genetic algorithm."""

def calculate_score(keyboard, char_list):
    """Calculate the score of a keyboard."""
    score = 0 
    with open("data/text_book.txt", "r") as f: # "text_book.txt" is the corpus of text took as reference from a book
        text = f.read() 
        for char in text: # For each character in the text we calculate the distance of each key
            if char in keyboard:
                score += keyboard[char]
    return score

def fitness_function(char_list, population):
    """Calculate the score of each individual in the population."""
    return [calculate_score(individual, char_list) for individual in population]
