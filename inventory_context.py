import json
import os

SAVE_FILE = "inventory_save.json"

class InventoryContext:
    """
    Holds the inventory for characters, with persistence
    """
    def __init__(self, character_context):
        self.character_context = character_context
        self.inventory = {}

        if os.path.exists(SAVE_FILE):
            self.load_state()

    def add_item(self, char_name, item_name):
        if char_name not in self.character_context.characters:
            print(f"No character named {char_name}")
            return
        if char_name not in self.inventory:
            self.inventory[char_name] = []
        self.inventory[char_name].append(item_name)
        print(f"Added {item_name} to {char_name}'s inventory.")
        self.save_state()

    def list_items(self, char_name):
        items = self.inventory.get(char_name, [])
        print(f"{char_name}'s inventory: {items}")

    def save_state(self):
        """
        Save inventory to JSON
        """
        with open(SAVE_FILE, "w") as f:
            json.dump(self.inventory, f, indent=2)

    def load_state(self):
        """
        Load inventory from JSON
        """
        with open(SAVE_FILE, "r") as f:
            self.inventory = json.load(f)
