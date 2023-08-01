def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if (number % i != 0):
            continue
        else:
            return False
        return True

    