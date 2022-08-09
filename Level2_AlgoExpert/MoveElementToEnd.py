print("Move Element to End")

def moveElementToEnd(array, toMove):
  count = 0
  while toMove in array:
    array.remove(toMove)
    count = count + 1
  array.extend([toMove]*count)
  return array 

array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
print(f"original array: {array}")
result = moveElementToEnd(array, toMove)
print(f"result: {result}")