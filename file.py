"""//////////////////////////////////////////////////////       # Multi line comment
Subj:   Coding Dojo > Python Stack > Python > Fundamentals > Reconize Python
By:     Virgilio D> Cabading Jr.    Created: October 24, 2021
/////////////////////////////////////////////////////////"""

num1 = 42                                       # Variable declaration, number primitive data type, initialize           
num2 = 2.3                                      # Variable declaration, number primitive data type, initialize
boolean = True                                  # variable declaration, boolean primitivedata type, initialize
string = 'Hello World'                          # variable declaration, string primitive data type, initialize
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
                                                # variable declaration, list composite data type, initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
                                                # variable declaration, dictionary composite data type, initialize
fruit = ('blueberry', 'strawberry', 'banana')   # variable declaration, tuple composite data type, initialize
print(type(fruit))                              # type method returns class type of argument, prints class tuple
print(pizza_toppings[1])                        # access value of list composite data type
pizza_toppings.append('Mushrooms')              # append method adds an item at the end of a list
print(person['name'])                           # access value of dictionary composite date type using a key
person['name'] = 'George'                       # change value of dictionary composite data type using a key
person['eye_color'] = 'blue'                    # initialize value of dictionary composite data type using a key
print(fruit[2])                                 # access value of tuple composite data type using an index

if num1 > 45:                                   # if conditional, access value of number primitive data type
    print("It's greater")                       # function that prints a string
else:                                           # else conditional
    print("It's lower")                         # function that prints a string

if len(string) < 5:                             # if conditional, len funtion, returns the number of characters in a string
                                                # access value of a string primitive data type
    print("It's a short word!")                 # function that prints a string
elif len(string) > 15:                          # else if contditional (note elif is short hand for else if)
                                                # len function, retrurns the number of characters if a string is passed as a parameter
    print("It's a long word!")
else:                                           # else conditional
    print("Just right!")

for x in range(5):                              # for loop, start at 0, stop at 6, increment by 1
                                                # range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
    print(x)                                    # prints a number
for x in range(2,5):                            # for loop, start at 2, stop at 5, increment by 1
    print(x)                                    # prints a number
for x in range(2,10,3):                         # for loop, start at 2, stop at 10, increment by 3
    print(x)                                    # prints a number
    
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)