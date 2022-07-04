def arrayOfProducts(array):
  # exempt is the variable that will be exempt from the compounding of integers
  exempt = 0
  # answer will hold all values
  answer = []

  while exempt < len(array):
    #runnning sum will 'refresh with each while loop' 
    runningSum = 1
      
    for idx, i in enumerate(array):
      #if the idx of the loop is the exempt, continue to the next loop
      if idx == exempt:
          continue
      #begin compounding the values
      else:
          runningSum *= i 
     
    #add the values to the answer array and also increase the exempted value
    answer.append(runningSum)
    exempt += 1

  return answer

#BIG O EVal
#Time = O(n2)
#space = O(n)
