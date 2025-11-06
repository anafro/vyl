import os

from vyl.ai.solution import AISolution
from vyl.ai.task import AITask


def ai_chat() -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "chat.txt")

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def ai_chat_add(task_or_solution: AITask | AISolution) -> str:
    json = task_or_solution.to_json()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "chat.txt")

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(json)
        f.write("\n")

def ai_chat_flush():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "chat.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("")