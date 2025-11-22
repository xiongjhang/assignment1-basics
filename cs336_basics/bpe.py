from typing import Iterable
import multiprocessing

# TODO:implement BPE tokenizer training
def train_bpe(
        input_path: str,
        vocab_size: int,
        special_tokens: list[str] | None = None,
) -> tuple[dict[int, bytes], list[tuple[bytes, bytes]]]:
    
    vocab = ...
    merges = ...
    return vocab, merges

# TODO: implement BPE tokenizer class
class BPETokenizer:

    def __init__(
        self,
        vocab: dict[int, bytes],
        merges: list[tuple[bytes, bytes]],
        special_tokens: list[str] | None = None,
    ):
        pass
    
    @classmethod
    def from_files(
        cls,
        vocab_filepath: str,
        merges_filepath: str,
        special_tokens: list[str] | None = None,
    ):
        pass

    def encode(
        self, 
        text: str
    ) -> list[int]:
        pass

    def encode_iterable(
        self, 
        iterable: Iterable[str]
    ) -> Iterable[int]:
        pass

    def decode(
        self, 
        ids: list[int]
    ) -> str:
        pass

if __name__ == "__main__":

    # TODO: BPE training on TinyStories dataset
    pass

    # TODO: BPE training on OpenWebText dataset
    pass
