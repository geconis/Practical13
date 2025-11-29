# Observer Pattern: allows subscribing to changes in the context
class CharsContext:
    def __init__(self):
        self.characters = {}
        self.items = {}
        self.abilities = {}
        self.subscribers = []

    def subscribe(self, func):
        self.subscribers.append(func)

    def notify(self, event, obj):
        for sub in self.subscribers:
            sub(event, obj)


class Character:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.abilities = []

# Strategy Pattern: encapsulates character actions
class ActionStrategy:
    def execute(self, actor, target):
        raise NotImplementedError

class AttackAction(ActionStrategy):
    def execute(self, actor, target):
        print(f"{actor} attacks {target}")

class HealAction(ActionStrategy):
    def execute(self, actor, target):
        print(f"{actor} heals {target}")

class AbilityAction(ActionStrategy):
    def execute(self, actor, target):
        print(f"{actor} uses ability on {target}")

class Item:
    def __init__(self, name):
        self.name = name

class Ability:
    def __init__(self, name):
        self.name = name
