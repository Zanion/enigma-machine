from enigma_machine.rotor import Rotor


class Enigma:
    """ Implementation of the Enigma I

    The Enigma I which was the main machine used by the German Army (Wehrmacht)
    and Air Force (Luftwaffe). The Army and Naval machines were the only ones
    produced with the plugboard.

    """


    def __init__(self, used_wheels=["I", "II", "III"], window_pos=['A', 'A', 'A']):

        assert(len(used_wheels) == len(window_pos))
