def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("an error occored")
    else:
        print("none")
    finally:
        print("{:d} / {:d} = {}".format(a, b, result))
        return result