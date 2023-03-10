#Fundamental Data types
#1
##Int and float: int for absolute numbers and float for numbers with "decimals"
# print(type(1+2))
# print(type(2*4))
# print(type(2-4))
# print(type(2/4))

# print(type(0))
# print(type(0.0))

# print(1+2)
# print(1-2)
# print(1*2)
# print(1/2)
# print(1**2)
# print(1//2)
# print(1%2)

#2
#math functions
# print(round(3.7))
# print(abs(-45))

#3
#operator precedent
# print(20-3*4)
# print((20-3)+2**2)

# ();**;*/;+-

#4
# print(bin(89))
# print(int('0b101100101', 2))

## Variables
# user_iq = 190
# _user_iq = 134

# a,b,c=1,2,3

# print(b)

#5
#augmented assignment operator

# some_value = 5
# some_value = 5+2
# some_value *= 2

##useful
# + --> add
# - -->subtract
# / --> divide
# * --> multiply
# ** --> power of
# // --> returns the integer rouded down like 1//2=0
# % --> returns de reminder of a division like 5%4=1 (5/4=2 with a reminder of 1)
# round --> returns the rounded number
# abs --> returns the absolute number
  


# print(some_value)

##strings

# print(type("hi hello there 21!"))

# username = 'powercoder'
# pasword = 'supersecret'
# long_string = '''

# WOW
# O O
# ---

# '''

# print(long_string)

# first_name = 'Pedro'
# last_name = 'Raposo'

# full_name = first_name + ' ' + last_name

# print(full_name)

#string concatenation --> adding strings together
# print(type(int(str(100))))
#type conversion

##escape sequence  --> \

# i can't write "it's" because of the apostroph
# weather = '\t it\'s \"kind of\" sunny \n hope you have a good day'
# print(weather)

##formating strings

# name = 'Johnny'
# age = 55


# print('hi ' + name + '. You are ' + str(age) + ' years old.')

# #formated way --> f --> {}  also called fstring

# print (f'hi {name}. You are {age} years old.')

# #old way
# print('hi {}. You are {} years old.'.format(name, age))
# print('hi {new_name}. You are {age} years old.'.format(new_name='Sally', age = 100))

#6

# selfish ='0123456789'
# #       #   01234567

# # print(selfish[6])

# # # we can set a start and finnish inside the string by apply [start:stop:stepover]

# # print(selfish[4:6:2])
# # print(selfish[::1])

# print(selfish[::-1])  #starts on the end and go backwards with the minus

## immutability - strings in python are immutable, they can't be changed once creted, the only way to change their value is completly assign a new value

# rod = '123'
# # rod[0] = '4'  --> it doesn't work


# rod = '1234'   # the previous value is erased and substituited by this one

# print(rod)

##buitl-in functions and methods
# quote = 'to be or not to be'
# quote2 = quote.replace('be','me')
# # print(greet[0:len(greet)])
# # print(len(greet))

# print(quote.upper())
# print(quote.capitalize())
# print(quote.find('be'))
# print(quote.replace('be','me'))
# print(quote)
# print(quote2)

##booleans

# name = 'Pedro'
# is_cool = False

# is_cool = True

# print(bool(1))
# print(bool(0))
# print(bool('true'))


##exercise

# name ='Pedro Raposo'
# age = 30
# relationship_status = 'single'

# relationship_status='it\'s complicated'
# print(relationship_status)

# birth_year = input('what year were you born? ')

# age = 2022 - int(birth_year)

# print(f'your age is : {age}')


# create a password checker



##list

# li = [1,2,3,4,5]
# li2 = ['a','b','c']
# li3 = [1,2,'a',True]

# # Data structure: way of organize info or data in a "folder"

# amazon_cart = [
#   'notebooks', 
#   'sunglasses',
#   'grapes',
#   'toys',
#   'cellphone'
# ]

# print(amazon_cart[0::2])
# amazon_cart[0] ='laptop' 
# print(amazon_cart)

# ##list slicing

## matrix

# matrix = [
#   [1,2,3],
#   [2,4,6],
#   [7,8,9]
# ]

# print(matrix[0][1])

## list method
# basket = [1,2,3,4,5,]

# print(len(basket))

#adding
# new_list = basket.append(100)
# new_list=basket
# print(basket)
# print(new_list)

# basket.insert(4,100)
# print (basket)
# new_list2 = basket.insert(5,100)
# print(new_list2)


# new_list3 = basket.extend([100, 101])
# print (new_list3)
# print(basket)


## removing

# basket.pop() #--> removes the last item of the list
# basket.pop(0) #--> removes the first item of the list. we give the index we want to remove
# basket.remove(4) #--> we give the number we want to remove
# print (basket)
# new_list4 = basket.remove(2)
# new_list5 = basket.pop(2) #--> pop returns whatever we just remove
# print(new_list4)
# print(new_list5)
# print(basket.pop(2))

