customer_list = [] 
user = int(input("cout: "))
for cout in range(user):
    # cout = cout + 1
    customer_list.append(input("Name of customer "+str(cout)+" :"))
for data in customer_list:
    print(f"Hello {data}")
    
    
print(customer_list)