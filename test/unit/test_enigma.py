import pytest
from enigma_machine.enigma import Enigma, REFLECTOR_DB


@pytest.fixture
def enigma():
    return Enigma()


def test_rotor_step(enigma):
    enigma.configure_rotors(["K", "D", "O"])
    enigma.step()
    assert enigma.windows == ["K", "D", "P"]
    enigma.step()
    assert enigma.windows == ["K", "D", "Q"]


def test_rotor_doublestep(enigma):
    enigma.configure_rotors(["K", "D", "Q"])
    enigma.step()
    assert enigma.windows == ["K", "E", "R"]
    enigma.step()
    assert enigma.windows == ["L", "F", "S"]
    enigma.step()
    assert enigma.windows == ["L", "F", "T"]
    enigma.step()
    assert enigma.windows == ["L", "F", "U"]


def test_encrypt_letter():
    enigma = Enigma(rotor_order=["III", "II", "I"], reflector=REFLECTOR_DB["UKW-B"])
    enigma.configure_rotors(["M", "E", "U"])
    assert enigma.encrypt_letter("A") == "G"


def test_encrypt_message():
    enigma = Enigma(rotor_order=["III", "II", "I"], reflector=REFLECTOR_DB["UKW-B"])
    enigma.configure_rotors(["M", "E", "U"])
    assert enigma.encrypt_message("AAAAA") == "GDXTZ"
