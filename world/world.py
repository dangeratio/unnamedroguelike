import random
import math
import numpy as np
import biomes
from opensimplex import OpenSimplex
# from noise import pnoise2

def debug_print(message):
    # notimplemented
    # print(message)
    pass

def error_print(message):
    print(message)

class World:
    def __init__(self, size='medium'):
        # Define the world size based on user input
        if size == 'small':
            self.size = 50
        elif size == 'medium':
            self.size = 100
        elif size == 'large':
            self.size = 200
        else:
            raise ValueError("Invalid size. Supported values are 'small', 'medium', or 'large'")
        
        # Define the default world seed
        self.seed = random.randint(0, 100000)
        # Define the default world biomes from biomes.py
        self.biomes = biomes.biomes

    def generate(self):
        try:
            # debug
            debug_print("Generating world with seed: {}".format(self.seed))
            # Create a variable to store the world map
            world_map = np.zeros((self.size, self.size), dtype=int)
            
            # Parameters for the noise
            scale = 0.1
            seed = self.seed
            
            # Initialize the OpenSimplex noise generator
            noise_generator = OpenSimplex(seed=seed)
            
            # Generate the world map using OpenSimplex noise
            for x in range(self.size):
                for y in range(self.size):
                    # debug
                    debug_print("Generating biome for x: {}, y: {}".format(x, y))
                    
                    # Generate noise using 2D noise
                    noise = noise_generator.noise2(x * scale, y * scale)
                    
                    # Select the biome based on the noise value
                    if noise < -0.2:
                        # e.g. Industrial Wasteland
                        world_map[x, y] = 2
                    elif noise < 0.2:
                        # e.g. Neon City
                        world_map[x, y] = 0
                    else:
                        # e.g. Hacker's Hideout
                        world_map[x, y] = 1
                
            # Set the world map to the world object
            self.map = world_map

            # debug
            debug_print("World generated successfully")
        
        except Exception as e:
            error_print(f"An error occurred during generation: {e}")
        
        return self


    def display_world(self):
        
        # Check if map attribute exists
        if hasattr(self, 'map'):
            # Prints a grid of biomes in the world
            for x in range(self.size):  # Corrected here
                for y in range(self.size):  # Corrected here
                    biome_id = self.map[x, y]
                    print_symbol = self.biomes[biome_id]["tile_ascii"][0]
                    print(print_symbol, end=' ')
                print() # new line for next row
        else:
            debug_print("World map has not been generated.")



# Usage example
world_gen = World(size='small')
world = world_gen.generate()
world_gen.display_world()
