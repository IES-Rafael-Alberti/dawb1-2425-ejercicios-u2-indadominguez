# test_ej22_17

import pytest
from unittest.mock import patch
from src.bucles.ej22_17 import suma_digitos 

def test_suma_digitos():
    assert suma_digitos(123) == 6       
    assert suma_digitos(456) == 15      
    assert suma_digitos(0) == 0       
    assert suma_digitos(1001) == 2     
    assert suma_digitos(9876543210) == 45  

