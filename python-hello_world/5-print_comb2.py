# for i in range(100):
#     print("{:02d}".format(i),end=", ")
#     if i < 99:
#         print(end="\n")

for number in range(100):
    if number <= 98:
        print("{:02d}".format(number), end=", ")
    elif number == 99:
        print("{:02d}".format(number), end="\n")
    else:
        break