from cli.interpreter import CommandInterpreter


class DummyCommand:
    def __init__(self):
        self.name = "ping"
        self.called = False

    def execute(self, args):
        self.called = True


def test_interpreter_executes_command(monkeypatch):
    dummy = DummyCommand()
    interpreter = CommandInterpreter([dummy])

    # Імітуємо користувацьке введення
    inputs = iter(["ping", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    interpreter.run()
    assert dummy.called
