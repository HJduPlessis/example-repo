int_list = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100];

def linear_search(arr, target): #most basic search algorithm, keeps code clean and simple
    for i in range(len(arr)):
        if arr[i] == target:
            return i;
    return -1;

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i];
        j = i - 1;
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j];
            j -= 1;
        arr[j + 1] = key;
    return arr;

def binary_search(arr, target): #binary search algorithms are used when the array is sorted, it divides the array into halves to find the target value
    left, right = 0, len(arr) - 1;
    while left <= right:
        mid = left + (right - left) // 2;
        if arr[mid] == target:
            return mid;
        elif arr[mid] < target:
            left = mid + 1;
        else:
            right = mid - 1;
    return -1;

print(linear_search(int_list, 9));  

print(binary_search(insertion_sort(int_list), 9));  