import random
from MyPackage.Tool import performance

def check(arr: list):
    n = len(arr)
    
    if n == 0 or len(arr) == 1:
        return True
    
    return arr[0] <= arr[1] and check(arr[1:])

def merge_sort(array, length):
    if length <= 1:
        return array
    
    left, left_length, right, right_length = split(array, length)
    
    left = merge_sort(left, left_length)
    right = merge_sort(right, right_length)
    
    return merge(left, left_length, right, right_length)

def merge(left, left_length, right, right_length):
    result = []
    i = 0
    j = 0
    while i < left_length and j < right_length:
        if left[i] == right[j]:
            result.append(left[i])
            result.append(right[j])
            i += 1
            j += 1
        elif left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    return result + left[i:] + right[j:]

def split(array: list, length: int) -> tuple[list, int, list, int]:
    mid = length // 2
    left = array[:mid]
    right = array[mid:]
    return left, mid, right, length - mid

@performance
def per(arr: list):
    return merge_sort(arr, len(arr))

a = [random.randint(-5, 5) for _ in range(100)]
print(a)
b = per(a)
print(b)
# print(check(b))

