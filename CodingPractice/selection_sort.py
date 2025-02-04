def selectionSort(alist: list) -> list:
  """ Selection sort algorithm"""
  # Outer loop to control the peak value of iteration
  for list_size in range(len(alist) -1, 0, -1):
    """ As selection sort makes only one exchange per iteration, so reduce the
        size by one, every iteration"""
    max_value_index = 0
    for index in range(list_size + 1):
      """ From 0 to current unsorted list size, extract the index with max value"""
      if alist[index] > alist[max_value_index]:
        max_value_index = index
    
    alist[list_size], alist[max_value_index] = alist[max_value_index], alist[list_size]
  
  return alist

if __name__ == "__main__":
  tlist = [54,26,93,17,77,31,44,55,20]
  print(selectionSort(tlist))
