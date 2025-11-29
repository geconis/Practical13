class GameCharacter:
    """
    Represents a character in the game with battle stats and actions
    """
    def __init__(self, character):
        self.name = character.name
        self.strength = character.strength
        self.agility = character.agility
        self.intelligence = character.intelligence
        self.health = character.health
        self.max_health = character.health
        self.image_url = getattr(character, "image_url", None)
    
    def is_alive(self):
        return self.health > 0

    def take_damage(self, amount):
        self.health = max(self.health - amount, 0)

    def heal(self, amount):
        self.health = min(self.health + amount, self.max_health)

    def __str__(self):
        return f"{self.name} | HP: {self.health}/{self.max_health} | STR: {self.strength} | AGI: {self.agility} | INT: {self.intelligence}"
