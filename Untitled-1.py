# # birth_age= input("input your year of birth: ")

# # age = int(birth_age) - 2025
# # print(age)

# # course ='python for beginners'
# # print(course.replace('x', '4'))

# # course ='python for beginners'
# # print(course.find('for'))

# # x= 10
# # x -= 4
# # print(x)

# #logical operators: and , or
# # price=25
# # print(price > 10 and price < 30)

# #if statements
# # temperature = 25

# # if temperature > 30:
# #     print("it's a hot day")
# #     print("drink plenty of water")
# # elif temperature > 20:
# #     print("its a nice day")
# # elif temperature > 10:
# #     print("its a bit code")
# # else:
# #     print("its code")

# # exercise = int(input('Whats your weight: '))
# # size =input("(k)g or (l)bs: ").lower()
# # gravity =  9.81
# # double_mass= 0.22481
# # if size == 'l':
# #     mass = exercise // gravity
# #     print("weight in kg: {} ".format(mass) )
# # elif size == 'k':
# #     mass2 = exercise * double_mass
# #     print("weight in (L)bs: {} ".format(mass2) )


# # exercise = int(input('Whats your weight: '))
# # size =input("(k)g or (l)bs: ").lower()
# # gravity =  9.81
# # double_mass= 0.22481
# # if size == 'l':
# #     mass = exercise // 0.45
# #     print("weight in kg: {} ".format(mass) )
# # elif size == 'k':
# #     mass2 = exercise * 0.45
# #     print("weight in (L)bs: {} ".format(mass2) )
# # else:
# #     print("rerun")

# #loop
# i = 1
# while i <= 10:
#     print('*' * i)
#     i = i + 1

# # sets
# names= ['kola','gloria','tolu','chidi','tonye']
# names[0]='kol' ## to change a sring in a list 
# print(names[0])

# numbers = [1,2,3,4,5]
# # numbers.insert(5, 6)
# numbers = [1,2,3,4,5]
# #print(1 in numbers)
# print(len(numbers))

# numbers = [1,2,3,4,5]
# for items in numbers:
#     print(items)

# i = 0
# while i < len (numbers):
#     print(i)
# i = 0
# while i <= 10:
#     print('*' * i)
#     i = i + 1


# i = 5
# while i >= 1:
#     print('*'* i)
#     i = i - 1
#     break

# p= "hello world"
# print(p)

#FUNCTIONS
'''
function = A block of reuseable code
    place () after the function name to invoke it
'''

# def birthday(name,age): # name is the parameter
#     print(f"happy birthday to {name}")
#     print(f"you are {age} years old")
#     print("You are Old")

# birthday('gloria',20)

# def display_invoice(username, amount, due_date):
#     print(f"hello {username}")
#     print(f"your bill of ${amount:.2f} is due: {due_date}")

# display_invoice('gloria', 100.01, "01/02")

'''
Return statement :
this is a statement used to end a function 
and send a result back to the caller
'''
def add(x,y):
    z= x + y
    return z

def subtract(x,y):
    z= x - y
    return z

def multiply(x,y):
    z= x * y
    return z

def divide(x,y):
    z= x / y
    return z

# print(add(1,3))
# print(multiply(1,3))
# print(divide(1,3))  
# print(subtract(1,3))

def creation_name(first_name,last_name):
    first_name = first_name.capitalize()
    last_name=last_name.capitalize()
    return first_name + " " + last_name

full_name = creation_name("George","Gloria")
print(full_name)
