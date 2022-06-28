
def twosum(array, sum):
  tracker = {}
  for i in range(0, len(array)):
    whatdoineedthere = sum - array[i]
    if whatdoineedthere in tracker:
      return [i, tracker[whatdoineedthere]]
    else:
      tracker[array[i]] = i
  return False 

print(twosum([1, 2, 3, 4], 6))

