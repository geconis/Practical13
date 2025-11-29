import sys
from cli.interpreter import CommandInterpreter
from context_factory import create_context_and_commands

def main():
    args = sys.argv[1:]
    mode = None

    if "--text" in args:
        mode = "text"
    elif "--chars" in args:
        mode = "chars"
    elif "--game" in args:
        mode = "game"   
    elif "--inventory" in args:
        mode = "inventory"
    else:
        choice = input("Choose mode (text/chars/game/inventory): ")
        mode = choice.strip().lower()

    context, commands = create_context_and_commands(mode)

    if not context:
        print("Unknown mode")
        return

    interpreter = CommandInterpreter(commands)
    interpreter.run()

if __name__ == "__main__":
    main()
