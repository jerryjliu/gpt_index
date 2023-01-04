from abc import abstractmethod
from typing import Any, Iterable, List

from gpt_index.readers.base import BaseReader
from gpt_index.readers.schema.base import Document


class StringIterableReader(BaseReader):
    """String Iterable Reader

    Gets a list of documents, given an iterable (e.g. list) of strings

    Example:
        .. code-block:: python
            from gpt_index import StringIterableReader, GPTTreeIndex

            documents = StringIterableReader().load_data(texts=["I went to the store", "I bought an apple"]).load_data()
            index = GPTTreeIndex(documents)
            index.query("what did I buy?")

            # response should be something like "You bought an apple."
    """

    def load_data(self, **load_kwargs: Any) -> List[Document]:
        """
        Load the data
        """
        texts = load_kwargs.get("texts", list())
        results = []
        for text in texts:
            results.append(Document(text))

        return results