import os
from typing import Optional
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import snapshot_download

from vyl.ai.chatloader import ai_chat
from vyl.ai.memoryloader import ai_memory
from vyl.ai.solution import AISolution
from vyl.ai.task import AITask
from vyl.ai.provider import AI
from vyl.ai.concepts.conceptloader import ai_concepts
from transformers import logging
from rich.console import Console


class HuggingFaceAI(AI):
    def __init__(
        self,
        console: Console,
        model_name: str = "Qwen/Qwen2.5-Coder-1.5B-Instruct",
        device: Optional[str] = None
    ):

        super().__init__(console)
        logging.set_verbosity_error()
        self.console = console
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.local_dir = f"./models/{model_name}"
        self._download_model(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.local_dir,
            trust_remote_code=True,
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            self.local_dir,
            device_map={"": "cuda:0"},
            offload_folder="offload",
            trust_remote_code=True,
        )
        self.memory = ai_memory()
        self.chat = ai_chat()

    def _download_model(self, model_name: str) -> None:
        if not os.path.exists(self.local_dir) or not os.listdir(self.local_dir):
            os.makedirs(self.local_dir, exist_ok=True)
            snapshot_download(repo_id=model_name, local_dir=self.local_dir, resume_download=True)

    def create_solution(self, task: AITask) -> AISolution:
        chat_template = [
            {"role": "system", "content": ai_concepts()},
            {"role": "user", "content": f'''
                <task>
                    <prompt>{task.prompt}</prompt>
                    <path>{task.path}</path>
                    <memory>{self.memory}</memory>
                    <chat-history>{self.chat}</chat-history>
                </task>
            '''}
        ]
        input_ids = self.tokenizer.apply_chat_template(chat_template, return_tensors="pt", add_generation_prompt=True).to(self.device)
        output_tokens = self.model.generate(input_ids=input_ids, max_new_tokens=800)
        response_text = self.tokenizer.decode(output_tokens[0][input_ids.shape[-1]:], skip_special_tokens=True)
        response_text = response_text.strip()
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]
        response_text = response_text.strip()

        return AISolution.from_json(self.console, response_text)
