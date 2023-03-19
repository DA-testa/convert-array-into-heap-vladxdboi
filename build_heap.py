# python3
# Vladislavs Senevičs, 11.grupa, 221RDB453

import os

def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n//2, -1, -1):
        swaps += sift_down(data, i)
    return swaps

def sift_down(data, i):
    swaps = []
    n = len(data)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[left] < data[i]:
            j = left
            if right < n and data[right] < data[left]:
                j = right
        elif right < n and data[right] < data[i]:
            j = right
        else:
            continue

        swaps.append((i, j))
        data[i], data[j] = data[j], data[i]
    return swaps

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