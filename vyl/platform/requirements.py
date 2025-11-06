from vyl.utils.checkos import is_windows
from vyl.utils.crash import crash


def crash_if_cant_launch() -> None:
    if not is_windows():
        print("""
        Your OS does not seem to be Windows. 
        We only run on Windows, my apologies.
        """)
        crash()
