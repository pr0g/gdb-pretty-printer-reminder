import gdb.printing
import custom_printers

gdb.printing.register_pretty_printer(
    gdb.current_objfile(), custom_printers.build_pretty_printer()
)
