#python-for-applied-data-science-ai


#Strings: Start #####################
#####################################


#Consider the variable <code>d</code> use slicing to print out the first three elements:
d = "ABCDEFG"
print(d[0:3])
#Use a stride value of 2 to print out every second character of the string <code>e</code>:
e = 'clocrkr1e1c1t'
print(e[::2])
#print upper and lower case:
f = "You are wrong"
f2="YOU ARE RIGHT"
print(f.upper())
print(f2.lower())

#Consider the variable g, and find the first index of the sub-string snow:
g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
g.find('snow')
#In the variable g, replace the sub-string Mary with Bob and comma with dot:
g.replace('Mary', 'Bob')
g.replace(',', '.')
#In the variable g, split the substring to list:
g.split()
#In the string s3, find whether the digit is present or not using the \d and search() function:
import re
s3 = "House number- 1105"
re.search(r'\d', s3)
#In the string <code>str1</code>, replace the sub-string <code>fox</code> with <code>bear</code> using <code>sub() </code>function:
str1= "The quick brown fox jumps over the lazy dog."
re.sub('fox', 'bear', str1)

#In the string str2 find all the occurrences of woo using findall() function:
str2= "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"
re.findall(r'woo', str2)

### Sting finished #####################
#####################################

#### Lists: Start #################
#####################################
#Quiz on List
#Create a list a_list, with the following elements 1, hello, [1,2,3] and True.
a_list = [1,'hello', [1,2,3], True]

#Find the value stored at index 1 of a_list.
a_list[1]
#Retrieve the elements stored at index 1, 2 and 3 of a_list.
a_list[1:4]

#Concatenate the following lists A = [1, 'a'] and B = [2, 1, 'd']:
A = [1, 'a']
B = [2, 1, 'd']
A_B = A + B
print(A_B)

# Create an empty list
shopping_list = []
#Now store the number of items to the shopping_list: Watch, Laptop, Shoes, Pen, Clothes
items = ['Watch', 'Laptop', 'Shoes', 'Pen', 'Clothes']
shopping_list = items
print(shopping_list)
# Add a new item to the shopping_list (football)
shopping_list.append('football')
#Print First and last item from the shopping_list
print(shopping_list[0])
print(shopping_list[-1])

#Print "Laptop" and "shoes"

shopping_list.index('Laptop')
shopping_list.index('Shoes')
print(shopping_list[1], shopping_list[2])

#Change the item from the shopping_list
#Instead of "Pen" I want to buy "Notebook" let's change the item stored in the list.
index = shopping_list.index('Pen')
print(index)
shopping_list[index] = 'Notebook' 
print(shopping_list)

# delete item 'clothes'
index = shopping_list.index('Clothes')
print(index)
del(shopping_list[4])
print(shopping_list)

#### Finished Lists #################
#####################################

### TUPLES Start #######################
########################################

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco")
#find the length of the tuple
print(len(genres_tuple))

#Access the element, with respect to index 3:
genres_tuple[3]
#Use slicing to obtain indexes 3, 4 and 5:
genres_tuple[3:6]

#Find the first two elements of the tuple genres_tuple:
genres_tuple[0:2]

#Find the index of 's' in "disco":
genres_tuple.index("disco")
item = genres_tuple[7]
letter_index = item.find('s')
print(letter_index)

#Generate a sorted List from the Tuple <code>C_tuple=(-5, 1, -3)</code>:
C_tuple=(-5, 1, -3)
C_tuple_sorted = sorted(C_tuple)
print(C_tuple_sorted)

### TUPLES Finish #######################
########################################