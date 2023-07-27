for number in range(100):
    if number <= 98:
        print("{:02d}".format(number), end=", ")
    elif number == 99:
        print("{:02d}".format(number), end="\n")
    else:
        break