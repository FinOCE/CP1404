def main():
    file = open("temps_input.txt", "r")
    values = file.readlines()
    result = ''
    for i in range(0, len(values)):
        result += f"{fahrenheit_to_celsius(float(values[i]))}\n"
    file.close()

    file = open("temps_input.txt", "w")
    file.write(result)
    file.close()

def celcius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

main()