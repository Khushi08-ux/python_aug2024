def my_function (some_list):
    some_list.remove(10)
    some_list.insert(1,25)
    some_list.append(50)

print("Enter space separated numbers")
list1=list(map(int,input().split()))
print(list1)
my_function(list1) #call by refernce
print(list1)