# 1c. Create a program that asks the user to provide 2 numbers 
# and output the GCD (Greatest Common Divisor) and LCM (Lowest Common Multiple) 
# of both numbers.

def LCM(num1, num2):
    # Check for zero input
    if num1 == 0  and num2 == 0:
        return "undefined"
    elif num1 ==0 or num2 == 0:
        return 0
    
    # To keep track of each multiplicative
    oldnum1 = num1
    oldnum2 = num2
    
    # LCM of two numbers should be equal to each other
    # While theyre not equal, iteratively check their multiplacitive
    while (num1 != num2):
        while (num2 > num1):
            num1 += oldnum1
        while (num1 > num2):
            num2 += oldnum2

    return num1 # Or return num2

# GCD can be define by LCM, so just reuse the LCM method
def GCD(num1, num2):
    if num1 == 0 and num2 == 0:
        return "undefined"
    elif num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    else:
        return int(num1*num2/LCM(num1, num2))


print("Input 2 numbers to find the GCD (Greatest Common Divisor) and LCM (Lowest Common Multiple) of the two numbers.")
while True:
    try:
        input_one = int(input("First input: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

while True:
    try:
        input_two = int(input("Second input: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("GCD: ", GCD(input_one, input_two))
print("LCM: ", LCM(input_one, input_two))
