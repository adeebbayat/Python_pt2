from random import shuffle
data = [1,5,7,3,4,5,5,7,8,6,3,3]

def is_sorted(data) -> bool:
    return all(a <= b for a, b in zip(data,data[1:]))

def bogosort(data) -> list:
    count = 1
    while not is_sorted(data):
        shuffle(data)
        print(count)
        count = count + 1
    return data

print(bogosort(data))