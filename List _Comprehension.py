#list , set , dict

my_list = [char for char in 'helllppo']
my_list2 = [num * 2 for num in range (1,200)]
my_list3 = [num **2 for num in range (1,100) if num % 2 == 0]

print(my_list)
print(my_list2)
print(my_list3)

#set comprehension
my_set = {char for char in 'helllppo'}
print(my_set)

#dict comprehension
simple_dict = {
    'a' : 1,
    'b' : 2
}

my_dict = {key:value**2 for key,value in simple_dict.items()}
my_dic2 = {key:value**2 for key,value in simple_dict.items() if value % 2 == 0}
my_dict3 = {num : num*2 for num in [1,2,3]}

print(my_dict)
print(my_dic2)
print(my_dict3)


#Exercise

some_list = ['a' , 'b' , 'c', 'b' , 'd' , 'm' , 'n' ,'n']

duplicates = [x for x in some_list if some_list.count(x)>1]
duplicates = list({char for char in duplicates})

print(duplicates)