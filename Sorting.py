"""
1. Heap sort
"""
def heapify(data:list, size:int, i:int):
    
    # find the largest between i, and i's childs.
    largest = i
    i_lc = 2*i+1
    i_rc = 2*i+2

    if (i_lc < size and data[i_lc] > data[i]):
        largest = i_lc
    
    if (i_rc < size and data[largest] < data[i_rc]):
        largest = i_rc
    
    # Now that we know the largest of sub-tree, we swap the elements

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, size, largest) # largest is only the index here which would be of either of the child nodes
    

def heap_sort(data:list):

    # build a max heap
    n = len(data)
    for i in range(n//2 - 1, -1, -1):
        heapify(data, n, i) # start from leaf - 1 level and work your way up to build heap tree

    # retrieve the top element and heapify again

    for i in range(n-1, 0, -1):
        data[0], data[i] = data[i], data[0]
        heapify(data, i, 0)

input_array = [3,7,2,1,8,9]
heap_sort(input_array)
print("heap sort:")
for i in input_array:
    print(i)

"""
2. Merge sort
"""

def merge_sort(data:list):
    size = len(data)
    if size <= 1:
        return data

    mid = size // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)

def merge(left_data, right_data):
    merged = []
    i = j = 0
    while i < len(left_data) and j < len(right_data):
        if left_data[i] <= right_data[j]:
            merged.append(left_data[i])
            i = i + 1
        else:
            merged.append(right_data[j])
            j = j + 1

    merged.extend(left_data[i:])
    merged.extend(right_data[j:])
    return merged

input_array = [3,7,2,1,8,9]
output = merge_sort(input_array)
print("merge sort:")
for i in output:
    print(i)

"""
3. Quick sort - you take a random element and recursively put elements smallest than i to the left and vice versa
"""
def partition(data:list, low, high):
    pivot = data[high]
    i = low - 1

    for j in range(low, high):
        if data[j] <= pivot:
            i = i + 1
            data[j], data[i] = data[i], data[j]
    
    data[high], data[i+1] = data[i+1], data[high]
    return i + 1

def quick_sort(data:list, low, high):
    if low < high:
        pivot_array = partition(data, low, high)
        quick_sort(data, low, pivot_array-1)
        quick_sort(data, pivot_array+1, high)

def quick_sort_unoptim(data:list):
    if len(data) <=1 :
        return data
    pivot = data[0]
    less_array = [x for x in data[1:] if x < pivot]
    greater_or_equal = [x for x in data[1:] if x >= pivot]
    return quick_sort_unoptim(less_array) + [pivot] + quick_sort_unoptim(greater_or_equal)

input_array = [3,7,2,1,8,9]
quick_sort(input_array, 0, len(input_array) - 1)
print("quick sort:")
for i in input_array:
    print(i)
"""
4. Distribution sort - bucket implementation
"""


"""
5. Insertion sort - for lists smaller than 32
"""
def insertion_sort(data:list):
     if len(data) <= 1:
         return data
     
     for i in range(1, len(data)):
         key = data[i]
         j = i - 1

         while j >= 0 and key < data[j]:
             data[j+1] = data[j]
             j = j - 1
        
         data[j+1] = key

input_array = [3,7,2,1,8,9]
insertion_sort(input_array)
print("insertion sort:")
for i in input_array:
    print(i)

