import consolemenu
from consolemenu.items import FunctionItem


def read_measuring_data():
    pu = consolemenu.PromptUtils(consolemenu.Screen())
    result = pu.input("Vul bestandsnaam in")
    pu.println("\nBestandsnaam:", result.input_string, "\n")
    pu.enter_to_continue()


def main():
    menu = consolemenu.ConsoleMenu("Clean Air")
    menu.append_item(FunctionItem("Lees meetgegevens in", read_measuring_data))
    menu.show()


if __name__ == '__main__':
    main()
