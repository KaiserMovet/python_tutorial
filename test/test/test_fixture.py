

def test_fixture(calc_interface):
    res = calc_interface.add(6, 5)
    assert res == 0
