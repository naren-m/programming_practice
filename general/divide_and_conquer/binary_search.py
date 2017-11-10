# Problem Grokking algorithms book. Exercise 4.4


def binary_search(arr, element, start=0, end=0):
    print(arr, element, start, end)
    if start >= end:
        return -1

    mid = (start + end) // 2

    if element == arr[mid]:
        return mid
    elif element < arr[mid]:
        # element to find is less than mid. search in left sub array
        return binary_search(arr, element, start, mid - 1)
    else:
        # element to find is greater than mid. search in right sub array
        return binary_search(arr, element, mid + 1, end)


l = [1, 2, 3, 4, 5]

print(binary_search(l, 5, 0, len(l)))

print(binary_search(l, 3, 0, len(l)))

print(binary_search(l, 1, 0, len(l)))