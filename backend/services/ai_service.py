import os 
import yaml
from groq import Groq
from typing import List , Dict

class AIService:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.prompts = self._load_prompts()

    def _load_prompts(self) -> dict :
        """" Load prompts from a YAML file."""
        import os
        from pathlib import Path
        config_path = Path(__file__).parent.parent / "config" / "prompts.yaml"
        with open(config_path, "r") as f:
            return yaml.safe_load(f)

    def get_system_prompt(self , mode: str ="default") ->str:
        """Get the system prompt based on the mode."""
        return self.prompts["system_prompts"].get(mode, self.prompts["system_prompts"]["default"])
    

    def generate_response(self, messages: List[Dict[str, str]], mode: str = "default") -> str:
        """ Generate AI response using OpenAI API
        
        Args:
        messages: List of {"role": "user/assistant" , "content":"..."}
        mode: Which system prompt to use
        
        Returns:
        AI response as string
        """
        system_prompt = self.get_system_prompt(mode)


        full_messages = [
            {"role": "system" , "content": system_prompt}

        ] + messages
        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages = full_messages,
            temperature=0.4,
            max_tokens=10000
        )
        return response.choices[0].message.content