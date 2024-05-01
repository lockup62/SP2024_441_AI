import pygad
import numpy as np
import time

def game_fitness(solution, idx, elevation, size):
    fitness = 100 

    for city in solution_to_cities(solution, size):
        city_elevation = elevation[city[0], city[1]]

        if city_elevation > 0.9:
            fitness -= 2
        if city_elevation < 0.1:
            fitness -= 2
        if 0.4 < city_elevation < 0.6:
            fitness += 2
        
        x = size[0] / 10
        y = size[1] / 10

        for next_city in solution_to_cities(solution, size):
            if (not np.array_equal(next_city, city) and
                abs(next_city[0] - city[0]) <= x and
                abs(next_city[1] - city[1]) <= y
            ):
                fitness -= 3

    return fitness

def setup_GA(fitness_fn, n_cities, size):
    num_generations = 100
    num_parents_mating = 10
    solutions_per_population = 300
    num_genes = n_cities
    init_range_low = 0
    init_range_high = size[0] * size[1]
    parent_selection_type = "sss"
    keep_parents = 10
    crossover_type = "single_point"
    mutation_type = "random"
    mutation_percent_genes = 10

    ga_instance = pygad.GA(
        num_generations=num_generations,
        num_parents_mating=num_parents_mating,
        fitness_func=fitness_fn,
        sol_per_pop=solutions_per_population,
        num_genes=num_genes,
        gene_type=int,
        init_range_low=init_range_low,
        init_range_high=init_range_high,
        parent_selection_type=parent_selection_type,
        keep_parents=keep_parents,
        crossover_type=crossover_type,
        mutation_type=mutation_type,
        mutation_percent_genes=mutation_percent_genes,
        on_generation=lambda gen: time.sleep(0.01)
    )

    return fitness_fn, ga_instance

def solution_to_cities(solution, size, margin=10, min_distance=10):
    cities = []
    while len(cities) < len(solution):
        x = np.random.randint(margin, size[0] - margin)
        y = np.random.randint(margin, size[1] - margin)
        city = [x, y]
        if all(np.linalg.norm(np.array(city) - np.array(existing_city)) >= min_distance for existing_city in cities):
            cities.append(city)
    return np.array(cities)

def generate_cities(size, n_cities):
    # Load elevation data
    elevation = get_elevation(size)
    elevation = (elevation - elevation.min()) / (elevation.max() - elevation.min())

    # Setup fitness function and GA
    fitness = lambda ga_instance, solution, idx: game_fitness(
        solution, idx, elevation=elevation, size=size
    )
    fitness_function, ga_instance = setup_GA(fitness, n_cities, size)

    # Run GA to generate cities
    ga_instance.run()

    # Get the best solution
    best_solution = ga_instance.best_solution()[0]

    # Convert solution to cities and routes
    cities = solution_to_cities(best_solution, size)
    routes = [(i, (i + 1) % n_cities) for i in range(n_cities)]

    return cities, routes
