# Program to accept 3 distinct numbers and find smallest among them
x = int(input('Enter the value of 1st number'))
y = int(input('Enter the value of 2nd number'))
z= int(input('Enter the value of 3rd number'))
# check if valid input  
if x<y and x<z:
    print(x,' is smallest')
elif y<z and y<x:
    print(y,'  is smallest')
else:
    print(z,' is smallest')        