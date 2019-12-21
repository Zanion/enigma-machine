from collections import namedtuple
from enigma_machine.defaults import ALPHABET


class PlugBoard:


    def __init__(self, plugs={}, alphabet=ALPHABET):
        self.plugs = plugs
        self.alphabet = alphabet


    @property
    def alphabet(self):
        return self._alphabet


    @alphabet.setter
    def alphabet(self, alphabet):
        assert isinstance(alphabet, str), "Alphabet must be string"
        assert len(alphabet) > 0, "Alphabet must be non-zero length"

        self._alphabet = alphabet


    def add_plug(letter1, letter2):
        assert letter1 in self.alphabet
        self.plugs[letter1] = letter2
        self.plugs[letter2] = letter1

