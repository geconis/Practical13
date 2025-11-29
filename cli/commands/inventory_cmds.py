from base import Command

class AddItemCommand(Command):
    """
    Add item to character inventory
    """
    def __init__(self, context):
        super().__init__("add_item", "Add item to character inventory", context)

    def execute(self, args):
        if len(args) < 2:
            print("Usage: add_item <char_name> <item_name>")
            return
        char_name, item_name = args[:2]
        self.context.add_item(char_name, item_name)

class ListInventoryCommand(Command):
    """
    List items of a character
    """
    def __init__(self, context):
        super().__init__("list_inventory", "List items of a character", context)

    def execute(self, args):
        if len(args) < 1:
            print("Usage: list_inventory <char_name>")
            return
        char_name = args[0]
        self.context.list_items(char_name)
