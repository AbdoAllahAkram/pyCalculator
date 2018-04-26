num_1, num_2, result = 0, 0, 0

## Start get_input function
def get_input():
    return float(input("Enter a number: "))
## End get_input function

## Start print_result function
def print_result(result):
    print("result = " + str(result))
## End print_result function



while True:
    print("options")
    print("write 'add' to add tow numbers")
    print("write 'subtract' to subtract tow numbers")
    print("write 'multiply' to multiply tow numbers")
    print("write 'divide' to Divide tow numbers")
    print("write 'quit' to Quit the program")

    user_input = str(input(": "))

    if user_input == "quit":
        break
    elif user_input == "add":
        num_1 = get_input()
        num_2 = get_input()
        result = num_1 + num_2
        print_result(result)

        if input("to continue or quit press [y/n] : ") == "y":
            continue
        else:
            break
    elif user_input == "subtract":
        num_1 = get_input()
        num_2 = get_input()
        result = num_1 - num_2
        print_result(result)

        if input("to continue or quit press [y/n] : ") == "y":
            continue
        else:
            break
    elif user_input == "multiply":
        num_1 = get_input()
        num_2 = get_input()
        result = num_1 * num_2
        print_result(result)

        if input("to continue or quit press [y/n] : ") == "y":
            continue
        else:
            break

    elif user_input == "divide":
        num_1 = get_input()
        num_2 = get_input()

        if num_1 == 0 or num_2 == 0:
            print("can't Divide Zero")
            break
        else:
            result = num_1 / num_2
            print_result(result)

            if input("to continue or quit press [y/n] : ") == "y":
                continue
            else:
                break

    else:
        print("Unknown Input")
        continue
