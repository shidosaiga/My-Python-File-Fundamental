customer_list = []
customer_age_list = []

def InputCustomer(list):
    for count in range(list):
        customer_list.append(input(f"Customer number {count} name is :"))
        customer_age_list.append(int(input(f"Customer number {count}age is :")))
    print("\n")

def ShowData():
    for data_name,data_age in zip(customer_list,customer_age_list):    
            print(f"custumer name {data_name} age is {data_age}\n")
    
    
amount_customer = int(input("How many yout customer :"))
InputCustomer(amount_customer)
ShowData()

# print(customer_list)
# print(customer_age_list)

