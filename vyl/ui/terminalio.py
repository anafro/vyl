import sys

from ascii_colors import ASCIIColors

from vyl.ui.io import IO


class TerminalIO(IO):
    def __init__(self) -> None:
        pass

    def read(self, prompt: str = "", color: str = ASCIIColors.color_white) -> str:
        return input(f"{prompt}: ")

    def readbool(self, prompt: str = "") -> bool:
        answer = self.read(f"{prompt} <(y)es or (n)o>").lower()
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False
        else:
            return self.readbool(prompt)

    def write(self, message: str, color: str = ASCIIColors.color_white) -> None:
        ASCIIColors.print(message, color=color)

    def writeerr(self, error: str, color: str = ASCIIColors.color_red) -> None:
        ASCIIColors.print(error, color)

    def get_prompt(self) -> str:
        return ' '.join(sys.argv[1:])
