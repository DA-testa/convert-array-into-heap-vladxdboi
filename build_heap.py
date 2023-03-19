# python3
# Vladislavs Senevičs, 11.grupa, 221RDB453

import os

def build_heap(data):
    swaps = []
    n = len(data)

    for i in range(n//2, -1, -1):
        j = i
        while True:
            left = 2 * j + 1
            right = 2 * j + 2
            min_val = j

            if left < n and data[left] < data[min_val]:
                min_val = left

            elif right < n and data[right] < data[min_val]:
                min_val = right

            elif min_val == j:
                break

            swaps.append((j, min_val))
            data[j], data[min_val] = data[min_val], data[j]
            j = min_val

    return swaps

def main():
    input_type = input("Enter input type: ")

    if input_type == 'I':
        n = int(input())
        data = list(map(int, input().split()))

    elif input_type == 'F':
        file_name = input("Enter file name: ").strip()
        path = os.path.join("tests", file_name)
        with open(path, 'r') as file:
            n = int(file.readline().strip())
            data = list(map(int, file.readline().strip().split()))
    else:
        print('Invalid input type')
        return
    
    assert len(data) == n

    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
