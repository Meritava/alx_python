user_input = float(input("enter your temperature "))
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

convert_to_celsius(user_input)