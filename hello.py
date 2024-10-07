print("Hello World!")

# Basic data types
name = "Alice"  # string
age = 25    # integer
height = 5.9    # float
isStudent = True    # boolean

# Compound data types

fruits = ['apple','banana','cherry']    # list
coordinates = (10.0, 20.0)  # tuple
person = {'name':'Alice',   # dictionary
          'age': 25}
unique_numbers = {1,2,3,4,5}     #set

result = 10 + 3.5 # result will be a float

num_str = '100'
num_int = int(num_str) # converts to string

# Conditional statements --------------------------------

#If-Else

x = 10
if x > 0:
    print('x is positive')
elif x == 0:
    print('x is zero')
else:
    print('x is negative')

# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
    
# Combining If-Else with Loops

numbers = [1,2,3,4,5]

for num in numbers:
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
        
