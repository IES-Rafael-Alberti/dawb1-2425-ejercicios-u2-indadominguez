# test_ej21_01

# tests/test_edad.py

from src.ej21_01 import verificar_edad, main
from unittest.mock import patch

def test_verificar_edad_mayor():
    assert verificar_edad(24) == "Eres mayor de 18 años"

def test_verificar_edad_menor():
    assert verificar_edad(14) == "No eres mayor de 18 años enano"

@patch("builtins.input", return_value="24")
@patch("builtins.print")
def test_main_mayor(mock_print, mock_input):
    main()
    mock_print.assert_called_once_with("Eres mayor de 18 años")

@patch("builtins.input", return_value="14")
@patch("builtins.print")
def test_main_menor(mock_print, mock_input):
    main()
    mock_print.assert_called_once_with("No eres mayor de 18 años enano")

