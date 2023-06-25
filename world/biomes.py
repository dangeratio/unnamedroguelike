# biomes.py
# this file contains biome data for the world including:
# - biome list
# - biome tiles: list of tiles that can be found in the biome
# - tile colors: list of colors for the tiles
# - tile_ascii: list of ascii representation for the tiles

# biome list
biomes = [
    # list of cyberpunk biomes that may be used in the world
    {
        "name": "Neon Cityscape",
        "tiles": ["skyscraper", "neon_sign", "street", "alley", "subway_entrance"],
        "tile_colors": [(128, 0, 128), (60, 255, 60), (20, 20, 20), (40, 40, 40), (90, 90, 90)],
        "tile_ascii": ["H", "*", "=", "#", "O"]
    },
    {
        "name": "Hacker's Hideout",
        "tiles": ["computer", "server_rack", "bookshelf", "hacker_table", "secret_door"],
        "tile_colors": [(10, 10, 10), (0, 128, 0), (80, 40, 10), (60, 60, 60), (50, 50, 50)],
        "tile_ascii": ["@", "[", "]", "T", "/"]
    },
    {
        "name": "Industrial Wasteland",
        "tiles": ["factory", "smokestack", "rusted_machinery", "barbed_wire", "toxic_waste"],
        "tile_colors": [(80, 80, 80), (50, 50, 50), (90, 80, 70), (60, 60, 60), (0, 255, 0)],
        "tile_ascii": ["F", "|", "&", "!", "X"]
    },
    {
        "name": "Black Market Bazaar",
        "tiles": ["stall", "guard", "black_market_items", "smuggler", "hidden_entrance"],
        "tile_colors": [(100, 50, 10), (50, 0, 0), (80, 40, 20), (30, 30, 30), (20, 20, 20)],
        "tile_ascii": ["S", "G", "$", "~", "?"]
    },
    {
        "name": "Corporate Enclave",
        "tiles": ["corporate_tower", "security_gate", "helipad", "executive_office", "vault"],
        "tile_colors": [(200, 200, 200), (30, 30, 30), (100, 100, 100), (150, 150, 150), (0, 128, 255)],
        "tile_ascii": ["C", "+", "H", "E", "V"]
    }
]

# The structure of each biome dictionary is:
# {
#    "name": <biome_name>,
#    "tiles": [<tile_1>, <tile_2>, ...],
#    "tile_colors": [(r1, g1, b1), (r2, g2, b2), ...],
#    "tile_ascii": [<ascii_1>, <ascii_2>, ...]
# }
