import os


def ai_concepts() -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "VYL_CONCEPTS.sysprompt.md")

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
