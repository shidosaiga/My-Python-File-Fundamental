customer_list = [] 
print(f"before list {customer_list}")
def InputUser(round):
    for cout in range(round):
        # cout = cout + 1
        customer_list.append(input(f"Name of customer {cout} :"))
        # customer_list.append(input("Name of customer +str(cout)+ :"))

def ShowData():
    for data in customer_list:
        print(f"Hello {data}")
        
user = int(input("cout: "))
InputUser(user)
ShowData()    
print(f"after list {customer_list}")

