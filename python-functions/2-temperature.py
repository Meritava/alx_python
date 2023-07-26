user_input = float(input("give temprature "))
def convert_to_celsius(fahrenheit):
    converted_temp = (fahrenheit - 32) * (5 / 9)
    return converted_temp
convert_to_celsius(400)
print(convert_to_celsius)