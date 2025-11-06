import os

from vyl.ai.chatloader import ai_chat_add
from vyl.ai.providers.huggingface import HuggingFaceAI
from vyl.ai.task import AITask
from rich.console import Console
from rich.prompt import Confirm
from rich.style import Style, Color

ai_style = Style(italic=True, color=Color.parse('#444444'))
stdout_style = Style(color=Color.parse('#222244'))
code_style = Style(color=Color.parse('#222233'))
console = Console(style=ai_style)
ai = HuggingFaceAI(console)
path = os.getcwd()


def solve(prompt: str) -> None:
    task = AITask(prompt, path)
    solution = ai.create_solution(task)

    ai_chat_add(task)
    ai_chat_add(solution)

    console.print(solution.explanation, highlight=False, end='\n\n')

    if solution.has_code():
        console.print(solution.python_code, style=code_style, highlight=False)

        user_wants_to_apply = prompt.lower().endswith('now') or Confirm.ask(solution.application_question if solution.application_question else 'Run?', show_choices=False, default=False)

        if user_wants_to_apply:
            solution.evaluate()
            console.print(solution.get_std(), highlight=False, style=stdout_style)