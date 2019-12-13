from enigma_machine.conf.defaults import ALPHABET


class Rotor:


    def __init__(self, wheel_id, wiring, notch, turnover, window="A"):
        """

        Args:
            ...

        """
        self.wheel_id = wheel_id
        self.wiring = wiring.upper()
        self.notch = notch.upper()
        self.turnover = turnover.upper()
        self.window = window.upper()


    @property
    def window(self):
        return self._window


    @property.setter
    def window(self, window):
        self._window = window.upper()
        self.offset = ALPHABET.index(self.window)


    def step(self):
        """ Step the rotor position

        TODO

        """
        # Increment the offset and wrap around to 0 after Z(25)
        self.offset = (self.offset + 1) % 26
        self.window = ALPHABET[self.offset]





