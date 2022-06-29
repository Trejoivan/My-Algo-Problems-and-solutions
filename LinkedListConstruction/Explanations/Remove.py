



def remove(self, node):
  if node == self.head:
    self.head = self.head.next
  if node == self.tail:
    self.tail = self.tail.prev
  self.removeNodeBindings(node)
    