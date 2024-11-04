# test_ej22_02

import pytest
from src.bucles.ej22_02 import mostrar_años_cumplidos

def test_mostrar_años_cumplidos(monkeypatch):
    edad = 7
    salida_esperada = [1, 2, 3, 4, 5, 6, 7]  
    resultado = []

    monkeypatch.setattr("builtins.print", lambda x: resultado.append(x))
    mostrar_años_cumplidos(edad)

    assert resultado == salida_esperada
