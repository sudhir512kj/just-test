# class Car:
#     def __init__(self) -> None:
#         pass
#     def features(self, data):
#         pass

# class Bike:
#     def __init__(self) -> None:
#         pass
#     def features(self, data):
#         pass

# class Factory(data):
#     vehicles = {
#         'Car': Car,
#         'Bike': Bike
#     }

import copy

n = 3
m = 2
matrix = [[0 for i in range(n)] for j in range(m)]
print(matrix) 

obj = {
    "name": "hello"
}

newObj = copy.copy(obj)
anotherNewObj = copy.deepcopy(obj)
for each in obj:
    anotherNewObj[each] = obj[each]



