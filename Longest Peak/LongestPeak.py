

def LongestPeak(array):
  #Variable that will keep track of longestPeak 
  longestPeak = 0

  #start i at one so that you can retrack your i value and check before and after
  i = 1

  #while loop to loop through starting at index 1 from above and stops before the end of the array

  while i < len(array) - 1:
    #isPeak will check for a peak by looking at the previous i value and the next i value
    isPeak = array[i -1] < array[i] and array[i] > array[i + 1]

    #if no peak is found , the i in incremented and the search is continued
    if not isPeak:
        i += 1
        continue
    
    #if peak is found , two pointers are created, on on prev and on on next

    leftIdx = i - 2
    #while loop to find all values decreasing ensuring not to reach below 0
    while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
        leftIdx -= 1
        
    
    rightIdx = i + 2
    #while loop to catch all increasing values from i 
    while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
        rightIdx += 1

    #simple subtraction to give currentPeaklength
    currentPeaklen = rightIdx - leftIdx - 1

    #max to return only the largest value 
    longestPeak = max(longestPeak, currentPeaklen)

    #i becomes rightIdx to start from where the last peak left off
    i = rightIdx

  
  return longestPeak


print('test 1')
print(LongestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5 , -1, -3, 2, 3]) == 6)