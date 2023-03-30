number_list = []

def Inputnumber_list(list):
    for count in range(list):
        count = count + 1
        number_list.append(int(input(f"Enter number {count} to fine Min and Max :")))
        
MinMax_list = int(input("Cout number : "))        
Inputnumber_list(MinMax_list)

print(number_list)
print(f"Max :{max(number_list)}")
print(f"Min :{min(number_list)}")

mean = sum(number_list)/len(number_list)

print(f"mean :{int(mean)}")





