# Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.

# Expected output

# Case 1 
# base = 2
# exponent = 5
# 2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)

# Case 2 
# base = 5
# exponent = 4
# 5 raises to the power of 4 is: 625 
# i.e. (5 *5 * 5 *5 = 625)

# --------------------------------------------------------------------

# Pseudocode 

# Create an function named exponent (base,exp)
def exponent(base,exp):

# Inside the function, create a variable named result and set it to 1 
    result = 1 

# Inside the function, create a loop that will multiply the result to the base
    for i in range(exp):
        result = result * base         

# Return the result 
    return result 

# Create a variable to let the user input the base number
user_base = int(input("Input base here: "))

# Create a variable to let the user input the exponent number 
user_exponent = int(input("Input exponent here: "))

# Create a variable to place the inputted values in the function
result = exponent(user_base,user_exponent)

# Print the result 
print(user_base, "raises to the power of", user_exponent, "is:", result)