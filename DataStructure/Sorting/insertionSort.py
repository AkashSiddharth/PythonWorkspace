import sys

def insertionSort(arr):
    for i in range(1, len(arr)):
        cur_val = arr[i] 
        position = i

        while position > 0 and arr[position-1] > cur_val:
            arr[position] = arr[position - 1]
            position -= 1
        
        arr[position] = cur_val
    
    return arr

if __name__ == "__main__":
    try:
        if len(sys.argv) == 1:
            raise AttributeError
        
        lst = list(map(int, sys.argv[1:]))
        print(insertionSort(lst))
    except AttributeError as e:
        print(e)