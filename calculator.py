#Python Calculator to do all the arithmetic operations
#Declaration of variables for type of operation, first number and second number. 
#User selects the arithmetic operation to execute
#Enters the two numbers
#Program output the results

first_number = int(input("Enter first number: "))
operation = input("Enter arithmetic operation to perform: ")
second_number = int(input("Enter second number for the calculation: "))

if operation == "+":
   print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print (first_number * second_number)
elif operation == "/":
    print (first_number / second_number)
else:
    print("Invalid arithmetic symbol!")
