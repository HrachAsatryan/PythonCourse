import problem21
def test_answer():
    assert problem21.balCalc(1000, 0.12, 0.2) == 77.43
    assert problem21.balCalc(50000, 0.24, 0.01) == 56207.52
    assert problem21.balCalcRec(1000, 0.12, 0.2) == 77.43
    assert problem21.balCalcRec(50000, 0.24, 0.01) == 56207.52
