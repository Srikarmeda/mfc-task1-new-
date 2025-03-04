import time
import random
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time
size = 1000 
arr1 = [random.randint(0, 10000) for _ in range(size)]
arr2 = arr1[:]
arr3 = arr1[:]
bubble_time = measure_time(bubble_sort, arr1)
selection_time = measure_time(selection_sort, arr2)
insertion_time = measure_time(insertion_sort, arr3)
print(f"Bubble Sort Time: {bubble_time:.6f} seconds")
print(f"Selection Sort Time: {selection_time:.6f} seconds")
print(f"Insertion Sort Time: {insertion_time:.6f} seconds")
