


# Big 0 = time: O(1); space O(1)
def setTail(self, node):
  #just likst setHead we will create a use-case check for an empty LL 
  if self.tail is None:
    #calling our setHead function to set the tail and head of an empty LL
    self.setHead(node)
    return
  
  # calling our insertAfter to our .tail since after our tail will be pushed back. Look at instertAfter for step-by-step instructions.
  self.insertAfter(self.tail, node)
