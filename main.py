"""Main module of the project : it contains the main function that runs the genetic algorithm to find the optimal keyboard layout."""

from keyboard import create_initial_population, show_keyboard
from fitness import fitness_function, calculate_score
from genetic_algorithm import crossover_mutation_elitism, elitism, best_keyboard_of_the_generation
from config import char_list, population_size, number_of_generation, mutation_rate, tolerance, set_of_keys

#----------------------------------------------------------------------------------------------------------------------------#

def main():
    # We create the initial population and set the optimal keyboard to QWERTY
    actual_generation = create_initial_population(population_size)
    optimal_keyboard = actual_generation[0]  # We set QWERTY keyboard as the optimal keyboard (reference)
    previous_best_score = float('inf')

    # Evolution loop for the genetic algorithm
    for gen in range(number_of_generation):
        scores = fitness_function(char_list, actual_generation) # We calculate the score of each individual in the population
        best_score = min(scores) # Get the best score of the generation 
        best_keyboard = best_keyboard_of_the_generation(actual_generation, scores) # Get the best keyboard of the generation

        if best_score < calculate_score(optimal_keyboard, char_list): # Update the optimal keyboard if a better one is found
            optimal_keyboard = best_keyboard

        print(f"Generation {gen+1} | Best Score: {best_score}")

        # Check if the convergence is achieved
        if abs(previous_best_score - best_score) < tolerance:
            print("Convergence achieved, stopping evolution.")
            break
        previous_best_score = best_score # Update the previous best score

        # Apply elitism, crossover, mutation and create the new generation
        new_generation = elitism(actual_generation, scores)
        while len(new_generation) < population_size:
            crossover_mutation_elitism(actual_generation, new_generation, char_list, mutation_rate)

        actual_generation = new_generation.copy() # Update the actual generation

    # Show the optimal keyboard and its score
    print("\nOptimal Keyboard found :\n")
    show_keyboard(optimal_keyboard)
    print(f"\nOptimal Score : {calculate_score(optimal_keyboard, char_list)}")


#----------------------------------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()

#----------------------------------------------------------------------------------------------------------------------------#