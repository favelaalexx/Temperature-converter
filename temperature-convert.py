from progress.bar import Bar, ChargingBar
import os, time, random

def charging_bar():
    bar2 = ChargingBar('Processing:', max=100)
    for num in range(100):
        time.sleep(random.uniform(0, 0.1))
        bar2.next()
    bar2.finish()

def fahrenheit_celsius():
    # Convert temperature from Fahrenheit to Celsius
    fahrenheit = float(input('Enter the temperature in degrees Fahrenheit: '))
    celsius = (fahrenheit -32 ) * 5.0/9.0
    charging_bar()
    print()
    return '{} Celsius degrees are {} Farenheit degrees'.format(fahrenheit, celsius)
    
def celsius_fahrenheit():
    # Converts temperature in degrees Celsius to Fahrenheit
    celsius = float(input('Enter the temperature in degrees Celsius:'))
    fahrenheit = 9.0/5.0 * celsius +32
    charging_bar()
    print()
    return '{} Farenheit degrees are {} Celsius degrees' .format(fahrenheit, celsius)
     
while True:

    print("TEMPERATURE CONVERTER")
    print()
    print('1.- Fahrenheit to Celsius.')
    print('2.- Celsius to Fahrenheit.')
    print("3.- Exit.")

    try:
        option = int(input('Select an option:'))
        if option == 1:      
            print(fahrenheit_celsius())
        elif option == 2:
            print(celsius_fahrenheit())
        elif option == 3:
            print('Good Bye :)')
            break
        else:
            raise ValueError
    except ValueError:
        print('Enter only numbers.(1/2)')