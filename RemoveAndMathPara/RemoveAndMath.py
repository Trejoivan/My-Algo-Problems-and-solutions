# Given a formula with letters and parentheses, remove parentheses
# also do the mathematical formula for the letters given

# a-(a-b) -> b -> a-a+b -> b


def removeAndMath(str):
  filtered = ''
  for i in str:
    if i != '(' and i != ')':
      filtered += i
  
  return list(filtered)

print(removeAndMath('a-(a-b)'))