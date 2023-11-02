def check(arr: list) -> bool:
    n = len(arr)
    
    if n == 0 or len(arr) == 1:
        return True
    
    return arr[0] <= arr[1] and check(arr[1:])

def merge(arr1: list, arr2: list) -> list:
    """
    
    :param arr1:
    :param arr2:
    :return:
    """
    i = 0
    j = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            result.extend([arr1[i], arr1[i]])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    result.extend(arr2[j:])
    result.extend(arr1[i:])
    return result

def split(arr: list) -> tuple[list, list]:
    """
    - O(k) where k represent slice size
    :param arr:
    :return:
    """
    length = len(arr) // 2
    # arr[:length]: O(k) where k represent slice size
    left = arr[:length]
    right = arr[length:]
    
    return left, right

def merge_sort(arr: list) -> list:
    """
    - Sorts a order list in ascending
    - Take O(k*n*log(n)) time complexity and O(n) space complexity
    :param arr:
    :return:
    """
    if len(arr) <= 1:
        return arr
    
    left, right = split(arr)
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)


if __name__ == '__main__':
    a = [5, 1, 1, 3, 23, 34, 24]
    print(a)
    print(merge_sort(a))
    print(check(a))
