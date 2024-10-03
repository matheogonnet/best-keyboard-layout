"""This module contains the configuration of the genetic algorithm : the set of keys, the population size, the number of generations, the mutation rate and the tolerance."""

# Set of keys with their distances (in inches) : We consider that when we press a key, the finger go back to the initial position wich is the space key
set_of_keys = {
    'Q': 1.032, 'W': 1.032, 'E': 1.032, 'R': 1.032, 'T': 1.247, 'Y': 1.605,
    'U': 1.032, 'I': 1.032, 'O': 1.032, 'P': 1.032, 'A': 0, 'S': 0, 'D': 0,
    'F': 0, 'G': 1.0, 'H': 1.0, 'J': 0, 'K': 0, 'L': 0, ':': 0, 'Z': 1.118,
    'X': 1.118, 'C': 1.0, 'V': 1.0, 'B': 1.0, 'N': 1.0, 'M': 1.0, ',': 1.118,
    '.': 1.118, '?': 1.118, ' ': 0
}

char_list = list(set_of_keys.keys())  # List of characters

# Genetic algorithm configuration
population_size = 1000
number_of_generation = 100
mutation_rate = 0.2
tolerance = 0.001
