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


class arrPrinter(gdb.ValuePrinter):

    def __init__(self, val):
        self.__val = val

    def to_string(self):
        size = int(self.__val["size"])
        return f"arr_t(size={size})"

    def children(self):
        data_ptr = self.__val["v"]
        if data_ptr == 0:
            return

        size = int(self.__val["size"])
        for i in range(size):
            yield f"[{i}]", (data_ptr + i).dereference()

    def display_hint(self):
        return "array"


def build_pretty_printers():
    pp = gdb.printing.RegexpCollectionPrettyPrinter("custom_printers")
    pp.add_printer("foo_t", "^foo_t$", fooPrinter)
    pp.add_printer("bar_t", "^bar_t$", barPrinter)
    pp.add_printer("arr_t", "^arr_t$", arrPrinter)
    return pp
