def probe(alist: list, ind: int) -> int:
  """ Probes each index frpm current position till the end to find empty pos
      in the list, if no empty index is found, it wrpas aroud and searches
      from start to the current position. """
  empty = False
  
  while ind < len(alist) and not empty:
    if alist[ind] == None:
      print("Empty found:", ind)
      return ind
    ind += 1
  
  for i, val in enumerate(alist[:ind]):
    if val == None:
      print("Empty found:", ind)
      return i

def hash(alist: list, num: int) -> int:
  """ Hash function to calculate index and store the number."""
  index = num % len(alist)

  if alist[index] != None:
    print("index is full, probing...")
    index = probe(alist, index)
  
  alist[index] = num
  return index

if __name__ == "__main__":
  input_l = 113, 117, 97, 100, 114, 108, 116, 105, 99

  store = [None] * len(input_l)
  print(input_l)
  for n in input_l:
    location = hash(store, n)
    print(location)
  
  print(store)

