print('hello world')

name = "Tim"
greeting = "hello "
print(greeting+name+',')

name = "Aaron"

print(greeting,name)


#interpolating strings
print(f'Hello, {name}')

#== is a boolean there is no ===

#this is a list which === an array
my_list = ['b', 'c', 'd', 'e']
my_list.append('a')

#for loop in py
#counter = 0
#for letter in my_list:
 #   counter+=1
 #   print(counter, letter)

# for index in range(len(my_list)):
#     print(index, my_list[index])
    
#enumerates over the index and the element at the same time
# for (index, el) in enumerate(my_list):
#     print(index, el)
    
#list comprehensions

my_list[0] = 1


numbers = [1,2,3,4,5]\
#this is a list comprehension
squares = [num*num for num in numbers]

# print(squares)

halves = [num/2 for num in numbers]
# print(halves)

evens = [num for num in halves if(num%2 == 0)]

# print(evens)

names = ["logan", "isabel", "len", "steve", "Sarah"]

s_names = [name for name in names if name.capitalize().startswith('S')]

# print(s_names)

#to get a range

#print index 0 to 2
# print(my_list[0:3])
#stop print at index 3
# print(my_list[:3])
#print starting index 2
# print(my_list[2:])


#dictionary is made of key value pairs
my_dict = {"a": 1, "b":2}

my_dict["c"] = 3;

print(my_dict);


#tuples are like list but cannot change or add values
my_tuple = ('a', 1, 2)
print(my_tuple)