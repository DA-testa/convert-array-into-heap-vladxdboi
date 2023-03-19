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
    min = i
    for j in range(2*i + 1, n):
        if data[j] < data[min]:
            min = j
    if i != min:
        swaps.append((i, min))
        data[i], data[min] = data[min], data[i]
        sift_down(min, data, swaps, n)

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
            swaps = []
            for _ in range(n):
                data = list(map(int, file.readline().strip().split()))
                swaps += build_heap(data)
    else:
        print('Invalid input method')
        return
    
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()