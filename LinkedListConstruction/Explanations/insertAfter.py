



def insertAfter(self, node, nodeToInsert):
  #goind to check for an empty LL
  if nodeToInsert == self.head and nodeToInsert == self.tail:
    return
  self.remove(nodeToInsert)
  
  nodeToInsert.prev = node
  nodeToInsert.next = node.next
  
  # checks to see if the node is the tail of the LL
  if node.next is None:
    self.tail = nodeToInsert
  else:
    node.next.prev = nodeToInsert
  node.next = nodeToInsert
