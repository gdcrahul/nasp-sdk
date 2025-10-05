# nasp/llm_wrapper.py
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch

class LLMWrapper:
    def __init__(self, model_name="distilgpt2", device=None):
        """
        Improved wrapper:
         - default model: distilgpt2 (smaller but better than gpt2 for many cases)
         - uses max_new_tokens, sampling, repetition_penalty
         - strips the prompt from returned text so Agent only sees continuation
        """
        self.model_name = model_name

        # choose device: 0 = first GPU, -1 = CPU
        if device is None:
            self.device = 0 if torch.cuda.is_available() else -1
        else:
            self.device = device

        # load tokenizer + model
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, use_fast=True)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)

        # ensure pad token exists
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        self.generator = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            device=self.device,
            framework="pt"
        )

    def generate(self, prompt: str,
                 max_new_tokens: int = 80,
                 do_sample: bool = True,
                 temperature: float = 0.8,
                 top_p: float = 0.92,
                 top_k: int = 50,
                 repetition_penalty: float = 1.2) -> str:
        """
        Generate continuation text (returns only the generated continuation, not the full prompt).
        Tweak temperature/top_p/top_k/repetition_penalty to control verbosity and repetition.
        """
        try:
            outputs = self.generator(
                prompt,
                max_new_tokens=max_new_tokens,
                do_sample=do_sample,
                temperature=temperature,
                top_p=top_p,
                top_k=top_k,
                repetition_penalty=repetition_penalty,
                truncation=True,
                pad_token_id=self.tokenizer.eos_token_id,
                num_return_sequences=1
            )
            full = outputs[0]["generated_text"]
            # remove the original prompt if present (most pipelines return prompt + continuation)
            if full.startswith(prompt):
                continuation = full[len(prompt):].strip()
            else:
                # fallback: if not present, return full but trimmed
                continuation = full.strip()
            # apply a sensible cutoff to avoid insane repetition
            # if too long, truncate to first 500 characters
            if len(continuation) > 2000:
                continuation = continuation[:2000].rsplit(".", 1)[0] + "."
            return continuation
        except Exception as e:
            return f"⚠️ [LLM Error] {str(e)}"
