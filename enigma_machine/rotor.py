from collections import namedtuple
from enigma_machine.conf.defaults import ALPHABET

Wire = namedtuple("Wire", "contact_in contact_out")


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
        self.window = window.upper()
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

        Returns a sorted list of wires based on direction of encoding based on
        index mapping from ALPHABET onto the rotor wiring.

        Args:
            forward (bool): Direction of encoding (Default: True)

        Returns:
            Sorted list of wires indexed by mapping to ALPHABET

        """
        if forward:
            return sorted(self._wiring, key=lambda x: x.contact_in)
        return sorted(self._wiring, key=lambda x: x.contact_out)


    @property.setter
    def wiring(self, contact_mapping):
        """ Set the wiring from a string mapping of ALPHABET onto inbound contacts

        Iterates over the inbound contact_mapping of ALPHABET onto the inbound
        contacts on the rotor wiring. Populates a wiring array with all contacts
        such that they can be encoded during forward or reversed passes on the
        rotor.

        Args:
            contact_mapping (string): String containing ordered mapping of contacts

        """
        assert (len(contact_mapping) == 26), 'Argument must contain 26 letters'
        assert isinstance(contact_mapping, str), 'Argument must be of type string'

        self._wiring = []
        for idx in range(len(ALPHABET)):
            self._wiring.append(Wire(ALPHABET[idx], contact_mapping[idx]))


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
        return wire.contact_out if forward else wire.contact_in
