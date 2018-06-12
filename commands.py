

class MacroCommand:

    def __init__(self, commands):
        self.commands = list(commands)

    def __call__(self):
        for c in self.commands:
            c()
