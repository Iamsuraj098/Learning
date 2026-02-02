"""
Optional: Advanced LLM with better response generation
This is an enhanced version using open-source LLM for better quality responses
"""

from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch

class AdvancedLLMGenerator:
    """
    Use this for better quality responses.
    Models to try:
    - "gpt2" (small, fast)
    - "EleutherAI/gpt-neo-125M" (medium)
    - "EleutherAI/gpt-neo-2.7B" (large, requires more memory)
    - "stabilityai/stablelm-base-alpha-3b" (good balance)
    """
    
    def __init__(self, model_name="gpt2", device="cpu"):
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if device == "cuda" else torch.float32
        )
        self.model.to(device)
        self.generator = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            device=0 if device == "cuda" else -1
        )
    
    def generate(self, prompt, max_length=300, temperature=0.7):
        """Generate response"""
        output = self.generator(
            prompt,
            max_length=max_length,
            num_return_sequences=1,
            temperature=temperature,
            top_p=0.9,
            do_sample=True,
            repetition_penalty=1.2
        )
        return output[0]['generated_text']

# Usage in app.py:
# llm = AdvancedLLMGenerator("gpt2")
# response = llm.generate(prompt)

"""
Installation for advanced models:
pip install transformers torch

For GPU support:
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
"""
