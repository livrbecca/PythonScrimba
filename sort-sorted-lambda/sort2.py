def find_smallest_int(arr):
    arr.sort()
    print(arr)

find_smallest_int([34, 15, 88, 2])

def find_smallest_int1(arr):
    arr.sort()
    return arr[0]