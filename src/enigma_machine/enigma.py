from enigma_machine.rotor import Rotor
from enigma_machine.conf.defaults import *


ROTOR_I = Rotor("I", ROTOR_I_WIRE_MAPPING, "Y")
ROTOR_II = Rotor("II", ROTOR_II_WIRE_MAPPING, "M")
ROTOR_III = Rotor("III", ROTOR_III_WIRE_MAPPING, "D")
ROTOR_IV = Rotor("IV", ROTOR_IV_WIRE_MAPPING, "R")
ROTOR_V = Rotor("V", ROTOR_V_WIRE_MAPPING, "H")


class Enigma:
    """ Implementation of the Enigma I

    The Enigma I which was the main machine used by the German Army (Wehrmacht)
    and Air Force (Luftwaffe). The Army and Naval machines were the only ones
    produced with the plugboard.

    """


    def __init__(self, used_wheels=["I", "II", "III"], window_pos=['A', 'A', 'A']):

        assert len(used_wheels) == len(window_pos), "Count of used wheels and window selections must be equal"

        self.wheels = [ ROTOR_I, ROTOR_II, ROTOR_III ]


    def step(self):
        raise NotImplementedError


    def configure_plugboard(self):
        raise NotImplementedError


    def configure_rotor(self, rotor, window_setting="A", ring_position="A"):
        raise NotImplementedError


    def configure_rotor_order(self, rotor_order):
        raise NotImplementedError


    def encrypt_message(self, message):
        raise NotImplementedError


    def decrypt_message(self, message):
        self.encrypt_message(message)


    def encrypt_letter(self, letter):
        raise NotImplementedError


    def decrypt_letter(self, letter):
        self.encrypt_letter(letter)

