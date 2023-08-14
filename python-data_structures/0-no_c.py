def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char == 'c' and char == 'C':
            my_string.remove(char)
        else:
            continue
        new_string += char
        return new_string
    


print(no_c("Chicago"))