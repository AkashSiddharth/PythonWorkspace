import sys

def mergeSort(arr):
    length = len(arr)
    mid = length // 2
    lefthalf = arr[:mid]
    righthalf = arr[mid:]

    # if the len greater than 1
    if length > 1:
        # Call mergesort on the left half
        mergeSort(lefthalf)

        # Call mergesort on the right half
        mergeSort(righthalf)

        return mergeArrays(arr, lefthalf, righthalf)

def mergeArrays(arr, lefthalf, righthalf):
    i, j, k = [0] * 3
    # Merge the arrays
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            arr[k] = lefthalf[i]
            i += 1
        else:
            arr[k] = righthalf[j]
            j += 1
        k += 1
    
    # Copy the remaining objects in the array
    while i < len(lefthalf):
        arr[k] = lefthalf[i]
        i += 1
        k += 1
    
    while j < len(righthalf):
        arr[k] = righthalf[j]
        j += 1
        k += 1
    return arr
    
# Main
if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise AttributeError("Require more arguments to be passed to sort")
    
    lst = list(map(int, sys.argv[1:]))
    print (mergeSort(lst))
