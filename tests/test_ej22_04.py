# test_ej22_04
 
import pytest
from src.bucles.ej22_04 import cuenta_atras 


def test_cuenta_atras_positivo(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "5")
    from src.bucles.ej22_04 import main
    main()  

    captured = capsys.readouterr()
    assert captured.out.strip() == "5, 4, 3, 2, 1, 0"


def test_cuenta_atras_negativo(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "-3")
    from src.bucles.ej22_04 import main
    main() 

    captured = capsys.readouterr()
    assert captured.out.strip() == "Por favor, ingresa un número entero positivo."


def test_cuenta_atras_cero(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "0")
    from src.bucles.ej22_04 import main
    main()  

    captured = capsys.readouterr()
    assert captured.out.strip() == "0"
