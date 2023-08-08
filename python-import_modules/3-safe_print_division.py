def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("an error occored")
    else:
        print("none")
    finally:
        print("Inside result: {}".format(result))
        return result