import random


def binary_search(data, target):
    while True:
        if len(data) == 0:
            return False

        mid = len(data) // 2
        if data[mid] == target:
            return True
        else:
            if target < data[mid]:
                data = data[:mid]
            elif target > data[mid]:
                data = data[mid + 1:]


if __name__ == '__main__':
    data = [random.randint(0, 100) for _ in range(10)]
    data.sort()

    print(data)

    target = int(input('Enter a number to search: '))
    found = binary_search(data, target)

    print(found)
