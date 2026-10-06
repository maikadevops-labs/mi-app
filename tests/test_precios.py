from app.precios import total_con_iva


def test_total_con_iva():
    assert total_con_iva(100) == 121.0


def test_iva_personalizado():
    assert total_con_iva(100, iva=0.105) == 110.5
