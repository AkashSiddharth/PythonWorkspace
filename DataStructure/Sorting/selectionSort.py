def selectionSort(arr):
    arr_len = len(arr)
    for fill_here in range(arr_len-1,0,-1):
        max_location = 0
        for j in range(1, fill_here + 1):
            if arr[j] > arr[max_location]:
                max_location = j
        
        temp = arr[fill_here]
        arr[fill_here] = arr[max_location]
        arr[max_location] = temp

    return arr

    
if __name__ == "__main__":
    l = [6,2,43,7,9,5,57,4,35]
    print(selectionSort(l))