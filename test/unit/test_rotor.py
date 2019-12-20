import pytest
from enigma_machine.rotor import Rotor


def test_rotor_notch_setting():
    rotor = Rotor("I", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Y")
    assert rotor.notch == "Y"
    assert rotor.turnover == "Q"


def test_rotor_wiring():
    wiring_0 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotor = Rotor("I", wiring_0, "Y")
    assert len(rotor.wiring) == 26
    assert ''.join([ wire.l_contact for wire in rotor.get_wiring() ]) == wiring_0
    inverse_wiring = "UWYGADFPVZBECKMTHXSLRINQOJ"
    assert ''.join([ wire.r_contact for wire in rotor.get_wiring(forward=False) ]) == inverse_wiring


def test_encode_default_ring_setting():
    letter = "A"
    wiring_0 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotor = Rotor("I", wiring_0, "Y")

    out = rotor.encode(letter)
    assert out == "E"


def test_encode_offset_window():
    letter = "A"
    wiring_0 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotor = Rotor("I", wiring_0, "Y")
    rotor.configure(window="B")

    out = rotor.encode(letter)
    assert out == "J"


def test_encode_B_ring_setting():
    letter = "A"
    wiring_0 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotor = Rotor("I", wiring_0, "Y")
    rotor.configure(window="A", ring_setting="B")

    out = rotor.encode(letter)
    assert out == "K"


def test_encode_F_ring_setting():
    letter = "A"
    wiring_0 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotor = Rotor("I", wiring_0, "Y")
    rotor.configure(window="Y", ring_setting="F")

    out = rotor.encode(letter)
    assert out == "W"


