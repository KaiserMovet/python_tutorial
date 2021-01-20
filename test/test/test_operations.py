from Calculator import Calculator


def test_add():
    calc_obj = Calculator("Test")
    error_list = []
    test_numbers_list = [(1, 2, 5), (4, 5, 5)]
    for test_numbers in test_numbers_list:
        a, b, c = test_numbers
        res = calc_obj.add(a, b)
        if res != c:
            error_list.append(F"ADD {a}+{b}={res} instead of {c}")

    assert not error_list, "\n" + "\n".join(error_list)


def test_power():
    calc_obj = Calculator("Test")
    error_list = []
    test_numbers_list = [(1, 2, 1), (2, 4, 16)]
    for test_numbers in test_numbers_list:
        a, b, c = test_numbers
        res = calc_obj.pow(a, b)
        if res != c:
            error_list.append(F"Power {a}**{b}={res} instead of {c}")

    assert not error_list, "\n" + "\n".join(error_list)
