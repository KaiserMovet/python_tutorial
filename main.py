from Calculator import Calculator, CalculatorZeroException
from pprint import pprint


def data_structures():

    print("Dictionary")
    dict_obj = {1: 10, 3: 30}
    dict_obj[5]: "xd"
    for key, item in dict_obj.items():
        print(key, item)

    print("List")
    list_obj = [1, 4, 2, 3, 4]
    list_obj.append("xd")
    for val in list_obj:
        print(val)

    print("List with iterator")
    list_obj = [10, 40, 20, 30, 40]
    list_obj.append("xd")
    for i, val in enumerate(list_obj):
        print(i, val)

    print("Tuple")
    tuple_obj = (1, 4, 2, 3, 4)
    # Cannot add new elements
    for val in tuple_obj:
        print(val)

    print("Set")
    # Unique elements
    set_obj = set([1, 4, 2, 3, 4])
    set_obj.add(1)
    for val in set_obj:
        print(val)

    print("=" * 10)

    if 5 in set_obj:
        print(F"{5} is in set")
    print("SET: ")
    pprint(set_obj)
    breakpoint()


def calc():

    calc_obj = Calculator()
    a = 2
    b = 0

    print(calc_obj)

    for a, b in zip([1, 2, 3], [4, 5, 6]):
        print("=" * 10)
        print("a", a)
        print("b", b)
        print('add', calc_obj.add(a, b))
        print('sub', calc_obj.sub(a, b))
        print('mul', calc_obj.mul(a, b))
        try:
            print('div_floor', calc_obj.div_floor(a, b))
            print('div', calc_obj.div(a, b))
        except CalculatorZeroException as ex:
            print(ex)
            break
        print('power', calc_obj.pow(a, b))
    else:
        print("No break")
    i = 5
    while(i):
        i -= 1
        print(i)
        break
    else:
        print("No break")


def main():
    print("*" * 10)
    data_structures()
    print("*" * 10)
    # calc()
    print("*" * 10)


if __name__ == "__main__":
    main()
