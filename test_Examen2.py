from Examen2 import MiClase  

objeto = MiClase(5350128, 120, 24, ["Ignorantes", "NADIE SABE", "Rata De Dos Patas"], [0.8, 0.6, 0.7,])

def test_ObtieneValencia():
    assert objeto.ObtieneValencia(objeto.Valencia) == 4

def test_DivisibleTempo():
    assert objeto.DivisibleTempo(objeto.Tempo) == [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120]

def test_ObtieneMasBailable():
    assert objeto.ObtieneMasBailable(objeto.listaBailabilidad) == 0.8

def test_VerificaListaCanciones():
    assert objeto.VerificaListaCanciones(objeto.listaCanciones) == True
