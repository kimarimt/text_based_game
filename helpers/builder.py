from entity.tile import Tile
from helpers.constants import DATA_DIR, TILES_DATA_FILE_PATH, MAP_DATA_FILE_PATH
from string import ascii_lowercase
import json
import os


def build_game_board():
    """
    Reads the TILE_OBJECTS_FILE_PATH and converts each piece of tile room data into
    a TILE object stores it into the game_board dictionary as the value with a letter as the key.
    :return: The game board
    :rtype: dict[str, Tile]
    """
    game_board = {}
    file_path = os.path.join(DATA_DIR, TILES_DATA_FILE_PATH)

    with open(file_path, 'r') as json_file:
        tiles_data = json.load(json_file)
        letters = ascii_lowercase[:len(tiles_data)]

        for letter, tile_data in zip(letters, tiles_data):
            name = tile_data['name']
            paths = tile_data['paths']
            center = (tile_data['center_x'], tile_data['center_y'])
            required_item = tile_data['required_item']
            available_item = tile_data['available_item']
            tile = Tile(name, paths, center, required_item, available_item)
            game_board[letter] = tile

    return game_board


def build_game_map():
    """
    Reads and processes MAP_DATA_FILE_PATH and return a nested list of
    map data lines.
    :return: The map data used for the game.
    :rtype: list[list[str]]
    """
    file_path = os.path.join(DATA_DIR, MAP_DATA_FILE_PATH)

    with open(file_path, 'r') as f:
        map_data = [list(line.rstrip()) for line in f.readlines()]
        return map_data
