

def setTail(self, node):
  if self.tail is None:
    self.setHead(node)
    return
  self.insertAfter(self.tail, node)
