# test_ej22_03

import pytest
from src.bucles.ej22_03 import impar, mostrar_impares  

def test_impar():
    assert impar(1) is True
    assert impar(2) is False

def test_mostrar_impares(monkeypatch):
    numero = 7
    salida_esperada = "1, 3, 5, 7\n"
    resultado = []


    monkeypatch.setattr("builtins.print", lambda x, end="\n": resultado.append(f"{x}{end}"))
    mostrar_impares(numero)
    assert ''.join(resultado).strip() == salida_esperada.strip()

def test_main_positive_input(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "3")
    from  src.bucles.ej22_03 import main
    main()
    assert capsys.readouterr().out == "1, 3\n"

def test_main_non_positive_input(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "-1")
    from src.bucles.ej22_03 import main
    main()
    assert capsys.readouterr().out == "Introduce un número entero positivo por favor.\n"
