class Command:
    def __init__(self, name, description="", context=None):
        self.name = name
        self.description = description
        self.context = context

    def execute(self, args):
        raise NotImplementedError
