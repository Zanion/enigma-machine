import pytest
from enigma_machine.rotor import Rotor
from enigma_machine.conf.defaults import ALPHABET_LENGTH, ROTOR_I_WIRE_MAPPING


@pytest.fixture
def rotor():
    return Rotor("I", ROTOR_I_WIRE_MAPPING, "Y")


def test_rotor_notch_setting(rotor):
    assert rotor.notch == "Y"
    assert rotor.turnover == "Q"


def test_rotor_wiring(rotor):
    assert len(rotor.wiring) == ALPHABET_LENGTH
    assert ''.join([ wire.l_contact for wire in rotor.get_wiring() ]) == ROTOR_I_WIRE_MAPPING
    inverse_wiring = "UWYGADFPVZBECKMTHXSLRINQOJ"
    assert ''.join([ wire.r_contact for wire in rotor.get_wiring(forward=False) ]) == inverse_wiring


def test_encode_default_ring_setting(rotor):
    letter = "A"
    expected = "E"

    actual = rotor.encode(letter)
    assert actual == expected


def test_encode_offset_window(rotor):
    letter = "A"
    expected = "J"

    rotor.configure(window="B")
    actual = rotor.encode(letter)
    assert actual == expected


def test_encode_B_ring_setting(rotor):
    letter = "A"
    expected = "K"
    rotor.configure(window="A", ring_setting="B")
    actual = rotor.encode(letter)
    assert actual == expected


def test_encode_F_ring_setting(rotor):
    letter = "A"
    expected = "W"
    rotor.configure(window="Y", ring_setting="F")
    actual = rotor.encode(letter)
    assert actual == expected


