import json
import os
from models.game_character import GameCharacter

SAVE_FILE = "game_save.json"

class GameContext:
    """
    Holds the state of the current game
    """
    def __init__(self, available_characters):
        self.available_characters = available_characters
        self.selected_characters = {}
        self.game_log = []

        if os.path.exists(SAVE_FILE):
            self.load_state()

    def select_character(self, name):
        if name not in self.available_characters:
            print(f"Character '{name}' not found.")
            return None

        if name in self.selected_characters:
            print(f"Character '{name}' already selected.")
            return self.selected_characters[name]

        game_char = GameCharacter(self.available_characters[name])

        if hasattr(self, "saved_characters") and name in self.saved_characters:
            game_char.health = self.saved_characters[name].get("health", game_char.health)

        self.selected_characters[name] = game_char
        print(f"Selected {name} for the game!")
        self.save_state()
        return game_char

    def list_selected(self):
        if not self.selected_characters:
            print("No characters selected.")
            return
        for char in self.selected_characters.values():
            print(char)

    def log_action(self, action_desc):
        self.game_log.append(action_desc)
        print(action_desc)
        self.save_state()

    def save_state(self):
        """
        Save selected characters' HP and game log
        """
        data = {
            "characters": {
                name: {"health": char.health} for name, char in self.selected_characters.items()
            },
            "game_log": self.game_log
        }
        with open(SAVE_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def load_state(self):
        """
        Load saved game state
        """
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
        self.saved_characters = data.get("characters", {})
        self.game_log = data.get("game_log", [])
