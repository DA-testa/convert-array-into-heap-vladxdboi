# python3
# Vladislavs Senevičs, 11.grupa, 221RDB453

import os

def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n//2, -1, -1):
        sift_down(i, data, swaps, n)
    return swaps

def sift_down(i, data, swaps, n):
    min_index = i
    for j in range(2*i + 1, n):
        if data[j] < data[min_index]:
            min_index = j
    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        sift_down(min_index, data, swaps, n)

def main():
    input_type = input("Enter input type: ")

    if 'I' in input_type:
        n = int(input())
        data = list(map(int, input().split()))
    elif 'F' in input_type:
        name = input().strip()
        path = os.path.join("tests", name)
        with open(path, 'r') as file:
            n = int(file.readline().strip())
            data = list(map(int, file.readline().strip().split()))
    else:
        print('Invalid input method')
        return
    
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()