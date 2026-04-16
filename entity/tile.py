from dataclasses import dataclass


@dataclass
class Tile:
    """
    A class to represent a room tile in the game.

    Attributes:
        name (str): The name of the room.
        paths (dict[str, str]): The available paths that the player can take.
        center (tuple[int, int]): Represents the center coordinate of the room.
        Used to place the player token on the game map.
        required_item (str | None): The item needed to enter a room; defaults to None if the room is free to access.
        available_item (str | None): The item needed to progress through the game; defaults to None if the room is empty.
    """
    name: str
    paths: dict[str, str]
    center: tuple[int, int]
    required_item: str | None
    available_item: str | None

    directions = {
        'w': 'North',
        's': 'South',
        'a': 'West',
        'd': 'East',
    }

    def show_info(self):
        """
        Displays the room's name and possible paths out to the console.
        """
        print(f'Current Room: {self.name}')
        print(f'\nPaths')
        for i, letter in enumerate(self.paths.keys()):
            print(f'{i + 1}: Go {self.directions[letter]} ({letter})')

    def is_not_accessible(self, inventory):
        """
        Checks if the room is accessible based on if the room's required_item is in the player's
        inventory.
        :param inventory: The player's inventory
        :type inventory: list[str]
        :return: Whether the room is accessible or not.
        :rtype: bool
        """
        return self.required_item is not None and self.required_item not in inventory

    def has_item(self, inventory):
        """
        Checks if the room has an item and if it's in the player inventory.
        :param inventory: The player's inventory
        :type inventory: list[str]
        :return: Whether the room has an item and if it's in the player's inventory.
        :rtype: bool
        """
        return self.available_item is not None and self.available_item not in inventory

    def clear_room(self):
        """
        Set's the room available_item to None
        """
        self.available_item = None
