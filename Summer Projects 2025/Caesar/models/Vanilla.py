
from models.Message import Message

import pandas as pd


class Vanilla(Message):
    """Simplest Implementation of Message class

    Heritate her attributes and methods for her mother (class Message)

    Simplest way of encoding/ decoding message ( only right (positive) offset) and
    the same offset for the entire document to encode
    """

    def __init__(self,message:str):
        super().__init__(message)


    def cyphering(self,offset: int) -> str:
        """ only right offsetting (positive value)

        :param offset: the count of letter on the right
        :return: the message encoded
        """
        encoded_text=[]
        for i in self.message.lower():
            if i.isalpha():
                index = Message.reversed_alphabet_dict[i]
                offseted_index = ((index + offset - 1) % 26) + 1
                encoded_text.append(Message.alphabet_dict[offseted_index])
            else:
                encoded_text.append(i)
        return ''.join(encoded_text)


    def matching_real_english(self, possibilities: list[str]) -> str:
        english_words = {'hello', 'world', 'the', 'and', 'to', 'a', 'of', 'is', 'in', 'that'}
        return max(possibilities, key=lambda phrase: sum(word in english_words for word in phrase.split()))


    def uncyphering(self,message) -> str:
            """
            Try all 26 possible Caesar decryptions and return them as a list.
            """
            possibilities = []

            for offset in range(1, 27):
                decoded_text = []

                for i in message.lower():
                    if i.isalpha():
                        index = Message.reversed_alphabet_dict[i]
                        offseted_index = ((index - offset - 1) % 26) + 1
                        decoded_text.append(Message.alphabet_dict[offseted_index])
                    else:
                        decoded_text.append(i)
                possibilities.append(''.join(decoded_text))
            return self.matching_real_english(possibilities)

