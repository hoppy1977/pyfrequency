import numpy as np

integer_array = np.random.randint(1, 11, 100)
print(integer_array)

frequencies = dict()
for number in integer_array:
    if(number in frequencies):
        frequencies[number] += 1
    else:
        frequencies[number] = 1

print(frequencies)

maxValue = max(frequencies.values())
maxKey = max(frequencies, key=frequencies.get)

print(f"The most frequenctly occuring integer is {maxKey} which occured {maxValue} times.")