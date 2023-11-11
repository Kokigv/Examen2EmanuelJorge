from Encuentra_Examen2 import MiClase

objeto = MiClase(5350128, 120, 24, ["Ignorantes", "NADIE SABE", "Rata De Dos Patas"], [0.8, 0.6, 0.7,])


def test_Encuentra():
    assert objeto.Encuentra([1,2,23,4],4) == True