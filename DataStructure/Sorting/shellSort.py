import sys

def shellSort(arr):
    sublist = len(arr) // 2
    while sublist > 0:
        for start in range(sublist):
            gapInsertionSort(arr, start, sublist)
        
        print("After increments of size",sublist, "The list is",arr)
        
        sublist = sublist // 2

def gapInsertionSort(arr, start, gap):
    for i in range(start+gap, len(arr), gap):
        cur_val = arr[i]
        pos = i

        while pos >= gap and arr[pos - gap] > cur_val:
            arr[pos] = arr[pos- gap]
            pos = pos - gap

        arr[pos] = cur_val

# Main
if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise AttributeError("Require more arguments to be passed to sort")
    
    lst = list(map(int, sys.argv[1:]))
    print (shellSort(lst))