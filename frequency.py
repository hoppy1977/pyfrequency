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

max_value = max(frequencies.values())
max_keys = set()
for current_key, current_value in frequencies.items():
    if max_value == current_value:
        max_keys.add(str(current_key))

outputString = ','.join(max_keys)

print(f"The integer/s {outputString} occured {max_value} times.")