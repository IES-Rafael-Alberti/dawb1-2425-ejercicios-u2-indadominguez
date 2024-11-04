# test_ej22_11

import pytest
from src.bucles.ej22_11 import palabra  


def test_palabra(capsys):
    test_input = "hola"
    palabra(test_input)
    captured = capsys.readouterr()
    expected_output = "\n".join(reversed(test_input)) + "\n"

    assert captured.out == expected_output

