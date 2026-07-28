arr = [4,1,7,6,3,2,8]

def quickSort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        p_index = partition(arr, low, high)
        # Recursively sort elements before and after partition
        quickSort(arr, low, p_index - 1)
        quickSort(arr, p_index + 1, high)
        
def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while i <= high - 1 and arr[i] <= pivot:
            i += 1
        while j >= low + 1 and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[low], arr[j] = arr[j], arr[low]
    return j

quickSort(arr,0,len(arr)-1)     
print(arr)       