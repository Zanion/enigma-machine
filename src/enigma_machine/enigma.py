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


    def __init__(self, used_wheels=["III", "II", "I"], window_pos=['A', 'A', 'A']):

        assert len(used_wheels) == len(window_pos), "Count of used wheels and window selections must be equal"

        self.wheels = [ ROTOR_III, ROTOR_II, ROTOR_I ]


    @property
    def windows(self):
        return [ rotor.window for rotor in self.wheels ]


    def step(self):
        l_wheel, m_wheel, r_wheel = self.wheels

        # Step the rightmost rotor every step; Turnover mid rotor as req
        # Doublestep midrotor on r_wheel turnover and on mid wheel turnover
        if r_wheel.step() or m_wheel.window == m_wheel.turnover:
            if m_wheel.step():
                l_wheel.step()


    def configure_plugboard(self):
        raise NotImplementedError


    def configure_rotors(self, window_setting=["A", "A", "A"], ring_position=["A", "A", "A"]):
        for idx, setting in enumerate(zip(window_setting, ring_position)):
            self.wheels[idx].configure(setting[0], setting[1])


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

