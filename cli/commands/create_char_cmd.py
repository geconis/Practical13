from base import Command
from models.character import Character

class CreateCharacterCommand(Command):
    """
    Command to create a new character through CLI prompts
    """
    def __init__(self, context):
        super().__init__("create_char", "Create a new character", context)

    def execute(self, args):
        name = input("Enter character name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return

        if name in self.context.characters:
            print(f"Character '{name}' already exists.")
            return

        try:
            strength = int(input("Enter Strength (1-100): "))
            agility = int(input("Enter Agility (1-100): "))
            intelligence = int(input("Enter Intelligence (1-100): "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            return

        image_url = input("Enter image URL (or leave empty for default): ").strip()
        if not image_url:
            image_url = None

        new_char = Character(name, strength, agility, intelligence, image_url=image_url)
        
        if hasattr(self.context, "add_character"):
            self.context.add_character(new_char)
        else:
            self.context.characters[name] = new_char

        print(f"✅ Character '{name}' created successfully!")
