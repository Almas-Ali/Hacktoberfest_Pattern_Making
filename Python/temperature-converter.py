#! /usr/bin/python3

#Get the temperature from user:
temp = input("Input the  temperature you like to convert (For example: 28C, 52F): ")
#Split the value:
degree = int(temp[:-1])
i_convention = temp[-1]

#Check whether temperature entered in Celsius:
if i_convention.upper() == "C":
    result = int(round((9 * degree) / 5 + 32))
    o_convention = "Fahrenheit"
#Check whether temperature entered in Fahrenheit:
elif i_convention.upper() == "F":
    result = int(round((degree - 32) * 5 / 9))
    o_convention = "Celsius"
else:
    print("I don't get this. Sorry. Bye!")
    quit()

print("The temperature in", o_convention, "is", result, "degrees.")
