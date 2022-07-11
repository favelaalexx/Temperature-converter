import os, time

def clean_screen():
    # Clean the screen when we call them
    time.sleep(1)
    os.system("cls")

def fahrenheit_celsius():
    # Convert temperature from Fahrenheit to Celsius
    fahrenheit = float(input('Enter the temperature in degrees Fahrenheit: '))
    celsius = (fahrenheit -32 ) * 5.0/9.0
    print()
    print('{:.1f}° Celsius degrees are {:.1f}° Farenheit degrees'.format(fahrenheit, celsius))
    
def celsius_fahrenheit():
    # Converts temperature in degrees Celsius to Fahrenheit
    celsius = float(input('Enter the temperature in degrees Celsius: '))
    fahrenheit = (celsius +32 ) * 9.0/5.0
    print()
    print('{:.1f}° Farenheit degrees are {:.1f}° Celsius degrees' .format(fahrenheit, celsius))

def exit():
    # Kill the program
    clean_screen()
    print('Good Bye :)') 
    clean_screen()   
 
while True:
    print()
    print("=================================")
    print("     TEMPERATURE CONVERTER       ")
    print("=================================")
    print()
    print('[1] Fahrenheit to Celsius')
    print('[2] Celsius to Fahrenheit.')
    print("[3] Exit.")

    try:
        option = int(input('Select an option: '))
        if option == 1:      
            fahrenheit_celsius()
        elif option == 2:
            celsius_fahrenheit()
        elif option == 3:
            exit()
            break
    except ValueError:
        print('Enter only numbers (1-3)')