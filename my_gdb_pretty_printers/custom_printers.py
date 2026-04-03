import gdb.printing


class fooPrinter(gdb.ValuePrinter):
    """Print a foo object."""

    def __init__(self, val):
        self.__val = val

    def to_string(self):
        return "a={" + str(self.__val["a"]) + "} b={" + str(self.__val["b"]) + "}"


class barPrinter(gdb.ValuePrinter):
    """Print a bar object."""

    def __init__(self, val):
        self.__val = val

    def to_string(self):
        return "x={" + str(self.__val["x"]) + "} y={" + str(self.__val["y"]) + "}"


def build_pretty_printers():
    pp = gdb.printing.RegexpCollectionPrettyPrinter("custom_printers")
    pp.add_printer("foo", "^foo$", fooPrinter)
    pp.add_printer("bar", "^bar$", barPrinter)
    return pp
