#Program to print positive number from a given list
list_1=[]
n=int(input("Enter the list size: "))
for i in range(0, n):
    item=int(input("Enter the numbers in the list: "))
    list_1.append(item)
print("User list is", list_1)
for number in list_1:
    if number > 0:
        print("The positive integer are: ", +number)
