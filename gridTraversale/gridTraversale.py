
# def gridTraversal(m, n, memo={}):

#   if m == 1 and n == 1:
#     return 1
#   if m == 0 or n == 0:
#     return 0
#   return gridTraversal(m - 1, n, memo) + gridTraversal(m, n - 1, memo)

# print(gridTraversal(40,40))


# def findBadPair(sequence):
#   for i in range(len(sequence)):
#     if sequence[i] >= sequence[i + 1]:
#       return i

#     return -1

# def solution(sequence):
#   j = findBadPair(sequence)
  
#   if j == -1:
#     return True

#   if findBadPair(sequence[j - 1:j] + sequence[j + 1:]) == -1:
#     return True

#   if findBadPair(sequence[j:j+1] + sequence[j + 2:]) == -1:
#     return True

#   return False



    
# print(solution([1, 3, 2]))


# def solution(matrix):
#     col = len(matrix[0]) - 1
#     idxWithGhosts = []
#     runningSum = 0
    
#     for i in range(len(matrix)):
#         for j in range(col + 1):
#             if matrix[i][j] == 0:
#                 if j not in idxWithGhosts:
#                     idxWithGhosts.append(j)
#             if j not in idxWithGhosts:
#                 runningSum += matrix[i][j]
#     return runningSum
    
# solution([[0, 1, 1, 2], 
#           [0, 5, 0, 0], 
#           [2, 0, 3, 3]])

# def solution(inputArray):
#     arrayDict = {}
#     maxLength = 0
    
#     for i in inputArray:
#         lengthArr = len(list(i))

#         if lengthArr in arrayDict:
#             arrayDict[lengthArr].append(i)
#         else:
#             maxLength = max(maxLength, lengthArr)
#             arrayDict[lengthArr] = [i]
            
#     return arrayDict[maxLength]

# print(solution(["aba", 
#  "aa", 
#  "ad", 
#  "vcd", 
#  "aba"]))


# def solution(s1, s2):
#     valueCommon = 0
#     s1Dict = createDict(s1)
#     s2Dict = createDict(s2)

#     for i in s1Dict.keys():
#       if i in s2Dict:
#         valueCommon += min(s1Dict[i], s2Dict[i])
#     return valueCommon

# def createDict(strings):
#     Sdict = {}
#     for i in strings:
#         if i in Sdict:
#             Sdict[i] += 1
#         else:
#             Sdict[i] = 1
#     return Sdict

# print(solution('aabcc', 'adcaa'))

# def solution(numbers):
#     arr = []
#     for i in range(1, len(numbers) - 1):
#         isZigZag = isZig(numbers, i)
#         if isZigZag == True:
#             arr.append(1)
#         else:
#             arr.append(0)

#     return arr

# def isZig(arr, idx):
#     if arr[idx] > arr[idx - 1]:
#         if arr[idx + 1] < arr[idx]:
#             return True

#     elif arr[idx] < arr[idx - 1]:
#          if arr[idx + 1] > arr[idx]:
#             return True
#     return False
    
# print(solution([1, 2, 1, 3, 4]))

# from cProfile import run

def solution(n, a):
    result = [0 for num in range(len(a))]
    
    if len(a) == 1:
        return a
        
    if len(a) == 2:
        result[0] = a[0] + a[1]
        result[1] = a[0] + a[1]
        
    for idx, i in enumerate(a):
        
        if idx > 0 and idx < len(a) - 1:
            result[idx] += a[idx - 1] + a[idx] + a[idx + 1]
            
        elif idx == len(a) - 1:
            result[idx] = a[idx] + a[idx - 1]

        else:
            result[idx] = a[idx + 1] + a[idx]
            
    return result


# def solution(a):
#     valueDict = {}
    
#     for i in range(len(a) + 2):
#         valueDict[2 ** i] = 1
        
#     result = 0
    
#     if len(a) == 2:
#         if a[0] in valueDict:
#             result += 1
        
#     for i in range(len(a)):
#         for j in range(i , len(a)):
#             runningSum = a[i] + a[j]
#             if runningSum in valueDict:
            
#                 result += 1
            
#     return result


# print(solution([1, -1, 2, 3]))  #should be 5
# print(solution([2]))  #should be 1

# def findMaxIdx(inputString):
#   char = list(inputString)
#   openBracket = []
#   for idx,c in enumerate(char):
#     if c == '(':
#       openBracket.append(idx)
#     elif c == ')':
#       idxTopop = openBracket.pop()
#       char[idxTopop:idx] = char[idx:idxTopop:-1]
#   return ''.join(c for c in char if c not in '()')



