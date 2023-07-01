import random
import math
import numpy as np
import biomes
from noise import pnoise2


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
            print("Generating world with seed: {}".format(self.seed))
            # Create a variable to store the world map
            world_map = np.zeros((self.size, self.size), dtype=int)
            
            # Parameters for the Perlin noise
            scale = 0.1
            octaves = 6
            persistence = 0.5
            lacunarity = 2.0
            
            # Generate the world map using Perlin noise
            for x in range(self.size):
                for y in range(self.size):
                    # debug
                    print("Generating biome for x: {}, y: {}".format(x, y))
                    try:
                        noise = pnoise2(x * scale,
                                        y * scale,
                                        octaves=octaves,
                                        persistence=persistence,
                                        lacunarity=lacunarity,
                                        repeatx=self.size,
                                        repeaty=self.size,
                                        base=self.seed)
                        
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
                    
                    except Exception as e:
                        # print the error message
                        print(f"An error occurred while generating noise at position ({x}, {y}): {e}")
            
            # debug
            print("Setting self.map to world_map")
            # Set the world map to the world object
            self.map = world_map

            # debug
            print("World generated successfully")
        
        except Exception as e:
            # print the error message
            print("Error generating world: {}".format(e))

        # Return the world object
        return self

    def display_world(self):
        # debug 
        print("Displaying world map")
        # Prints a grid of biomes in the world
        for x in range(self.size):
            for y in range(self.size):
                biome_id = self.map[x, y]
                # Assuming a print_symbol in the Biome object to represent the biome
                print_symbol = self.biomes[biome_id]["tile_ascii"][0]
                print(print_symbol, end=' ')
            print() # new line for next row

# Usage example
world_gen = World(size='small')
world = world_gen.generate()
world_gen.display_world()
