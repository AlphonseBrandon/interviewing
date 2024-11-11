def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr_example = [2, 5, 6, 3, 9,10, 20]

print(f"Burble sorted array\n{bubble_sort(arr_example)}")


def bubble_sort2(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sample = [2, 8,5, 9, 3, 6]
print(f"Bubble sort example 2:\n{bubble_sort2(sample)}")
