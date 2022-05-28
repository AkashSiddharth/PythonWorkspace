from turtle import position


def insertionSort(alist: list) -> list:
  """ Insertion Sort maintains a sorted sublist, gradually increases it by
      inserting elements at the correct place in each iteration."""

  for sub_size in range(1,len(alist)):
    # Nex index to insert in the sub list
    current_val = alist[sub_size]
    cur_pos = sub_size

    while cur_pos > 0 and alist[cur_pos - 1] > current_val:
      alist[cur_pos], alist[cur_pos - 1] = alist[cur_pos - 1], alist[cur_pos]
      cur_pos -= 1
  
  return alist

if __name__ == "__main__":
  alist = [15, 5, 4, 18, 12, 19, 14, 10, 8, 20]
  print(insertionSort(alist))