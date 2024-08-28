def partition_array(array):
    pivot=array[-1]
    j=0
    for i in range(len(array)-1):
        if array[i]<pivot:
            array[j],array[i]=array[i],array[j]
            j+=1
    array[j],array[i]=array[i],array[j]            

array=[432,4,5,5,6,5,876]
print(array)
    
partition_array(array)
print(array) 
