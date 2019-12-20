import pytest
from enigma_machine.rotor import Rotor
from enigma_machine.conf.defaults import ALPHABET, ROTOR_I_WIRE_MAPPING


@pytest.fixture
def rotor():
    return Rotor("I", ROTOR_I_WIRE_MAPPING, "Y")


def test_rotor_notch_setting(rotor):
    assert rotor.notch == "Y"
    assert rotor.turnover == "Q"


def test_rotor_wiring(rotor):
    assert len(rotor.wiring) == len(ALPHABET)
    assert ''.join([ wire.l_contact for wire in rotor.wiring ]) == ROTOR_I_WIRE_MAPPING


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


def test_stepping_rotor(rotor):
    assert rotor.step() == False, 'Turnover expected to be false for window setting A'
    assert rotor.core_offset == 1
    assert rotor.window == "B"


def test_stepping_rotor_notched(rotor):
    rotor.configure(window="Q")
    assert rotor.step() == True, 'Turnover expected to be on Q for notch at Y'
    assert rotor.core_offset == 17
    assert rotor.window == "R"
