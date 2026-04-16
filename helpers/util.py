from helpers.constants import CLEAR_COMMAND, ENEMY_SPAWN, PLAYER_TOKEN, REQUIRED_KEYS
from entity.tile import Tile
from time import sleep
import subprocess


def clear(seconds=1):
    """
    Clears the terminal screen after a time delay (defaults to 1 second).
    :param seconds: The number of seconds for the time delay.
    :type seconds: int
    """
    sleep(seconds)
    subprocess.run(CLEAR_COMMAND, shell=True)


def print_introduction():
    """
    Prints the game introduction to the screen.
    """
    print('Welcome to the Blackwood Mansion')
    print('Collect the Jade, Obsidian, and Quartz Keys and get back to the Entrance in order to escape the mansion.')
    print('But the evil Dr. Blackwood will appear at any time to capture you. Find the secret item to defeat him')
    print('Good luck and Goodspeed Agent Kent')
    input('Press any key to continue...')


def render_map(game_map, current_room):
    """
    Places the PLAYER_TOKEN at the center of the current room
    and renders the game_map.
    :param game_map: The game map
    :type game_map: list[list[str]]
    :param current_room: The current room
    :type current_room: Tile
    """
    x, y = current_room.center
    game_map[y][x] = PLAYER_TOKEN

    for row in game_map:
        for cell in row:
            print(cell, end='')
        print()


def clear_player_token(game_map, current_room):
    """
    Clears the PLAYER_TOKEN from the current_room
    :param game_map: The game map
    :type game_map: list[list[str]]
    :param current_room: the current roo
    :type current_room: Tile
    """
    x, y = current_room.center
    game_map[y][x] = ' '


def did_player_win(inventory, current_room):
    """
    Checks if the player has all the required keys and made it back to the return
    :param inventory: The player's inventory.
    :type inventory: list[str]
    :param current_room: The current room.
    :type current_room: Tile
    :return: Whether the player fulfilled the win conditions
    :rtype: bool
    """
    return all(key in inventory for key in REQUIRED_KEYS) \
        and 'Entrance' in current_room.name


def did_player_lose(inventory, current_room):
    """
    Checks if the player in is the same location as the enemy and doesn't have the item
    required to defeat it.
    :param inventory: The player's inventory.
    :type inventory: list[str]
    :param current_room: The current room.
    :type current_room: Tile
    :return: Whether the player fulfilled the game over conditions.
    :rtype: bool
    """
    return 'Pistol' not in inventory \
        and current_room.available_item == 'Enemy'


def enemy_already_spawned(game_board):
    """
    Checks if the enemy spawned at the specified location.
    :param game_board: The game board.
    :type game_board: dict[str, Tile]
    :return: Whether is enemy spawned or not
    :rtype: bool
    """
    return game_board[ENEMY_SPAWN].available_item == 'Enemy'


def spawn_enemy(game_board):
    """
    Spawns the enemy at the specified location based on the ENEMY_SPAWN_LOCATION
    :param game_board:
    :return:
    """
    game_board[ENEMY_SPAWN_LOCATION].available_item = 'Enemy'
    print('Dr Blackwood is searching for you. Be careful!\n')