def solution(numbers):
    swapped = False 
    
    for i in range(1, len(numbers)):
        prev = numbers[i - 1]
        
        if prev >= numbers[i]:
            
            if swapped == True:
                return False
            
            newNum = swapNum(prev)   #9
            
            if numbers[i] <= newNum:  # 10 >= 9
                return False
                
            else:
                numbers[i] = newNum
                swapped = True
        
    return True
                
            
            

def swapNum(number):
    stringNum = str(number)
    listNum = list(stringNum)
    
    end = len(listNum) - 1
    
    while listNum[end] == 0:
        end -= 1
    
    newNum = listNum[:end - 1]
    
    return int(''.join(newNum))



# print(findMaxIdx("foo(bar(baz))blim"))

# def solution(pictures):
#   n = len(pictures)
#   pictures.reverse()
#   for r in range(n):
#     for c in range(r):
#       pictures[r][c], pictures[c][r] = pictures[c][r], pictures[r][c]
#   return pictures


# print(solution([[1, 2, 3],[4, 5, 6], [7, 8, 9]]))

# def solution(image):
#     answer = []
#     startCol = 0
#     startRow = 0
#     holder =[]
#     while startCol < len(image[0]) - 2 and startRow < len(image) - 2:
#         colSum = 0
       
#         for i in range(3):
#             for j in range(3):
#                 colSum += image[startRow + i][startCol + j]

#         holder.append(colSum // 9)
        
#         if startCol == len(image[0]) - 3:
#             answer.append(holder)
#             holder =[]
#             if startRow == len(image) - 3:
#                 startCol += 1
#                 startRow = 0
#                 print('not here')
#             else:
#                 print('here')
#                 startRow += 1
                
#                 startCol = 0
            
#         else:
#             startCol += 1
        
            
#     return answer

# print(solution([[7,4,0,1], 
#  [5,6,2,2], 
#  [6,10,7,8], 
#  [1,4,2,0]]))

# def solution(a2b, b2a, trips):
#     time = min(a2b) + 100
#     pos = 0
#     flights = 1
    
#     while trips > 0:
#         if flights == 1:
#             if b2a[pos] < time:
#                 pos += 1
#             time += b2a[pos] + 100
#             flights = 0
#             trips -= 1
            
#         else:
#             if a2b[pos] < time:
#                 pos += 1
#             print('time', time)
#             time += a2b[pos] + 100
#             flights = 1
            
            
#     return time - 100

# print(solution( [0, 200, 500], [99, 210, 450], 1))


# You are given a string s. Consider the following algorithm applied to this string:

# Take all the prefixes of the string, and choose the longest palindrome between them.
# If this chosen prefix contains at least two characters, cut this prefix from s and go back to the first step with the updated string. Otherwise, end the algorithm with the current string s as a result.
# Your task is to implement the above algorithm and return its result when applied to string s.

# Note: you can click on the prefixes and palindrome words to see the definition of the terms if you're not familiar with them.

# Example

# For s = "aaacodedoc", the output should be solution(s) = "".

# The initial string s = "aaacodedoc" contains only three prefixes which are also palindromes - "a", "aa", "aaa". The longest one between them is "aaa", so we cut if from s.
# Now we have string "codedoc". It contains two prefixes which are also palindromes - "c" and "codedoc". The longest one between them is "codedoc", so we cut if from the current string and obtain the empty string.
# Finally the algorithm ends on the empty string, so the answer is "".
# For s = "codesignal", the output should be solution(s) = "codesignal".
# The initial string s = "codesignal" contains the only prefix, which is also palindrome - "c". This prefix is the longest, but doesn't contain two characters, so the algorithm ends with string "codesignal" as a result.

# For s = "", the output should be solution(s) = "".

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string s

# A string consisting of English lowercase letters.

# def mineSweeper(matrix):
#   result = []
#   for _ in range(len(matrix)):
#     result.append([])
#   for i in range(len(matrix)):

#     for j in range(len(matrix[0])):
#       result[i].append(countBombsSurrounding([i, j], matrix))

# def countBombsSurrounding(arr, matrix):
#   bombs = 0
#   deepBorder = len(matrix) - 1
#   wideBorder = len(matrix[0]) - 1

#   deepLow = roundToBorder(coordi[0], deepBorder)

# def roundToBorder(num , border):
  
#   if num < 0:
#     return 0

#   if num > border:
#     return border

#   return num


index = "abcdefghijklmnopqrstuvwxyz".index('r')
print('efghijklmnopqrstuvwxyzabcd'[index])