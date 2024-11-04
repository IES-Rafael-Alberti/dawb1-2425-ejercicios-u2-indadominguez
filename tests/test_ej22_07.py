# test_ej22_07

import pytest
from src.bucles.ej22_07 import tabla_multiplicar  

def test_tabla_multiplicar(capsys):
    tabla_multiplicar()
    captured = capsys.readouterr()
    expected_output = ""
    for i in range(1, 11):
        expected_output += f"Tabla de multiplicar del {i}:\n\n"
        for j in range(1, 11):
            expected_output += f"{i} x {j} = {i * j}\n\n"

    assert captured.out.strip() == expected_output.strip()



