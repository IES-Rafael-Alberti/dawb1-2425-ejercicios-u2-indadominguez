# test_ej21_05

import pytest
from src.condicionales.ej21_05 import debe_tributar

@pytest.mark.parametrize("edad, sueldo, resultado", [
    (17, 1000, True),  
    (18, 1500, True),  
    (20, 2000, True),  
    (16, 1000, False), 
    (15, 1200, False), 
    (17, 900, False),  
    (16, 800, False),  
    (0, 1000, False),  
    (0, 0, False)      
])
def test_debe_tributar(edad, sueldo, resultado):
    assert debe_tributar(edad, sueldo) == resultado
  



