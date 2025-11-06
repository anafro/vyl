from abc import ABC, abstractmethod

from ascii_colors import ASCIIColors


class IO(ABC):
    @abstractmethod
    def __init__(self) -> None:
        ...

    @abstractmethod
    def read(self, prompt: str = "", color: str = ASCIIColors.color_white) -> str:
        ...

    @abstractmethod
    def readbool(self, prompt: str = "") -> bool:
        ...

    @abstractmethod
    def write(self, message: str, color: str = ASCIIColors.color_white) -> None:
        ...

    @abstractmethod
    def writeerr(self, error: str, color: str = ASCIIColors.color_red) -> None:
        ...

    @abstractmethod
    def get_prompt(self) -> str:
        ...