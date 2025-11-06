import json


class AITask:
    def __init__(
            self,
            prompt: str,
            path: str,
    ) -> None:
        self.prompt = prompt
        self.path = path.replace("\\", "/")

    def to_json(self) -> str:
        return json.dumps(self.__dict__)