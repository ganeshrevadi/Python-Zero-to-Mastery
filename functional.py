from functools import reduce

lambda param: action(param)


my_list = [1,2,3]
ur_list = [10,20,30]
their = (1000,2000,3000)
def multiplyby2(item):
    return item * 2

def odd_only(item):
    return item %2 != 0

def accumulator(acc,item):
    return acc + item
#Map
print(list(map(multiplyby2,my_list)))
print(my_list)

# Filter 
print(list(filter(odd_only,my_list)))
print(my_list)

#Zip
print(list(zip(my_list,ur_list,their)))
print(my_list)

#Reduce
print(reduce(accumulator, my_list, 0))
print(my_list)

#Lambda
print(list(map(lambda item: item * 2,my_list)))
print(my_list)
 