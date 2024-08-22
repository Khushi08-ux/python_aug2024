#Program to Find Count of digits of a number

num=[]
n=int(input("Enter  the number of digits"))
print("Enter the digits")
for i in range(n):
    digit=input()
    num.append(digit)
frequency=[0]*10
for digit in num:
    frequency[int(digit)]+=1
for i in range(10):
    print(f"Digit{i}:{frequency[i]}")    
