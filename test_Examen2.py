from Examen2 import MiClase  

objeto = MiClase(530128, 120, 24, ["Ignorantes", "NADIE SABE", "Rata De Dos Patas"], [0.8, 0.6, 0.7,])

def test_ObtieneValencia():
    assert objeto.ObtieneValencia(objeto.Valencia) == 3

def test_DivisibleTempo():
    assert objeto.DivisibleTempo(objeto.Tempo) == [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120]

def test_ObtieneMasBailable():
    assert objeto.ObtieneMasBailable(objeto.listaBailabilidad) == 0.8

def test_VerificaListaCanciones():
    assert objeto.VerificaListaCanciones(objeto.listaCanciones) == True
######################################################################################################

######################################################################################################


objeto2 = MiClase(1234567, 2, 1254673, ["Odiame", "Pa mi", "Talvez"], [0.8, 0.9, 0.7])

def test2_ObtieneValencia():
    assert objeto2.ObtieneValencia(objeto2.Valencia) == 4

def test2_DivisibleTempo():
    assert objeto2.DivisibleTempo(objeto2.Tempo) == [1, 2]

def test2_ObtieneMasBailable():
    assert objeto2.ObtieneMasBailable(objeto2.listaBailabilidad) == 0.9

def test2_VerificaListaCanciones():
    assert objeto2.VerificaListaCanciones(objeto2.listaCanciones) == True

