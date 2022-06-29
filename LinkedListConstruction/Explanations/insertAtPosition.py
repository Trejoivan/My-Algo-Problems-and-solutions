



def insertAtPosition(self, position, nodeToInsert):
  if position == 1:
    self.setHead(nodeToInsert)
    return
  node = self.head
  currentPosition = 1
  while node is not None and currentPosition != position:
    node = node.next
    currentPosition += 1
  if node is not None:
    self.insertBefore(node, nodeToInsert)
  else:
    self.setTail(nodeToInsert)