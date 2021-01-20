from Calculator import Calculator


class CalcInterface:
    def __init__(self):
        self.calc = Calculator()

    def add(self, a, b):
        return self.calc.add(a, b)

    def clean(self):
        print("CLEAN CALCULATOR")
        del self.calc
