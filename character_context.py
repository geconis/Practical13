import json
from models.character import Character
import os

class CharacterContext:
    """
    Holds all characters and handles saving/loading to JSON
    """
    SAVE_FILE = "characters.json"

    def __init__(self):
        self.characters = {}
        self.load_characters()

    def add_character(self, character: Character):
        self.characters[character.name] = character
        self.save_characters()

    def save_characters(self):
        data = {}
        for name, char in self.characters.items():
            data[name] = {
                "strength": char.strength,
                "agility": char.agility,
                "intelligence": char.intelligence,
                "health": char.health
            }
        with open(self.SAVE_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def load_characters(self):
        if not os.path.exists(self.SAVE_FILE):
            return
        with open(self.SAVE_FILE, "r") as f:
            data = json.load(f)
        for name, stats in data.items():
            char = Character(
                name=name,
                strength=stats.get("strength", 10),
                agility=stats.get("agility", 10),
                intelligence=stats.get("intelligence", 10),
                health=stats.get("health", 100)
            )
            self.characters[name] = char
