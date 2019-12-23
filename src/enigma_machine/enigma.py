from enigma_machine.conf.defaults import *
from enigma_machine.rotor import Rotor
from enigma_machine.reflector import Reflector
from enigma_machine.plugboard import Plugboard


ROTOR_DB = {
    "I": Rotor("I", ROTOR_I_WIRE_MAPPING, "Y"),
    "II": Rotor("II", ROTOR_II_WIRE_MAPPING, "M"),
    "III": Rotor("III", ROTOR_III_WIRE_MAPPING, "D"),
    "IV": Rotor("IV", ROTOR_IV_WIRE_MAPPING, "R"),
    "V": Rotor("V", ROTOR_V_WIRE_MAPPING, "H")
}


REFLECTOR_DB = {
    "UKW-A": Reflector("EJMZALYXVBWFCRQUONTSPIKHGD"),
    "UKW-B": Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT"),
    "UKW-C": Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
}


class Enigma:
    """ Implementation of the Enigma I

    The Enigma I which was the main machine used by the German Army (Wehrmacht)
    and Air Force (Luftwaffe). The Army and Naval machines were the only ones
    produced with the plugboard.

    """


    def __init__(self, rotor_order=["III", "II", "I"], reflector=REFLECTOR_DB["UKW-A"]):
        self.reflector = reflector
        self.configure_rotor_order(rotor_order)
        self.plugboard = Plugboard()


    @property
    def windows(self):
        return [ rotor.window for rotor in self.rotors ]


    @property
    def rotors(self):
        return self._rotors


    @rotors.setter
    def rotors(self, rotors):
        """
        """
        for rotor in rotors:
            assert rotor, f"Rotor {rotor} must {ROTOR_DB.keys()}"
        self._rotors = [ ROTOR_DB.get(rotor) for rotor in rotors ]


    def step(self):
        l_rotor, m_rotor, r_rotor = self.rotors

        # Step the rightmost rotor every step; Turnover mid rotor as req
        # Doublestep midrotor on r_rotor turnover and on mid rotor turnover
        if r_rotor.step() or m_rotor.window == m_rotor.turnover:
            if m_rotor.step():
                l_rotor.step()


    def configure_plugboard(self, plugs=None, replace=False):
        self.plugboard.configure_plugs(plugs, replace)


    def clear_plugboard(self):
        self.plugboard.clear_plugs()


    def configure_rotors(self, window_setting=["A", "A", "A"], ring_position=["A", "A", "A"]):
        for idx, setting in enumerate(zip(window_setting, ring_position)):
            self.rotors[idx].configure(setting[0], setting[1])


    def configure_rotor_order(self, rotor_order):
        self.rotors = rotor_order


    def encrypt_message(self, message):
        raise NotImplementedError


    def decrypt_message(self, message):
        self.encrypt_message(message)


    def encrypt_letter(self, letter):
        raise NotImplementedError


    def decrypt_letter(self, letter):
        self.encrypt_letter(letter)

