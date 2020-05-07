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

for index in range(len(my_list)):
    print(index, my_list[index])
    
#enumerates over the index and the element at the same time
for (index, el) in enumerate(my_list):
    print(index, el)
    
#list comprehensions

my_list[0] = 1


numbers = [1,2,3,4,5]\
#this is a list comprehension
squares = [num*num for num in numbers]

print(squares)

thirds = [num/3 for num in numbers]
print(thirds)
