# Shellsort algorithm

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# Example:
my_list = [12, 34, 54, 2, 3]
shell_sort(my_list)
print("Sorted array:", my_list)

