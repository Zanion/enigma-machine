from collections import namedtuple
from enigma_machine.conf.defaults import ALPHABET


MAX_PLUGS = 13


class Plugboard:


    def __init__(self, plugs=None, alphabet=ALPHABET, max_plugs=MAX_PLUGS):
        self.alphabet = alphabet
        self.max_plugs = max_plugs
        self.configure_plugs(plugs, True)


    @property
    def alphabet(self):
        return self._alphabet


    @alphabet.setter
    def alphabet(self, alphabet):
        assert isinstance(alphabet, str), "Alphabet must be string"
        assert len(alphabet) > 0, "Alphabet must be non-zero length"

        self._alphabet = alphabet


    def clear_plugs(self):
        """ Convenience method to clear plugboard """
        self.configure_plugs(plugs=None, replace=True)


    def configure_plugs(self, plugs=None, replace=False):
        """
        """
        assert isinstance(plugs, list) or plugs is None, "Plugs must be list of replacements"
        assert isinstance(replace, bool), "Replace flag must be boolean"

        if replace:
            self.plugs = {}

        if not plugs:
            return

        for plug in plugs:
            self.add_plug(plug)


    def add_plug(self, plug=None):
        """
        """
        assert isinstance(plug, tuple) or plug is None, "Plug must be a tuple"

        if plug is None:
            return

        # Unpack plug tuple and validate
        letter1, letter2 = plug
        assert letter1 in self.alphabet, "Cannot add plugs to letters not in alphabet"
        assert letter2 in self.alphabet, "Cannot add plugs to letters not in alphabet"
        assert len(letter1) in self.alphabet, "Plugs must be between single letter character"
        assert len(letter2) in self.alphabet, "Plugs must be between single letter characters"

        # Assert length < 13
        assert len(self.plugs) < self.max_plugs, "Cannot add more than 13 plugs to plugboard"

        self.plugs[letter1] = letter2
        self.plugs[letter2] = letter1

