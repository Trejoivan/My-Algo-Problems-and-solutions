



def insertAfter(self, node, nodeToInsert):
  if nodeToInsert == self.head and nodeToInsert == self.tail:
    return
  self.remove(nodeToInsert)
  nodeToInsert.prev = node
  nodeToInsert.next = node.next
  if node.next is None:
    self.tail = nodeToInsert
  else:
    node.next.prev = nodeToInsert
  node.next = nodeToInsert