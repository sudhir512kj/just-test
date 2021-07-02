# create a dictionary
# keys are tuples and values are list
key = (1, 2, 3, 4)
val = ['strawberry', 'blackberry', 'cloudberry', 'blueberry']
# zip() function ties them up together like real life zip does
berries = {key: val for (key, val) in zip(key, val)}
print(berries)


# cal squars of numbers and create a dictionary
sqr = {x: x**2 for x in [2, 3, 7, 6, 9]}
print(sqr)


#  Create a new dictionary from an existing dictionary

k = [i for i in range(1, 10)]
v = [j*3 for j in range(1, 10)]
nums = {key: val for (key, val) in zip(k, v)}
print(nums)
# now use above dictionary to perform dictionary comprehension
# add 5 to every element of dictionary and create new one
add_nums = {k: v+5 for k, v in nums.items()}
print(add_nums)


# Conditionals with comprehensions
# extract even numbers and square them up to create new dict
even = {x: x**2 for x in range(1, 10) if x % 2 == 0}
print(even)

# add multiple conditions to if clause
odd = {x: x**2 for x in range(1, 20) if x > 2 and x % 2 != 0}
print(odd)

# Nested if-else with comprehensions
# lets say we have dictionary of persons and categorize them as young, adult and senior citizens as per their age
# logic age<18 young, age>18 and age<=60 adult, age>60 senior citizen
per_age = {'kobe': 2, 'vivek': 30, 'richie': 19,
           'vishakha': 28, 'krish': 62, 'jeff': 65, 'billy': 12}
age_cat = {k: ('young' if v <= 18 else 'adult' if (
    v >= 18 and v <= 60) else 'senior citizen') for k, v in per_age.items()}
print(age_cat)

# Nested Dictionary Comprehension
# nested dictionary comprehension
# kind of multiplication table from numbers 1 to 3
nestd = {v1: {v2*v1 for v2 in range(1, 11)} for v1 in range(1, 4)}
print(nestd)
