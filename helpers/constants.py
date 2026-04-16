import os


DATA_DIR = 'data'
TILES_DATA_FILE_PATH = 'tile_objects.json'
MAP_DATA_FILE_PATH = 'game_map.txt'
CLEAR_COMMAND = "cls" if os.name == 'nt' else 'clear'
PLAYER_START = 'g'
PLAYER_TOKEN = '@'
ENEMY_SPAWN_LOCATION = 'e'
REQUIRED_KEYS = ['Jade Key', 'Obsidian Key', 'Quartz Key']
