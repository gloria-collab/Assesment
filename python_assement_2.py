# question 1
''' Write a Python program that multiplies all the items in a list.

Sample list= [2, 3, 6]

Result = 36 '''

def solution(items):
    result = 1
    for item in items:
        result *= item
    return result
    
Sample_list= [2, 3, 6]
result = solution(Sample_list)
print(result)



#question 2
'''Write a Python program to get a list, sorted in increasing order by the last element in each tuple, 
from a given list of non-empty tuples.

Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

Expected result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

Hint: You can use the sort function.'''

def last_element(tup):
    return tup[-1]

def sort_by_last_element(tuples_list):
    tuples_list.sort(key=last_element)

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sort_by_last_element(sample_list)
print(sample_list)

#question 3
'''Write a Python program that combines two dictionaries by adding values for common keys.

d1 = {'a': 100, 'b': 200, 'c':300}

d2 = {'a': 300, 'b': 200, 'd':400}

Expected result: {'a': 400, 'b': 400, 'd': 400, 'c': 300}'''
def combine_dicts(d1, d2):
    for key, value in d2.items():
        if key in d1:
            d1[key] += value  # Add the value if the key exists in both dictionaries
        else:
            d1[key] = value  # Otherwise, add the key-value pair directly

    return d1

# Sample dictionaries
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Combine the dictionaries
result = combine_dicts(d1, d2)

print(result)

#Question 4
'''With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
 so that is an integral number between 1 and n (both included). Then the program should print the dictionary. 
 Suppose the following input is supplied to the program: 8. 
Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}'''
def generate_square_dict(n):
    return {i: i*i for i in range(1, n+1)}

n = 8

result = generate_square_dict(n)
print(result)

#Question 5
'''Write a program to sort a tuple by its float element.

For example: list= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

Expected result: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
'''
def get_float_value(tup):
    return float(tup[1])

def sort_by_float_element(tuples_list):
    return sorted(tuples_list, key=get_float_value, reverse=True)

# Sample list
list_of_tuples = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

# Sorting the list
sorted_list = sort_by_float_element(list_of_tuples)

print(sorted_list)

#Question 6
my_set = {0, 1, 2, 3, 4}
print("Set created:", my_set)

# 2. Iterating over the set
print("Iterating over the set:")
for item in my_set:
    print(item)

# 3. Add and remove items
my_set.add(5)  # Adding 5 to the set
my_set.remove(4)  # Removing 4 from the set
my_set.discard(3)  # Discarding 3 from the set

print("Updated Set:", my_set)



