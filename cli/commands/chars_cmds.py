from base import Command
from chars_system import Character, Item, Ability, AttackAction, HealAction, AbilityAction


class CreateCommand(Command):
    def __init__(self, context):
        super().__init__("create", "Create char/item/ability", context)

    def execute(self, args):
        if not args:
            print("Usage: create <char|item|ability>")
            return

        t = args[0]
        name = input(f"Enter {t} name: ")

        if t == "char":
            self.context.characters[name] = Character(name)
        elif t == "item":
            self.context.items[name] = Item(name)
        elif t == "ability":
            self.context.abilities[name] = Ability(name)
        else:
            print("Unknown type")
            return

        print(f"Created {t} '{name}'")


class AddCommand(Command):
    def __init__(self, context):
        super().__init__("add", "Add item/ability to character", context)

    def execute(self, args):
        if "--char_id" not in args or "--id" not in args:
            print("Usage: add --char_id <char> --id <item|ability>")
            return

        char_name = args[args.index("--char_id") + 1]
        obj_name = args[args.index("--id") + 1]

        if char_name not in self.context.characters:
            print(f"No character {char_name}")
            return

        char = self.context.characters[char_name]

        if obj_name in self.context.items:
            char.items.append(self.context.items[obj_name])
            print(f"Added item {obj_name} to {char_name}")
        elif obj_name in self.context.abilities:
            char.abilities.append(self.context.abilities[obj_name])
            print(f"Added ability {obj_name} to {char_name}")
        else:
            print(f"No item/ability '{obj_name}'")


class ActCommand(Command):
    def __init__(self, context):
        super().__init__("act", "Perform action", context)

    def execute(self, args):
        if len(args) < 3:
            print("Usage: act <attack|heal|ability> <actor> <target>")
            return

        action_type, actor, target = args[:3]

        # Strategy selection
        strategy_map = {
            "attack": AttackAction(),
            "heal": HealAction(),
            "ability": AbilityAction()
        }

        strategy = strategy_map.get(action_type)

        if strategy:
            strategy.execute(actor, target)
        else:
            print(f"Unknown action '{action_type}'")


class LsCommand(Command):
    def __init__(self, context):
        super().__init__("ls", "List objects", context)

    def execute(self, args):
        if not args:
            print("Characters:", list(self.context.characters.keys()))
            print("Items:", list(self.context.items.keys()))
            print("Abilities:", list(self.context.abilities.keys()))
            return

        t = args[0]
        if t == "char":
            for c in self.context.characters.values():
                print(f"{c.name}: items={len(c.items)}, abilities={len(c.abilities)}")
        elif t == "item":
            print(list(self.context.items.keys()))
        elif t == "ability":
            print(list(self.context.abilities.keys()))
        else:
            print("Unknown type")


class ShowChar(Command):
    def __init__(self, context):
        super().__init__("show_char", "Show character info", context)

    def execute(self, args):
        if not args:
            print("Usage: show_char <name>")
            return

        name = args[0]
        char = self.context.characters.get(name)

        if not char:
            print(f"Character '{name}' not found.")
            return

        print("─" * 40)
        print(f"Name: {char.name}")
        print(f"Element: {getattr(char, 'element', 'Unknown')}")
        print(f"Weapon: {getattr(char, 'weapon_type', 'Unknown')}")
        print(f"Rarity: {getattr(char, 'rarity', '?')}")
        print(f"Description: {getattr(char, 'description', 'No description')}")
        print("─" * 40)

def get_chars_commands(context):

    return [
        CreateCommand(context),
        AddCommand(context),
        ActCommand(context),
        LsCommand(context),
        ShowChar(context)
    ]
