temp_value = float(input("input your temp value "))
def converting(value):
    converted_value = (5 / 9) * (value - 32)
    return converted_value

def convert_to_celsius(fahrenheit):
    user_value = converting(fahrenheit)
    print("Your temp is {}".format(user_value))

convert_to_celsius(temp_value)