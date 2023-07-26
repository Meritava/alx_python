# fahrenheit = float(input("give temprature "))
# def convert_to_celsius(fahrenheit):
#     converted_temp = (fahrenheit - 32) * (5 / 9)
#     print("{}".format(converted_temp))

# # print("Temperature in Celsius = {:.2f}".formatconvert_to_celsius(fahrenheit))
# convert_to_celsius(fahrenheit)

# Define function to convert fahrenheit to celsius
def convert_to_celsius(fahrenheit):

    # Convert the Fahrenheit into Celsius
    C = (5 / 9) * (fahrenheit - 32)

    # Return the conversion value
    return C

# Take the Fahrenheit value from the user
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

# Print the Fahrenheit value
print("Temperature in Fahrenheit = {:.2f}".format(fahrenheit))

# Print the Celsius value
print("Temperature in Celsius = {:.2f}".format(convert_to_celsius(fahrenheit)))