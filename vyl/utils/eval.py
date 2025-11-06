import io
import sys


def evaluate(python_code: str) -> str:
    buffer = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = buffer

    exec(python_code)

    sys.stdout = old_stdout
    return buffer.getvalue()
