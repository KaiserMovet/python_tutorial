

class CalculatorZeroException(Exception):
    pass


class Calculator:

    HISTORY_FILE = "xd.log"

    # Constructor
    def __init__(self, name="SuperCalc"):
        print("CALCURATOR INIT")
        self.name = name
        self.history = []

    def add(self, a, b):
        self._save_log("ADD", a, b)
        return a + b

    def sub(self, a, b):
        self._save_log("SUB", a, b)
        return a - b

    def mul(self, a, b):
        self._save_log("MUL", a, b)
        return a * b

    def div_floor(self, a, b):
        self._save_log("DIV_FLOOR", a, b)
        if b == 0:
            raise CalculatorZeroException("Do not divide by zero")
        return a // b

    def div(self, a, b):
        self._save_log("DIV", a, b)
        if b == 0:
            raise CalculatorZeroException("Do not divide by zero")
        return a / b

    def pow(self, a, b):
        self._save_log("DIV", a, b)
        # Should be a ** b
        return a * b

    @classmethod
    def _save_log(cls, operation, a, b):
        log_line = F"{operation}({a}, {b})"
        with open(cls.HISTORY_FILE, 'a+') as f:
            f.write(log_line + "\n")

    # Used in print()
    def __repr__(self):
        return F"<Calculator: {self.name}>"

    def __del__(self):
        print("CALCURATOR DEL")
