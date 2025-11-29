import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from base import Command
from infra.api_client import GenshinAPIClient
from chars_system import Character, Item

def get_api_commands(context):
    client = GenshinAPIClient()

    class ListCharacters(Command):
        def __init__(self, context):
            super().__init__("list_characters", "List characters from API", context)

        def execute(self, args):
            chars = client.get_characters()
            print(f"Characters found: {len(chars)}")
            for name in list(chars.keys())[:10]:
                print(" -", name)

    class ListWeapons(Command):
        def __init__(self, context):
            super().__init__("list_weapons", "List weapons from API", context)

        def execute(self, args):
            weapons = client.get_weapons()
            print(f"Weapons found: {len(weapons)}")
            for name in list(weapons.keys())[:10]:
                print(" -", name)

    class CreateFromAPI(Command):
        def __init__(self, context):
            super().__init__("create_from_api", "Create character from API", context)

        def execute(self, args):
            if not args:
                print("Usage: create_from_api <character_name>")
                return

            name = args[0].lower()
            data = client.get_character(name)

            if not data:
                print(f"Character '{name}' not found in API.")
                return

            char = Character(name)
            char.description = data.get("description", "No description")
            char.element = data.get("vision", "Unknown")
            char.weapon_type = data.get("weapon", "Unknown")
            char.rarity = data.get("rarity", "?")

            self.context.characters[name] = char
            print(f"✅ Created character '{name}' from API.")
            print(f"  Element: {char.element}")
            print(f"  Weapon: {char.weapon_type}")
            print(f"  Rarity: {char.rarity}")

    return [
        ListCharacters(context),
        ListWeapons(context),
        CreateFromAPI(context)
    ]
