from consolemenu import *
from consolemenu.items import *

def read_measuring_data():
    pu = PromptUtils(Screen())
    result = pu.input("Vul bestandsnaam in")
    pu.println("\nBestandsnaam:", result.input_string, "\n")
    pu.enter_to_continue()


def main():
    menu = ConsoleMenu("Clean Air")
    menu.append_item(FunctionItem("Lees meetgegevens in", read_measuring_data))
    menu.show()

if __name__ == '__main__':
    main()
