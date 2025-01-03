def calculator():
    print("----Enter your equation----")
    a = input("Enter your equation: ")
    a = a.replace('^', '**')
    a = a.replace('%', '/100')

    try:
        b = eval(a)
        print(f"The result of the equation {a} is: {b}")
    except ZeroDivisionError:
        print("Error! Number Divided by Zero")
    except Exception as e:
        print(f"Error! Invalid equation. Details: {e}")

calculator()