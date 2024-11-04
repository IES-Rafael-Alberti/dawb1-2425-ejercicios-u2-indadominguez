# test_ej23_06

import pytest
from unittest.mock import patch
from src.bucles.ej22_06 import triangulo_rectangulo  

def test_triangulo_rectangulo(capsys):
    altura = 5  
    triangulo_rectangulo(altura)
    captured = capsys.readouterr()

    expected_output = "\n".join("*" * i for i in range(1, altura + 1)) + "\n"
    assert captured.out == expected_output
