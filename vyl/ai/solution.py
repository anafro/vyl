import json
from typing import Optional

from vyl.utils.eval import evaluate

from rich.console import Console


class AISolution:
    def __init__(
            self,
            console: Console,
            explanation: str,
            python_code: Optional[str] = None,
            application_question: Optional[str] = None,
            process_message: Optional[str] = None,
            completion_message: Optional[str] = None,
            can_apply_silently: bool = False,
            **kwargs
    ) -> None:
        self.console = console
        self.python_code = python_code
        self.explanation = explanation
        self.can_apply_silently = can_apply_silently
        self.application_question = application_question
        self.process_message = process_message
        self.completion_message = completion_message
        self.std_output = '<no code ran>'

    @classmethod
    def from_json(cls, console: Console, json_string: str) -> "AISolution":
        try:
            data = json.loads(json_string)
            key_map = {
                "pythonCode": "python_code",
                "applicationQuestion": "application_question",
                "processMessage": "process_message",
                "completionMessage": "completion_message",
            }

            for old, new in key_map.items():
                if old in data:
                    data[new] = data.pop(old)

            return AISolution(console=console, **data)
        except json.decoder.JSONDecodeError:
            print('The AI made a non-JSON response:')
            print(json_string)
            raise

    def evaluate(self):
        self.std_output = evaluate(self.python_code)

    def has_code(self) -> bool:
        return self.python_code is not None and len(self.python_code.strip()) != 0

    def to_json(self):
        return json.dumps({
            "explanation": self.explanation,
            "pythonCode": self.python_code,
            "stdOutput": self.std_output,
        })

    def get_std(self):
        return self.std_output if self.has_code() else ''
