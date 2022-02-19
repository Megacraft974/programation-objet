from fractions import Fraction


class BaseOperation:
    pass


class Number(BaseOperation):
    def __init__(self, val, ):
        assert type(val) in (int, float, Fraction), "'" + str(val) + "' must be of type int"
        self.value = Fraction(val)

    def __str__(self):
        return str(self.value)

    def get(self):
        return self.value

    def __add__(self, val):
        self.value += val
        return self

    def __mul__(self, val):
        self.value *= val
        return self


class Unknown(BaseOperation):
    def __init__(self, name):
        self.name = name
        self.value = None

    def __str__(self):
        return self.name

    def get(self):
        if self.value is None:
            return self.name
        else:
            return self.value


class Equality(BaseOperation):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.left) + " = " + str(self.right)

    def get(self):
        left = self.left.get()
        right = self.right.get()
        if type(left) is int and type(right) is int:
            return self.left.get() == self.right.get()
        else:
            return str(self)

    def get_unknowns(self):
        return self.left.get_unknowns() | self.right.get_unknowns()

    def solve(self):
        unknowns = self.get_unknowns()
        print(unknowns)
        if len(unknowns) == 1:
            # Solvable
            isolate, left_isolated = self.left.inverted()  # Operation to isolate the unknown on the left side and the unknown part of the left side

            tmp_right = self.right.copy()
            cancel, right_canceled = tmp_right.inverted()
            tmp_right.add(cancel)  # Operation to cancel everything except the unknown on the right side
            tmp_right.reduce()
            print(isolate, tmp_right, cancel)

            self.left.add(isolate)
            self.right.add(isolate)
            self.left.reduce()
            self.right.reduce()
            return self.get()
        else:
            return


class Operator(BaseOperation):
    def __init__(self, operation, *terms):
        if operation == "+":
            self.operation = lambda out, val: out + val
            self.invert = lambda e: -e
            self.null = 0
        elif operation == "*":
            self.operation = lambda out, val: out * val
            self.invert = lambda e: Fraction(1, e)
            self.null = 1
        else:
            raise TypeError(str(operation) + " is not a valid operator.")
        self.symbol = operation
        self.terms = terms

    def __str__(self):
        def format_sub(e):
            if isinstance(e, Operator):
                return "(" + str(e) + ")"
            else:
                return str(e)
        return (" " + self.symbol + " ").join(map(format_sub, self.terms))

    def get(self):
        self.reduce()
        if len(self.terms) == 1:
            return self.terms[0].get()
        else:
            return str(self)

    def add(self, term):
        print(term, isinstance(term, BaseOperation), isinstance(term, Operator))
        if isinstance(term, BaseOperation):
            self.terms.append(term)
        else:
            self.terms.append(Number(term))

    def copy(self):
        return Operator(self.symbol, *self.terms)

    def reduce(self):
        values = {}
        tmp = []
        for term in self.terms:
            val = term.get()
            if type(val) in (int, float, Fraction):
                if type(val) in values:
                    values[type(val)] = self.operation(values[type(val)], val)
                else:
                    values[type(val)] = val
            else:
                tmp.append(term)
        tmp.extend([Number(v) for v in values.values()])
        self.terms = tmp

    def inverted(self):
        self.reduce()
        out = []
        unknown = []
        for term in self.terms:
            if isinstance(term, Unknown):
                unknown.append(term)
            else:
                if isinstance(term, Operator):
                    # TODO - ONLY works with a single unknown
                    isolated, unknown_left = term.inverted()
                    # assert len(unknown_left.terms) == 0
                    out = list(isolated.terms) + [Operator(self.symbol, *out)]
                else:
                    val = term.get()
                    out.append(Number(self.invert(val)))

        return Operator(self.symbol, *out), Operator(self.symbol, *unknown)

    def get_unknowns(self):
        out = set()
        for term in self.terms:
            if isinstance(term, Operator):
                out.update(term.get_unknowns())
            elif isinstance(term, Unknown):
                out.add(term.name)
        return out


class Addition(Operator):
    def __init__(self, *terms):
        super().__init__("+", *terms)


class Product(Operator):
    def __init__(self, *terms):
        super().__init__("*", *terms)


if __name__ == "__main__":
    op = Equality(
        Product(
            Number(5),
            Number(6),
            Unknown("x")
        ),
        Addition(
            Number(4),
            Number(7),
            Number(12),
            Product(
                Number(3),
                Number(4),
            Unknown("x")
            )
        )
    )
    print("Base:", op)
    print("Reduced:", op.get())
    print("Solved:", op.solve())