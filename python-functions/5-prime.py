def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) != 0:
                print("True")
                break 
            else:
                print("False")