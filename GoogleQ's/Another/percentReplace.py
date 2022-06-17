import re
#import necessary libraries

def replacepercent(str, rep1, rep2 ):

  str = re.sub(f'%555%', rep1,  str)

  str = re.sub(f'%123%', rep2,  str)
  
  return str


print(replacepercent('*$%JB%jb%UX%789', 'UX', 'JB'))