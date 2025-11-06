import os


def ai_memory() -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "memory.txt")

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def ai_memorize(flashback: str) -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "memory.txt")

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(flashback)
        f.write("\n")