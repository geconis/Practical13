from base import Command
from text_system import TextElement

class PwdCommand(Command):
    def __init__(self, context):
        super().__init__("pwd", "Show current path", context)

    def execute(self, args):
        print(self.context.pwd())

class PrintCommand(Command):
    def __init__(self, context):
        super().__init__("print", "Print element or whole doc", context)

    def execute(self, args):
        if "--whole" in args:
            print(self.context.print_elem(whole=True))
        else:
            print(self.context.print_elem())

class AddCommand(Command):
    def __init__(self, context):
        super().__init__("add", "Add new element", context)

    def execute(self, args):
        if len(args) < 2:
            print("Usage: add <container|leaf> <name>")
            return
        elem_type, name = args[0], args[1]
        new_elem = TextElement(name, parent=self.context.current)
        self.context.current.add_child(new_elem)
        if elem_type == "container":
            self.context.current = new_elem
        print(f"Added {elem_type} '{name}'")

class RmCommand(Command):
    def __init__(self, context):
        super().__init__("rm", "Remove element", context)

    def execute(self, args):
        if args:
            self.context.current.remove_child(args[0])
            print(f"Removed {args[0]}")
        else:
            if self.context.current.parent:
                name = self.context.current.name
                parent = self.context.current.parent
                parent.remove_child(name)
                self.context.current = parent
                print(f"Removed current element '{name}' and moved up")

class UpCommand(Command):
    def __init__(self, context):
        super().__init__("up", "Move to parent", context)

    def execute(self, args):
        if self.context.current.parent:
            self.context.current = self.context.current.parent
            print(f"Moved up to {self.context.current.name}")
        else:
            print("Already at root")

class CdCommand(Command):
    def __init__(self, context):
        super().__init__("cd", "Change directory", context)

    def execute(self, args):
        if not args:
            print("Usage: cd <name>")
            return
        name = args[0]
        found = next((c for c in self.context.current.children if c.name == name), None)
        if found:
            self.context.current = found
            print(f"Changed to {name}")
        else:
            print(f"No element '{name}'")

def get_text_commands(context):
    return [
        PwdCommand(context),
        PrintCommand(context),
        AddCommand(context),
        RmCommand(context),
        UpCommand(context),
        CdCommand(context)
    ]