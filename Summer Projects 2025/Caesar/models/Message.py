import string
from abc import ABC , abstractmethod

class Message(ABC):
    """ A secret text that you want to encode or decode

    The point is to generate an encoded version of the original text via letter-offsetting
    --------------------------------------------------------------------------------------
    Attributes:
    ----------
    - message : str
    the original text

    Methods:
    -------
    - cyphering -> str
    applies an offset on the message turning it almost unreadable without knowing the value of the offset,
    returns a new text.

    - uncyphering -> str
    applies a series of offset on the encoded message trying to revert it back to the original.

    """
    alphabet_dict = {i: chr(96 + i) for i in range(1, 27)}
    reversed_alphabet_dict= {v: k for k, v in alphabet_dict.items()}


    def __init__(self,message: str):
        self.message = message
    @abstractmethod
    def cyphering(self,offset: int) -> str:
        pass
    @abstractmethod
    def uncyphering(self) -> str:
        pass