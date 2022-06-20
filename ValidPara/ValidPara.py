#Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

#Examples
#"()"              =>  true
#")(()))"          =>  false
#"("               =>  false
#"(())((()())())"  =>  true
#Constraints
#0 <= input.length <= 100

#Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).

# if str is empty or doesnt contain () : return True, if str starts with ) , or str ends with ( return False

# special cases 1. filterstr len string is == 1: return False: 2. if filteredempty len == 0 : return True, 
# for every opening para , must have a closing. 

# (()())
# 0

# counter of opening, and increment as I find opening, and then decrement as I find closing, if counter is not 0, return False, else return True 


def validParantheses(str):
  fStr = ''
  isOpen = 0
  #step filter str
 
  for i in str: 
    if i == '(' or i == ')':
      fStr += i 

  if len(fStr) == 1:
    return False
    
  elif len(fStr) == 0:
    return True
      
  if fStr[0] == ')' or fStr[-1] == '(':
    return False

  
  for j in fStr:
    if j == '(':
      isOpen += 1
      
    elif j == ')' and isOpen == 0:
      return False
      
    else:
      isOpen -= 1

  return isOpen == 0
  

print(validParantheses("()))))((((()"))

