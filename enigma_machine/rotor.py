from collections import namedtuple
from enigma_machine.conf.defaults import ALPHABET


Wire = namedtuple("Wire", "l_contact r_contact")


class Rotor:


    def __init__(self, wheel_id, contact_mapping, notch, turnover, window="A", ring_setting="A"):
        """

        Args:
            ...

        """
        self.wheel_id = wheel_id
        self.wiring = contact_mapping
        self.notch = notch.upper()
        self.turnover = turnover.upper()
        self.window = window
        self.ring_setting = ring_setting


    @property
    def ring_setting(self):
        return self._ring_setting


    @property.setter
    def ring_setting(self, setting):
        assert (len(setting) == 1), 'Ring setting must be a single letter'
        assert instanceof(setting, str), 'Ring setting must be of type string'
        self._ring_setting = setting.upper()


    @property
    def window(self):
        return self._window


    @property.setter
    def window(self, window):
        self._window = window.upper()
        self.offset = ALPHABET.index(self.window)


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


    @property.setter
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


    def step(self):
        """ Step the rotor position

        Returns:
            (bool) True if window is on a notched letter

        """
        # Increment the offset and wrap around to 0 after Z(25)
        self.offset = (self.offset + 1) % 26
        self.window = ALPHABET[self.offset]
        return self.window==self.notch


    def encode(self, letter, forward=True):
        """ Encode a letter passing through the rotor

        Args:
            letter (str): Letter to encode
            forward (bool): Encoding forward pass or reverse through the rotor

        Returns:
            (string) Letter encoded by the rotor wiring

        """
        wire = self.get_wiring(forward)[(self.ring_setting + self.offset) % 26]
        return wire.l_contact if forward else wire.r_contact
