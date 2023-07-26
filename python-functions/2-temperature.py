#!/usr/bin/env python3
user_input = float(input("give temprature"))
convert_to_celsius = __import__('2-temperature').convert_to_celsius
def convert_to_celsius(fahrenheit):
    converted_temp = convert_to_celsius * user_input
    return converted_temp
convert_to_celsius(400)