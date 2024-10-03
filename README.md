# Machine Learning : A Genetic Algorithm for Optimal Keyboard Layout

This project implements a genetic algorithm designed to find an optimal keyboard layout that minimizes the typing effort based on a given text corpus. The project was developed during my exchange as a visiting student at the University of Malta. The code showcases the key principles of a genetic algorithm, applying mutation, crossover, elitism, and selection to evolve a population of keyboard layouts over several generations.

## Project Overview

### Objective
The goal of this project is to evolve a keyboard layout that minimizes the total effort required to type a given corpus of text. The effort is measured based on the distance each key is from the "home position" (represented by the space bar), using pre-defined distances for each character.

### Why Use a Genetic Algorithm?

A genetic algorithm (GA) is a search heuristic that mimics the process of natural selection. It is particularly useful for optimization problems with a large search space, where traditional methods might be too slow or impractical.

In this project, the genetic algorithm starts with an initial population of keyboard layouts (including the standard QWERTY layout) and evolves them over multiple generations using genetic operations like crossover, mutation, and selection.

### Key Concepts of our  Genetic Algorithm

1. **Initial Population**: 
   The algorithm begins with a population of randomly generated keyboard layouts. QWERTY is included in this population as a benchmark.

2. **Fitness Function**: 
   The fitness of each layout is evaluated based on how "difficult" it is to type a specific text corpus with that layout. The effort score is calculated by summing the distances for each character in the text.

3. **Selection**: 
   Tournament selection is used to select individuals for reproduction. A small subset of the population is chosen, and the best-performing individual in this group is selected for reproduction.

4. **2-Points Crossover**: 
   Two parent keyboard layouts are selected, and two-point crossover is performed to create offspring. The offspring inherit key positions from both parents.

5. **Mutation**: 
   Mutation introduces randomness into the evolution process by swapping two random keys in the layout with a small probability, which helps prevent the algorithm from getting stuck in local minima.

6. **Elitism**: 
   The best-performing layouts (elites) are carried over to the next generation without modification, ensuring that the population retains high-quality solutions.

--- 

### Evolution of a Generation

Each generation undergoes the following steps:
1. **Fitness Evaluation**: 
   Each keyboard layout in the population is evaluated using the fitness function, which calculates the total effort score for typing a given text corpus.
   
2. **Selection**: 
   Tournament selection is used to pick individuals for reproduction.

3. **Crossover**: 
   Two-point crossover is applied to selected individuals to create new offspring.

4. **Mutation**: 
   A small mutation rate is applied, where two random keys in a layout are swapped.

5. **Elitism**: 
   The top elite individuals are retained in the population for the next generation.

6. **Replacement**: 
   The new generation replaces the old one, and the process repeats for a set number of generations or until a convergence criterion is met (i.e., when the improvement between generations becomes negligible).

### Project Structure

The project is organized into multiple Python modules to ensure modularity and maintainability:

```bash
best-keyboard-layout/
│
├── data/
│   └── text_book.txt
│
├── keyboard.py
├── genetic_algorithm.py
├── fitness.py
├── config.py
├── main.py
├── README.md
└── requirements.txt

```

- **`main.py`**: 
  The entry point of the project, where the genetic algorithm is executed. This file manages the overall flow of the algorithm, including population initialization, fitness evaluation, and the evolution loop.

- **`keyboard.py`**: 
  Contains functions related to keyboard layout creation and display. This includes the `create_keyboard()` function that generates random layouts and the `show_keyboard()` function for visualizing the layout.

- **`genetic_algorithm.py`**: 
  Implements the core genetic operations such as crossover, mutation, selection, and elitism.

- **`fitness.py`**: 
  Defines the fitness function that calculates the effort score for typing a given text on a particular keyboard layout.

- **`config.py`**: 
  Stores configuration parameters like the keyboard layout, distances for each key, population size, mutation rate, number of generations, etc.

- **`data/text_book.txt`**: 
  A text file containing the corpus of text used for calculating the fitness scores.

### How to Run the Project

1. Clone the repository:
    ```bash
    git clone https://github.com/matheogonnet/best-keyboard-layout.git
    cd best-keyboard-layout
    ```

2. Ensure you have Python installed on your system. Install any required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the main script:
    ```bash
    python main.py
    ```

The algorithm will begin running, displaying the best keyboard layout and its corresponding effort score for each generation. After running through all generations, the optimal keyboard layout found by the genetic algorithm will be displayed.

### Example Output

During execution, you will see the evolution of the generations and the best keyboard layout for each:
``` bash
Generation 1 | Best Score: 3000.234 
Generation 2 | Best Score: 2989.892 
... 
Generation X | Best Score: 890.322 
Convergence achieved, stopping evolution.

Optimal Keyboard found :
   [Q] | [W] | [E] | [R] | [T] | [Y] | [U] | [I] | [O] | [P]       
   [A] | [S] | [D] | [F] | [G] | [H] | [J] | [K] | [L] | [:]       
   [Z] | [X] | [C] | [V] | [B] | [N] | [M] | [,] | [.] | [?]       
                        [          ]                            
                        
Optimal Score : 890.322
```



### Conclusion

This project demonstrates how a genetic algorithm can be applied to optimize a keyboard layout, reducing typing effort for a specific text corpus. It provides an introduction to genetic algorithms and highlights the importance of evolutionary principles in solving complex optimization problems.

---

### Author

This project was developed by me, Mathéo Gonnet, during my exchange at the **University of Malta**.

