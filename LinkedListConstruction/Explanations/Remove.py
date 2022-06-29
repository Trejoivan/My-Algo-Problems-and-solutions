


def removeNodesWithValue(self, value):
  node = self.head
  while node is not None:
    nodeToRemove = node
    node = node.next
    if node.value == value:
      self.remove(nodeToRemove)

def remove(self, node):
  if node == self.head:
    self.head = self.head.next
  if node == self.tail:
    self.tail = self.tail.prev
  self.removeNodeBindings(node)
    

def removeNodeBindings(self, node):
  if node.prev is not None:
    node.prev.next = node.next
  if node.next is not None:
    node.next.prev = node.prev
  node.prev = None
  node.next = None