# new_list = basket.clear() #--> removes what's on the list
# print(basket)

##Index

# print(basket.index(2))

# basket_a = ['a','x','b','c','d','e','f','d']
# print('z' in basket_a) #--> show if there are a item in a list

# print(basket_a.index('d',0,4)) #--> show in what index is the item we want in a list

# print(basket_a.count('d')) #--> show how many items we seaech are on a list

# basket_a.sort()

# print(basket_a.sort())
# new_basket=basket_a[:]
# new_basket=basket_a.copy() #--> make a copy of a list
# new_basket.sort()
# basket_a.sort() #--> puts every item in "order"
# basket_a.reverse() #--> reverse the values of a list
# print(sorted(basket_a)) #--> do the "same thing" of sort but form of a function
# print(basket_a)
# print(new_basket)
# basket_a.sort()
# basket_a.reverse()
# print(len(basket_a))
# print(basket_a[::-1])

# print(basket_a)

# print(list(range(1,100)))
# print(list(range(100)))
# sentence=' '
# new_sentence=sentence.join(['hi,', 'my', 'name', 'is', 'Pedro'])
# new_sentence2=' '.join(['hi,', 'my', 'name', 'is', 'Pedro'])

# print(new_sentence)
# print(new_sentence2)


## list unpacking

# a,b,c,*other,d = [1,2,3,4,5,6,7,8,9]
# print(a)
# print(b)
# print(c)
# print(other)
# print(d)

# ##None
# a=None
# print(a)

##dictionary

# dictionary = {
#   'a':[1,2,3],
#   'b':'hello',
#   'x': True
# }

# my_list = [
#   {
#   'a':[1,2,3],
#   'b':'hello',
#   'x': True
#   },
#   {
#   'a':[4,5,6],
#   'b':'hello',
#   'x': True
#   }
# ]
# print(dictionary['a'][0])
# # print(dictionary)
# print(my_list[0]['b'])


### understandiong data structures

# dictionary = {
# '123' : [1,2,3],
# '123' : 'hello'
# }

# print(dictionary['123'])

# user = {
# 'basket' : [1,2,3],
# 'greet' : 'hello',
# 'age': 20
# }

# user2 = dict(name='JohnJohn')          #dict(key=value) --> another way to create a dictionary by a method

# print(user.get('age', '55'))
# print(user2)

# print('age' in user.keys())
# print('hello' in user.values())
# print(user.items())

# # user.clear()
# print(user)

# # user3 = user.copy()
# # print(user.clear())
# # print (user3)

# # print(user.pop('age'))
# # print(user.popitem())
# print(user.update({'ages':55}))

# print(user)


## tuple --> a tuple is like a list but ummutable, they can't be changed

# my_tuple = (1,2,3,4,5,5)
# print(my_tuple[1])
# print(5 in my_tuple)

# user = {
# (1,2) : [1,2,3],
# 'greet' : 'hello',
# 'age': 20
# }

# print(user.items())
# print(user[(1,2)])

# # x=my_tuple[0]
# # y=my_tuple[1]

# x,y,z, *other = (1,2,3,4,5)

# new_tuple = my_tuple[1:4]   #the tuples can be sliced
# print(new_tuple)
# print(other)
# print(x)
# print(y)
# print(x+y)

# print(my_tuple.count(5))
# print(my_tuple.index(2))
# print(len(my_tuple))

## set --> unordered collections of unique objects

# my_list=[1,2,3,4,5,5]
# my_set = {1,2,3,4,5,5}
# # my_set.add(100)
# # my_set.add(2)
# print(my_set)
# print(set(my_list)) #--> new set created from a list
# new_set=my_set.copy()
# print(1 in my_list)
# print(len(my_set))
# print(new_set)
# print(my_set.clear())
# print(new_set)
# print(my_set)

# my_set = {1,2,3,4,5,5}
# new_set=my_set.copy()
# my_set.clear()
# print(new_set)
# print(my_set)

# sets 2

my_set = {4,5}
your_set = {4,5,6,7,8,9,10}
print(my_set)
# print(my_set.difference(your_set))  #*
# print(my_set.discard(5)) #*
# print(my_set)

# print(my_set.difference_update(your_set)) #*
# print(my_set)

# print(my_set.intersection(your_set)) #*
# print(my_set & your_set) # a shortcut for intersection
# print(my_set.isdisjoint(your_set)) #* --> it says if the the 2 sets have something in commun

# print(my_set.union(your_set)) #* add 1 set to another and removes all the duplicated values
# print(my_set|your_set) # a shortcut for union

print(my_set.issubset(your_set))
print(my_set.issuperset(your_set))

print(your_set.issuperset(my_set))