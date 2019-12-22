from enigma_machine.conf.defaults import ALPHABET
from enigma_machine.rotor import Wire


class Reflector:


    def __init__(self, contact_mapping="", alphabet=ALPHABET):
        self.alphabet = alphabet
        self.wiring = contact_mapping


    @property
    def alphabet(self):
        return self._alphabet


    @alphabet.setter
    def alphabet(self, alphabet):
        assert isinstance(alphabet, str), "Alphabet must be string"
        assert len(alphabet) > 0, "Alphabet must be non-zero length"

        self._alphabet = alphabet


    @property
    def wiring(self):
        return self._wiring


    @wiring.setter
    def wiring(self, contact_mapping):
        """
        """
        assert isinstance(contact_mapping, str), "Contact mapping must be str"
        assert len(contact_mapping) == len(self.alphabet), "Contact mapping must be same length as alphabet"

        # Store sequence directly and use index as mapping to alphabet
        self._wiring = contact_mapping


    def encode(self, letter):
        """
        """
        assert len(letter) == 1, 'Letter must be a single letter'
        assert isinstance(letter, str), 'Letter must be of type str'
        assert letter in self.alphabet, 'Letter must be member of alphabet'

        # Access output wiring by index offset from alphabet
        return self.wiring[self.alphabet.index(letter)]

