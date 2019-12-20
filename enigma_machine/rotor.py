from collections import namedtuple
from enigma_machine.conf.defaults import ALPHABET


Wire = namedtuple("Wire", "l_contact r_contact")


class Rotor:


    def __init__(self, wheel_id, contact_mapping, notch, window="A", ring_setting="A"):
        """

        Args:
            ...

        """
        self.wheel_id = wheel_id
        self.wiring = contact_mapping
        self.notch = notch
        self.configure(window, ring_setting)


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
        self._notch = notch_pos.upper()
        # Notch position is 8 letter positions advanced from turnover in window
        self.turnover = ALPHABET[(ALPHABET.index(self._notch) - 8) % 26]


    @property
    def ring_setting(self):
        return self._ring_setting


    @ring_setting.setter
    def ring_setting(self, setting):
        assert (len(setting) == 1), 'Ring setting must be a single letter'
        assert isinstance(setting, str), 'Ring setting must be of type string'
        self._ring_setting = setting.upper()


    @property
    def window(self):
        return self._window


    @window.setter
    def window(self, window):
        self._window = window.upper()
        self.core_offset = (ALPHABET.index(self.window) - ALPHABET.index(self.ring_setting)) % 26


    def get_wiring(self, forward=True):
        """ Get sorted list of wire contacts based on direction of encoding

        Returns a sorted list of wires based on direction of encoding mapped
        from ALPHABET onto the rotor wiring.

        Args:
            forward (bool): Direction of encoding (Default: True)

        Returns:
            Sorted list of wires indexed by mapping to ALPHABET

        """
        assert isinstance(forward, bool), 'forward must be of type boolean'
        return sorted(self._wiring, key=lambda x: x.r_contact if forward else x.l_contact)


    @property
    def wiring(self):
        return self._wiring


    @wiring.setter
    def wiring(self, contact_mapping):
        """ Set the wiring from a string mapping of ALPHABET onto inbound contacts

        Iterates over the provided mapping of ALPHABET from the right contacts through
        the scrambled wiring onto the left contacts. Populates a wiring array with
        all Wire mappings such that they can be used to encode letters during
        forward or reverse passes on the rotor.

        All wires are established disregarding the ring setting (equivalent to
        assuming a default ring setting of A).

        Args:
            contact_mapping (string): String containing ordered mapping of contacts

        """
        assert (len(contact_mapping) == 26), 'Argument must contain 26 letters'
        assert isinstance(contact_mapping, str), 'Argument must be of type string'

        self._wiring = []
        for idx in range(len(ALPHABET)):
            self._wiring.append(Wire(contact_mapping[idx], ALPHABET[idx]))


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
            (bool) True if window is on a notched letter

        """
        # Increment the core_offset and wrap around to 0 after Z(25)
        self.core_offset = (self.core_offset + 1) % 26
        self.window = ALPHABET[self.core_offset]
        return self.window==self.notch


    def encode(self, letter, forward=True):
        """ Encode a letter passing through the rotor

        Args:
            letter (str): Letter to encode
            forward (bool): Encoding forward pass or reverse through the rotor

        Returns:
            (string) Letter encoded by the rotor wiring

        """
        wiring = self.get_wiring(forward)
        print(wiring)
        # Encryption shifted by ring_seting positon
        print(f"CoreOffset: {self.core_offset}")
        wire = wiring[self.core_offset]
        print(wire)
        letter = ALPHABET[ALPHABET.index(wire.l_contact if forward else wire.r_contact) - self.core_offset % 26]
        return letter
