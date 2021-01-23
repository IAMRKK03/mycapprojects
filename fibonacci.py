#program to print the fibonacci series number
number= int(input(" Enter the value of number :")) #input the value of number of terms
a=0;b=1;sum=0;count=1; #intialising the variables
print(" Fibonacci Series: ") #print the series
while(count<=number): #starting of the while loop condition
    print(sum)
    count += 1
    a = b
    b = sum
    sum = a+b
