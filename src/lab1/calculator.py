def plus(num_1, num_2):
    """Addition"""
    return f"Result: {num_1 + num_2}"


def minus(num_1, num_2):
    """Subtraction"""
    return f"Result: {num_1 - num_2}"


def multiply(num_1, num_2):
    """Multiplication"""
    return f"Result: {num_1 * num_2}"


def divide(num_1, num_2):
    """Division"""
    return f"Result: {num_1 / num_2}"


if __name__ == "__main__":
    while True:
        welcome_message = input("Your operation: ")
        if welcome_message == "+":
            try:
                print(plus(num_1=float(input()), num_2=float(input())))
            except:
                print("Wrong input")
        elif welcome_message == "-":
            try:
                print(minus(num_1=float(input()), num_2=float(input())))
            except:
                print("Wrong input")
        elif welcome_message == "*":
            try:
                print(multiply(num_1=float(input()), num_2=float(input())))
            except:
                print("Wrong input")
        elif welcome_message == "/":
            try:
                print(divide(num_1=float(input()), num_2=float(input())))
            except ZeroDivisionError:
                print("You cannot divide by zero")
            except:
                print("Wrong input")
        else:
            print("Math operation error, choose correct one(+ - * /): ")
