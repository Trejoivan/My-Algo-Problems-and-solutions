# This is an input class. Do not edit.
class Node:
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def setHead(self, node):
    if self.head is None:
      self.head = node
      self.tail = node
    self.insertBefore(self.head, node)

  def setTail(self, node):
      pass

  def insertBefore(self, node, nodeToInsert):
      pass

  def insertAfter(self, node, nodeToInsert):
      pass

  def insertAtPosition(self, position, nodeToInsert):
      pass

  #look into explanations for step by step explanations
  def removeNodesWithValue(self, value):
    node = self.head
    while node is not None:
      nodeToRemove = node
      node = node.next
      if node.value == value:
        self.remove(nodeToRemove)

  #look into explanations for step by step explanations
  def remove(self, node):
    if node == self.head:
      self.head = self.head.next
    if node == self.tail:
      self.tail = self.tail.prev
    self.removeNodeBindings(node)
      

  #look into explanations for step by step explanations
  def containsNodeWithValue(self, value):
    node = self.head
    while node is not None and node != value:
      node = node.next
    return node is not None

  def removeNodeBindings(self, node):
    if node.prev is not None:
      node.prev.next = node.next
    if node.next is not None:
      node.next.prev = node.prev
    node.prev = None
    node.next = None

