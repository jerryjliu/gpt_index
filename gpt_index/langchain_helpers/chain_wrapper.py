"""Wrapper functions around an LLM chain."""

from typing import Any, Optional, Tuple

from langchain import LLMChain, OpenAI
from langchain.llms.base import LLM

from gpt_index.prompts.base import Prompt
from gpt_index.utils import globals_helper


class LLMPredictor:
    """LLM predictor class."""

    def __init__(self, llm: Optional[LLM] = None) -> None:
        """Initialize params."""
        self._llm = llm or OpenAI(temperature=0, model_name="text-davinci-002")
        self.total_tokens_used = 0

    def predict(self, prompt: Prompt, **prompt_args: Any) -> Tuple[str, str]:
        """Predict the answer to a query."""
        llm_chain = LLMChain(prompt=prompt, llm=self._llm)

        formatted_prompt = prompt.format(**prompt_args)
        full_prompt_args = prompt.get_full_format_args(prompt_args)
        llm_prediction = llm_chain.predict(**full_prompt_args)

        self.total_tokens_used += self._count_tokens(
            formatted_prompt
        ) + self._count_tokens(llm_prediction)
        return llm_prediction, formatted_prompt

    def _count_tokens(self, text: str) -> int:
        tokens = globals_helper.tokenizer(text)
        return len(tokens["input_ids"])
