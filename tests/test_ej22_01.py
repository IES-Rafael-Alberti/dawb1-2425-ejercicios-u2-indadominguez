# test_ej22_01

import pytest
from src.bucles.ej22_01 import imprimir_palabra  

def test_imprimir_palabra(monkeypatch):
    palabra = "Hola"
    cantidad = 10
    salida_esperada = [palabra] * cantidad
    resultado = []

    monkeypatch.setattr("builtins.print", lambda x: resultado.append(x))
    imprimir_palabra(palabra, cantidad)

    assert resultado == salida_esperada


