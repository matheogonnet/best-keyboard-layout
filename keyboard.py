"""This module contains functions to create and display keyboards."""


import random
from config import set_of_keys, char_list

def create_keyboard():
    """Create a new keyboard by shuffling the set of keys."""
    shuffled_char_list = list(set_of_keys.keys()) # Shuffle the set of keys to create a random new keyboard
    random.shuffle(shuffled_char_list) # Shuffle the list of characters 
    new_keyboard = {shuffled_char_list[i]: set_of_keys[char_list[i]] for i in range(len(char_list))} # Create the new keyboard with the shuffled list of characters
    return new_keyboard


def create_initial_population(population_size):
    """Create the initial population of keyboards."""
    individuals = [set_of_keys]  # QWERTY keyboard is the first individual
    for _ in range(population_size - 1): # Create the rest of the population by creating random keyboards 
        individuals.append(create_keyboard())
    return individuals


def show_keyboard(keyboard):
    """Display the keyboard."""
    rows = [
        list(keyboard.keys())[:10], # We split the keyboard in 3 rows like a real keyboard (only for a better display)
        list(keyboard.keys())[10:20],
        list(keyboard.keys())[20:29],
        [' ']
    ]
    formatted_rows = []
    for row in rows:
        formatted_row = " | ".join([f"[{key}]" for key in row]) # Format each key with brackets and separate them with a pipe (only for a better display too)
        formatted_rows.append(formatted_row.center(60))

    print("\n".join(formatted_rows))
