def is_same_class(obj, a_class):
    if issubclass(obj, a_class):
        print("{} is an instance of the class {}".format(obj, a_class))
    else:
        return False