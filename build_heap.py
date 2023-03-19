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
        chunk_size = 1024
        with open(path, 'r') as file:
            n = int(file.readline().strip())
            swaps = []
            while True:
                chunk = file.readline().strip().split()
                if not chunk:
                    break
                chunk = list(map(int, chunk))
                swaps += build_heap(chunk)
            data = [x[0] for x in swaps]
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