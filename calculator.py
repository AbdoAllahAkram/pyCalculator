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

    ### Quit Prgoram
    if user_input == "quit":
        break
    ### Add
    elif user_input == "add":
        num_1 = get_input()
        num_2 = get_input()
        result = num_1 + num_2
        print_result(result)

        if input("to continue or quit press [y/n] : ") == "y":
            continue
        else:
            break

    ### Subtraction
    elif user_input == "subtract":
        num_1 = get_input()
        num_2 = get_input()
        result = num_1 - num_2
        print_result(result)

        if input("to continue or quit press [y/n] : ") == "y":
            continue
        else:
            break
    ### Multiplication
    elif user_input == "multiply":
        num_1 = get_input()
        num_2 = get_input()
        result = num_1 * num_2
        print_result(result)

        if input("to continue or quit press [y/n] : ") == "y":
            continue
        else:
            break

    ### Divition
    elif user_input == "divide":
        try:
            num_1 = get_input()
            num_2 = get_input()

            result = num_1 / num_2
            print_result(result)
        except ZeroDivisionError:
            print("Ann Error Occurred")
            print("due to zero division")
            continue

        if input("to continue or quit press [y/n] : ") == "y":
            continue
        else:
            break

    else:
        print("Unknown Input")
        continue
