from nwk.actor import _Player
from nwk.scene import _Scene
from termcolor import colored, cprint


class Console(object):
    def __init__(self, starting_location=None):
        self._action = None
        self._location = starting_location is not None and starting_location or "town"
        try:
            self.main()
        except KeyboardInterrupt:
            exit("Quit")

    def main(self):
        while True:
            s = _Scene(location_name=self._location)
            p = _Player()
            p._locale = self._location
            print(s.get_text())
            while True:
                try:
                    input_text = colored(
                        ">> What do you want to do? ", "grey", attrs=["bold"]
                    )
                    self._action = _parse(input(input_text))
                    if not self._action:
                        raise KeyboardInterrupt
                except KeyboardInterrupt:
                    continue
                # ACTION: go
                if "go" in self._action:
                    direction = self._action["go"]
                    if direction in (
                        "east",
                        "north",
                        "northeast",
                        "northwest",
                        "south",
                        "southeast",
                        "southwest",
                        "west",
                    ):
                        exits = s.get_exits()
                        if direction in exits:
                            location = exits[direction]
                            self._location = location.lower()
                            print("You head {}...".format(direction))
                            break
                        else:
                            _e("ERR: You can't go '{}'!".format(direction))
                    else:
                        _e("ERR: Invalid direction '{}'!".format(direction))
                # ACTION: quit
                if "help" in self._action:
                    print("commands:\n")
                    print(
                        "\t- 'go [direction]' i.e: 'go south' - Sends your character in the specified direction."
                    )
                    print("\t- 'help' - This text. Gives you explanation of commands.")
                    print("\t- 'quit' - Closes the application.")
                    print()
                if "quit" in self._action:
                    raise KeyboardInterrupt


def _e(string):
    cprint("\t{}".format(string), "red", attrs=["bold"])


def _parse(command):
    if command.startswith("go", 0):
        command = command.split(" ", 1)
        return {command[0]: command[1]}
    elif command.startswith("help", 0):
        return {"help": ""}
    elif command.startswith("quit", 0):
        return {"quit": ""}
    else:
        _e(f"ERR: You cannot '{command}'!")
        return False
