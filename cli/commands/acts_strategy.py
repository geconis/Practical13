class AttackAction:
    """
    Strategy Pattern: Attack action
    """
    def execute(self, actor, target, context):
        damage = actor.strength
        target.take_damage(damage)
        context.log_action(f"{actor.name} attacks {target.name} for {damage} damage. {target.name} HP: {target.health}/{target.max_health}")


class HealAction:
    """
    Strategy Pattern: Heal action
    """
    def execute(self, actor, target, context):
        heal_amount = actor.intelligence
        target.heal(heal_amount)
        context.log_action(f"{actor.name} heals {target.name} for {heal_amount}. {target.name} HP: {target.health}/{target.max_health}")


class AbilityAction:
    """
    Strategy Pattern: Ability action (example: uses agility)
    """
    def execute(self, actor, target, context):
        damage = actor.agility
        target.take_damage(damage)
        context.log_action(f"{actor.name} uses special ability on {target.name} for {damage} damage. {target.name} HP: {target.health}/{target.max_health}")
