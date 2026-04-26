from calculadora import soma, subtrai, multiplica, divide, quadrado

def test_soma(): assert soma(2, 2) == 4
def test_subtrai(): assert subtrai(5, 2) == 3
def test_multiplica(): assert multiplica(3, 3) == 9
def test_divide(): assert divide(10, 2) == 5
def test_quadrado(): assert quadrado(4) == 16
