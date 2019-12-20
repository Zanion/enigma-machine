from collections import namedtuple
from enigma_machine.conf.defaults import ALPHABET
from enigma_machine.wire import Wire


class Rotor:


    def __init__(self, wheel_id, contact_mapping, notch, window="A", ring_setting="A", alphabet=ALPHABET):
        """ Initialize Rotor

        Args:
            wheel_id (str):  Identifier for the Rotor
            contact_mapping (str):   Index ordered mapping from alphabet onto
                                    inbound contacts
            notch (str):    Letter associated with position of notch on Rotor ring
            window (str):   Initial window position of Rotor
            ring_setting (str): Rotor ring setting
            alphabet (str): Alphabet used for Rotor


        """
        self.alphabet = alphabet
        self.wheel_id = wheel_id
        self.wiring = contact_mapping
        self.notch = notch
        self.configure(window, ring_setting)


    @property
    def alphabet(self):
        return self._alphabet


    @alphabet.setter
    def alphabet(self, alphabet):
        assert isinstance(alphabet, str), "Alphabet must be string"
        assert len(alphabet) > 0, "Alphabet must be non-zero length"

        self._alphabet = alphabet


    @property
    def notch(self):
        return self._notch


    @notch.setter
    def notch(self, notch_pos):
        """ Set the position of the notch on the ring

        Sets the letter position of the notch on the ring for the rotor. Also
        updates and records the turnover position (Letter visible in window)
        when notch is active and triggers the next rotor to step.

        Args:
            notch_pos (str): Letter position of the notch on the ring

        """
        assert (len(notch_pos) == 1), 'Notch position must be single digit'
        assert isinstance(notch_pos, str), 'Notch postion must be of type string'
        assert notch_pos in self.alphabet, 'Notch position must be member of alphabet'

        self._notch = notch_pos.upper()
        # Notch position is 8 letter positions advanced from turnover in window
        self.turnover = self.alphabet[(self.alphabet.index(self._notch) - 8) % len(self.alphabet)]


    @property
    def ring_setting(self):
        return self._ring_setting


    @ring_setting.setter
    def ring_setting(self, setting):
        assert (len(setting) == 1), 'Ring setting must be a single letter'
        assert isinstance(setting, str), 'Ring setting must be of type string'
        assert setting in self.alphabet, 'Ring setting must be member of alphabet'

        self._ring_setting = setting.upper()


    @property
    def window(self):
        return self._window


    @window.setter
    def window(self, window):
        assert (len(window) == 1), 'Window setting must be a single letter'
        assert isinstance(window, str), 'Window setting must be of type string'
        assert window in self.alphabet, 'Window setting must be member of alphabet'

        self._window = window.upper()
        # Offset the core wiring based on selected window position
        self.core_offset = (self.alphabet.index(self.window) - self.alphabet.index(self.ring_setting)) % len(self.alphabet)


    @property
    def wiring(self):
        # Return forward pass mapping by default
        return sorted(self._wiring, key=lambda x: x.r_contact)


    @wiring.setter
    def wiring(self, contact_mapping):
        """ Set the wiring from a string mapping of alphabet onto inbound contacts

        Iterates over the provided mapping of alphabet from the right contacts through
        the scrambled wiring onto the left contacts. Populates a wiring array with
        all Wire mappings such that they can be used to encode letters during
        forward or reverse passes on the rotor.

        All wires are established disregarding the ring setting (equivalent to
        assuming a default ring setting of A).

        Args:
            contact_mapping (string): String containing ordered mapping of contacts

        """
        assert (len(contact_mapping) == len(self.alphabet)), f"Argument must contain {len(self.alphabet)} letters"
        assert isinstance(contact_mapping, str), 'Argument must be of type string'

        self._wiring = []
        for idx in range(len(self.alphabet)):
            self._wiring.append(Wire(contact_mapping[idx], self.alphabet[idx]))


    def configure(self, window="A", ring_setting="A"):
        """ Configure the rotor ring or window setting

        Args:
            window (str): Window setting for the rotor
            ring_setting (str): Ring setting for the ring relative to wiring core

        """
        # Configure ring setting first
        self.ring_setting = ring_setting
        # Then set window position
        self.window = window


    def step(self):
        """ Step the rotor position

        Returns:
            (bool) True if window is on a the turnover letter position

        """
        # Increment the core_offset and wrap around to 0 after after final letter
        turned = self.window == self.turnover
        self.core_offset = (self.core_offset + 1) % len(self.alphabet)
        self.window = self.alphabet[self.core_offset]
        return turned


    def encode(self, letter, forward=True):
        """ Encode a letter passing through the rotor

        Args:
            letter (str): Letter to encode
            forward (bool): Encoding forward pass or reverse through the rotor

        Returns:
            (string) Letter associated with the output index encoded by the
                     rotor

        """
        assert len(letter) == 1, 'Letter must be a single letter'
        assert isinstance(letter, str), 'Letter must be of type str'
        assert isinstance(forward, bool), 'forward must be of type boolean'

        # Target wire for input letter shifted by positon of wiring core and
        # inverse wiring mapping if backward pass through rotor
        wiring_map = self.wiring if forward else sorted(self.wiring, key=lambda x: x.l_contact)
        wire = wiring_map[self.core_offset]
        # Get output letter from encoding on wiring core
        encoded_letter = self.alphabet.index(wire.l_contact if forward else wire.r_contact)
        # Get index of the output letter shifted by the position of the wiring core
        output_index = encoded_letter - self.core_offset % len(self.alphabet)
        # Return letter associated with the output index
        return self.alphabet[output_index]

