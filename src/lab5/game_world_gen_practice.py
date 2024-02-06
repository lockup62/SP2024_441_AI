'''
Lab 5: PCG and Project Lab

This a combined procedural content generation and project lab. 
You will be creating the static components of the game that will be used in the project.
Use the landscape.py file to generate a landscape for the game using perlin noise.
Use the lab 2 cities_n_routes.py file to generate cities and routes for the game.
Draw the landscape, cities and routes on the screen using pygame.draw functions.
Look for triple quotes for instructions on what to do where.
The intention of this lab is to get you familiar with the pygame.draw functions, 
use perlin noise to generate a landscape and more importantly,
build a mindset of writing modular code.
This is the first time you will be creating code that you may use later in the project.
So, please try to write good modular code that you can reuse later.
You can always write non-modular code for the first time and then refactor it later.
'''

import sys
import pygame
import random
import numpy as np
from landscape import get_landscape

from pathlib import Path
sys.path.append(str((Path(__file__)/'..'/'..').resolve().absolute()))
from lab2.cities_n_routes import get_randomly_spread_cities, get_routes


# TODO: Demo blittable surface helper function

''' Create helper functions here '''
def create_landscape(size):
    landscape = get_landscape(size)
    print("Created a landscape of size", landscape.shape)
    return pygame.surfarray.make_surface(landscape[:, :, :3])
def draw_cities(pygame_surface, size, city_names, city_locations_dict, radius = 4, color=(1,20,61)):
    for city in city_names:
        curLoc = city_locations_dict[city]
        pygame.draw.circle(pygame_surface, color, curLoc, radius)
def draw_routes(pygame_surface, size, routes, city_locations_dict, width = 2, color=(50,30,21)):
    for route in routes:
        loc1 = city_locations_dict[route[0]]
        loc2 = city_locations_dict[route[1]]
        pygame.draw.line(pygame_surface, color, loc1, loc2, width)

if __name__ == "__main__":
    pygame.init()
    size = width, height = 640, 480
    black = 1, 1, 1

    screen = pygame.display.set_mode(size)

    pygame_surface = create_landscape(size)

    city_names = ['Morkomasto', 'Morathrad', 'Eregailin', 'Corathrad', 'Eregarta',
                  'Numensari', 'Rhunkadi', 'Londathrad', 'Baernlad', 'Forthyr']
    city_locations = []
    routes = []

    city_locations = get_randomly_spread_cities(size, len(city_names))
    routes = [(city_names[i], city_names[(i+1) % len(city_names)]) for i in range(len(city_names) - 1)]


    ''' Setup cities and routes in here'''

    city_locations_dict = {name: location for name, location in zip(city_names, city_locations)}
    random.shuffle(routes)
    routes = routes[:10] 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(black)
        screen.blit(pygame_surface, (0, 0))

        ''' draw cities '''
        draw_cities(pygame_surface, size, city_names, city_locations_dict, 10, black)
        ''' draw first 10 routes '''
        draw_routes(pygame_surface, size, routes, city_locations_dict, 3, black)

        pygame.display.flip()
