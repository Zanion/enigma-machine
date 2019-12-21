import pytest
from enigma_machine.enigma import Enigma


@pytest.fixture
def enigma():
    return Enigma()


def test_rotor_doublestep(enigma):
    enigma.configure_rotors(["K", "D", "O"])
    enigma.step()
    assert enigma.windows == ["K", "D", "P"]
    enigma.step()
    assert enigma.windows == ["K", "D", "Q"]
    enigma.step()
    assert enigma.windows == ["K", "E", "R"]
    enigma.step()
    assert enigma.windows == ["L", "F", "S"]
    enigma.step()
    assert enigma.windows == ["L", "F", "T"]
    enigma.step()
    assert enigma.windows == ["L", "F", "U"]


