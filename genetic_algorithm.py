"""This module contains the genetic algorithm functions : crossover, mutation, elitism, and the best keyboard of the generation."""

import random


def crossover(parent1, parent2):
    """Crossover function that creates two children from two parents."""
    list_parent1 = list(parent1.keys()) # Get the list of keys of the parent1
    list_parent2 = list(parent2.keys()) # Get the list of keys of the parent2

    crossover_point1 = random.randint(1, len(list_parent1) - 1) # Randomly choose the first crossover point
    crossover_point2 = random.randint(1, len(list_parent1) - 1) # Randomly choose the second crossover point

    if crossover_point1 > crossover_point2: # Swap the crossover points if the first one is greater than the second one (to avoid negative slicing)
        crossover_point1, crossover_point2 = crossover_point2, crossover_point1

    # Create the first child by taking the first part of the parent1 and the second part of the parent2
    child1_part1 = list_parent1[:crossover_point1]
    child1_part2 = [key for key in list_parent2 if key not in child1_part1]

    # Create the second child by taking the first part of the parent2 and the second part of the parent1
    child2_part1 = list_parent2[:crossover_point1]
    child2_part2 = [key for key in list_parent1 if key not in child2_part1]

    # Concatenate the two parts to get the children
    child1_keys = child1_part1 + child1_part2
    child2_keys = child2_part1 + child2_part2

    # Create the children by taking the values of the parents with the keys of the children
    child1 = {child1_keys[i]: parent1[list_parent1[i]] for i in range(len(list_parent1))}
    child2 = {child2_keys[i]: parent2[list_parent2[i]] for i in range(len(list_parent2))}

    return child1, child2


def mutation(child, mutation_rate=0.1):
    """Mutation function that swaps two random keys in the child with a probability of mutation_rate."""
    if random.random() < mutation_rate: # Check if the mutation occurs with the mutation rate, if yes we swap two random keys 
        idx1, idx2 = random.sample(range(len(child)), 2)
        keys = list(child.keys()) # Get the list of keys of the child
        child[keys[idx1]], child[keys[idx2]] = child[keys[idx2]], child[keys[idx1]] # Swap the two random keys
    return child


def elitism(population, scores, elite_size=2):
    """Elitism function that selects the elite_size best individuals of the population."""
    elite_indexes = sorted(range(len(scores)), key=lambda x: scores[x])[:elite_size] # Get the indexes of the elite individuals (the best individuals) by sorting the scores
    return [population[i] for i in elite_indexes]


def crossover_mutation_elitism(actual_generation, new_generation, char_list, mutation_rate=0.1):
    """Crossover, mutation and elitism function that creates a new generation from the actual generation."""
    parent1, parent2 = random.sample(actual_generation, 2) # Select two random parents from the actual generation
    child1, child2 = crossover(parent1, parent2) # Create two children by crossovering the two parents
    child1 = mutation(child1, mutation_rate) # Mutate the first child
    child2 = mutation(child2, mutation_rate) # Mutate the second child
    
    # Add the two children to the new generation
    new_generation.append(child1) 
    new_generation.append(child2) 


def best_keyboard_of_the_generation(population, scores):
    """Return the best keyboard of the generation."""
    best_score_index = scores.index(min(scores)) # Get the index of the best score in the scores list to get the best keyboard in the population
    return population[best_score_index]
