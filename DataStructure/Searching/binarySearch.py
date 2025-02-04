def bin_search(slist, item):
  ''' Non recusive '''
  head = 0
  tail = len(slist) - 1
  found = False

  if len(slist) == 0:
    return False
  
  while head <= tail and not found:
    # print(head, tail, found)
    mid = (head + tail) // 2

    if slist[mid] == item:
      found = True
    elif slist[mid] > item:
      tail = mid
    else:
      head = mid + 1
  
  return found

def bsearch(slist, item):
  ''' Recursion function '''
  if len(slist) == 0:
    return False

  midpoint = len(slist) // 2
  if slist[midpoint] == item:
    return True
  elif slist[midpoint] < item :
    # if item is greater than midpoint then,
    # search item is on the right side
    return bsearch(slist[midpoint+1:], item)
  else:
    # if item is greater than midpoint then,
    # search item is on the left side
    return bsearch(slist[:midpoint], item)

if __name__ == "__main__":
  alist = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18] 
  #location = bsearch(alist,50)
  location = bin_search(alist, 18)
  print(location)
