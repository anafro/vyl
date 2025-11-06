from abc import ABC, abstractmethod

from vyl.ai.task import AITask
from vyl.ai.solution import AISolution
from rich.console import Console


class AI(ABC):
    def __init__(self, console: Console):
        self.console = console

    @abstractmethod
    def create_solution(self, prompt: AITask) -> AISolution:
        ...
