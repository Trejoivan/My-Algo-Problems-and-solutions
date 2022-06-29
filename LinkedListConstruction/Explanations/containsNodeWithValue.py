
def containsNodeWithValue(self, value):
  # cread a variable that will hold the current node value aka the "head"
  node = self.head

  #create a while loop that will iterate over the entire Linked List until it reaches None , after the "tail"
  # OR when the value is found
  while node is not None and node != value:
    node = node.next

  # will return True if the value is found aka node == value , and will return False otherwise
  return node is not None