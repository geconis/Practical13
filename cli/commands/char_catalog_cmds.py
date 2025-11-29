from base import Command

class ListCharactersCommand(Command):
    """
    Command to list all characters in the catalog.
    """
    def __init__(self, context):
        super().__init__("list_chars", "List all characters", context)

    def execute(self, args):
        if not self.context.characters:
            print("No characters available.")
            return
        for name, char in self.context.characters.items():
            print(f"- {name}")

class ShowCharacterStatsCommand(Command):
    """
    Command to show full stats of a character
    """
    def __init__(self, context):
        super().__init__("show_stats", "Show stats for a character", context)

    def execute(self, args):
        if not args:
            print("Usage: show_stats <character_name>")
            return
        name = args[0]
        char = self.context.characters.get(name)
        if not char:
            print(f"Character '{name}' not found.")
            return
        print(char)  # Character.__str__() буде показувати stats
