#To read data from the console, we can use input (). However the input always reads only a string as usual with all other languages
my_number = int(input('Enter a number to check if it is even or not:'))
print(type(my_number))
if my_number %2==0:
    print(my_number,'is even')
else:
    print('not even')    