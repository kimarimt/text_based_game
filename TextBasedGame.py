from helpers.constants import PLAYER_START
from helpers.builder import *
from helpers.util import *


def main():
    game_board = build_game_board()
    game_map = build_game_map()
    current_room: Tile = game_board[PLAYER_START]
    current_paths = current_room.paths
    inventory = []

    print_introduction()
    while True:
        clear()

        required_keys = [key in inventory for key in REQUIRED_KEYS]
        if not enemy_already_spawned(
                game_board) and required_keys.count(True) > 1:
            spawn_enemy(game_board)
        if can_defeat_enemy(inventory, current_room):
            print("You used the pistol to shoot Dr. Blackwood\n")
            current_room.clear_room()

        if did_player_win(inventory, current_room) or \
                did_player_lose(inventory, current_room):
            break

        if current_room.has_item(inventory):
            inventory.append(current_room.available_item)
            print(f'You grabbed the {current_room.available_item}\n')
            current_room.clear_room()

        render_map(game_map, current_room)
        inventory_str = ', '.join(inventory) if len(inventory) else 'Empty'
        print(f'\nInventory: {inventory_str}')
        current_room.show_info()

        next_path = input('\nChoose your move or type \'q\' to quit: ') \
            .lower()
        if next_path == 'q':
            break
        if len(next_path) != 1 or next_path not in current_paths:
            print('\nYou can\'t go this way!!')
            continue

        next_room: Tile = game_board[current_paths[next_path]]
        if next_room.is_not_accessible(inventory):
            print(
                f'\nDoor locked! You need the {
                    next_room.required_item} to unlock the door!')
            continue

        clear_player_token(game_map, current_room)
        current_room = next_room
        current_paths = current_room.paths

    clear(0)

    if did_player_win(inventory, current_room):
        print('You collected all the keys and escaped from mansion. Good job Agent Kent!')
    elif did_player_lose(inventory, current_room):
        print(
            'The didn\'t grab the secret item and Dr Blackwood has captured you! GAME OVER!')


if __name__ == '__main__':
    main()
