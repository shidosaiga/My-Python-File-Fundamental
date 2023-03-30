name = input("what is you name? : ")
age = input("what is you age? : ")

def hello(YouName,YouAge):
    print(":-------------------------------------------:")
    print(f"I'm {YouName}. My age is {YouAge} year old.")
    print(":-------------------------------------------:")
hello(name,age)

num1 = int(input("number of num1 : "))
num2  =int(input("number of num2 : "))

def add(a,b):
    return a + b

print(f"{num1} + {num2} = ", add(num1,num2))


    