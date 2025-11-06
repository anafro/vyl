from vyl.utils.checkos import is_windows
from vyl.utils.crash import crash

from rich.console import Console


def crash_if_cant_launch(console: Console) -> None:
    if not is_windows():
        console.print("""
        Your OS does not seem to be Windows. 
        We only run on Windows, our apologies.
        """)
        crash()
