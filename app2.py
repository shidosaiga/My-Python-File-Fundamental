# Create a function to add two numbers 
def add(x, y):
   return x + y

# Create a function to subtract two numbers 
def subtract(x, y):
   return x - y

# Create a function to multiply two numbers
def multiply(x, y):
   return x * y

# Create a function to divide two numbers 
def divide(x, y):
   return x / y

 # Take input from the user 
print("Select operation.")  # Prints out the options for the user. 
print("1.Add")  # Addition option. 
print("2.Subtract") # Subtraction option. 
print("3.Multiply") # Multiplication option. 
print("4.Divide") # Division option. 

 # Store input as choice variable  
choice = input("Enter choice(1/2/3/4): ")

 # Convert string to int type  
choice = int(choice)

 # Take input from the user for num1 and num2 variables  

num1 = float(input("Enter first number: "))

num2 = float(input("Enter second number: "))

if choice == 1:                                      # If statement for addition operation    
    print(num1,"+",num2,"=", add(num1,num2))         # Prints out the result of the addition operation   
elif choice == 2:                                    # If statement for subtraction operation    
    print(num1,"-",num2,"=", subtract(num1,num2))    # Prints out the result of the subtraction operation   
elif choice == 3:                                    # If statement for multiplication operation    
    print(num1,"*",num2,"=", multiply(num1,num2))    # Prints out the result of the multiplication operation   
elif choice == 4:                                    # If statement for division operation    
    print(num1,"/",num2,"=", divide(num1,num2))      # Prints out the result of the division operation