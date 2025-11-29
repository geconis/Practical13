class CommandInterpreter:
    def __init__(self, commands):
        self.commands = {cmd.name: cmd for cmd in commands}

    def run(self):
        print("Available commands:", ", ".join(self.commands.keys()))
        print("Type 'exit' to quit.\n")
        while True:
            try:
                line = input("> ").strip()
                if not line:
                    continue
                if line in ("exit", "quit"):
                    break

                parts = line.split()
                cmd_name, args = parts[0], parts[1:]

                if cmd_name in self.commands:
                    self.commands[cmd_name].execute(args)
                else:
                    print(f"Unknown command: {cmd_name}")

            except KeyboardInterrupt:
                print("\nExiting...")
                break
