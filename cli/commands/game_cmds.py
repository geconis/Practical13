from base import Command
from game_context import GameContext
from cli.commands.acts_strategy import AttackAction, HealAction, AbilityAction

class SelectCharacterCommand(Command):
    """
    Select a character from available characters for the game
    """
    def __init__(self, context: GameContext):
        super().__init__("select_char", "Select character for game", context)

    def execute(self, args):
        if not args:
            print("Usage: select_char <character_name>")
            return
        name = args[0]
        self.context.select_character(name)


class StartGameCommand(Command):
    """
    Start the main game loop
    """
    def __init__(self, context: GameContext):
        super().__init__("start_game", "Start the game loop", context)

    def execute(self, args):
        if not self.context.selected_characters:
            print("No characters selected. Use select_char first.")
            return

        print("🎮 Game started!")
        print("Selected characters:")
        self.context.list_selected()
        print("Use 'act <action> <actor> <target>' to perform actions.")


class ActCommand(Command):
    """
    Perform an action (attack, heal, ability) in the game
    """
    def __init__(self, context: GameContext):
        super().__init__("act", "Perform action in game", context)

    def execute(self, args):
        if len(args) < 3:
            print("Usage: act <attack|heal|ability> <actor> <target>")
            return

        action_type, actor_name, target_name = args[:3]

        actor = self.context.selected_characters.get(actor_name)
        target = self.context.selected_characters.get(target_name)

        if not actor:
            print(f"Actor '{actor_name}' not selected.")
            return
        if not target:
            print(f"Target '{target_name}' not selected.")
            return

        strategy_map = {
            "attack": AttackAction(),
            "heal": HealAction(),
            "ability": AbilityAction()
        }

        strategy = strategy_map.get(action_type)
        if strategy:
            strategy.execute(actor, target, self.context)
        else:
            print(f"Unknown action '{action_type}'")
