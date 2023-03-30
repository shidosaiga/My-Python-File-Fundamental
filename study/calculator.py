num1 = int(input("enter you first number: "))
num2 = int(input("enter you second number: "))


print("Select operation.")  # Prints out the options for the user. 
print("1.Add")  # Addition option. 
print("2.Subtract") # Subtraction option. 
print("3.Multiply") # Multiplication option. 
print("4.Divide") # Division option. 

choice = int(input("choice to calculate 1/2/3/4 : "))

# def Add(a ,b ):
#     return a + b
# def Subtract(a ,b ):
#     return a - b
# def Multiply(a ,b ):
#     return a * b
# def Divide(a ,b ):
#     return a / b
    

   
if choice ==1:
    print(num1," + ",num2," = ", num1 + num2) #Add(num1,num2)
elif choice ==2:
     print(num1," - ",num2," = ", num1 - num2) #Subtract(num1,num2)
elif choice ==3:
     print(num1," * ",num2," = ", num1 * num2) #Multiply(num1,num2)
elif choice ==4:
      print(num1," / ",num2," = ", num1 / num2) #Divide(num1,num2)
else:
    print("error")
    