import sys

from iris.command import Command


class ExitCommand(Command):
    name = 'exit'
    description = 'Exit IRIS OSINT Framework'
    aliases = 'q', 'quit'

    @Command.execute
    def run(self):
        sys.exit(0)
