# convert.py
#   A program to convert Celsius to Fahrenheit.
#
# by: st33ze

def main():
    # Introduction
    print("Hello, I am converting Celsius degrees into Fahrenheit.")

    # Calculate
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32

    # Print output
    print("The temperature is {} degrees Fahrenheit."
          .format(fahrenheit))

main()
