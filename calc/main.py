from calc_factories import make_root, make_display,\
     make_label, make_buttons
from calc_class import Calculator

def main():
    root = make_root()
    display = make_display(root)
    label = make_label(root)
    buttons = make_buttons(root)
    calc = Calculator(root, label, display, buttons)
    calc.start()

if __name__ == '__main__':
    main()
