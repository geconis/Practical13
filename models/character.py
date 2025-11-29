class Character:
    def __init__(self, name, strength, agility, intelligence, health=100, image_url=None):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.health = health
        self.image_url = image_url or "https://example.com/default.png"

    def get_stats(self):
        return {
            "Name": self.name,
            "Strength": self.strength,
            "Agility": self.agility,
            "Intelligence": self.intelligence,
            "Health": self.health,
            "Image URL": self.image_url
        }

    def __str__(self):
        stats = self.get_stats()
        return "\n".join(f"{k}: {v}" for k, v in stats.items())
