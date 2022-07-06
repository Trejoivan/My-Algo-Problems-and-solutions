
def gridTraversal(m, n):
  if m == 1 and n == 1:
    return 1
  if m == 0 or n == 0:
    return 0
  return gridTraversal(m - 1, n) + gridTraversal(m, n - 1)

print(gridTraversal(3, 3))