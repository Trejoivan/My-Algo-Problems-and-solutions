 
 
# Big 0 = time: O(1); space O(1)

def setHead(self, node):
  # if the LL is empty the below will check and then set the head and tail to the given node
  if self.head is None:
    self.head = node
    self.tail = node

  #Look at "Explanations/inserBefore" to understand what the below function is doing
  self.insertBefore(self.head, node)
