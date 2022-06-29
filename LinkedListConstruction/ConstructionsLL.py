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

  #look into explanations for step by step explanations
  def setHead(self, node):
    if self.head is None:
      self.head = node
      self.tail = node
    self.insertBefore(self.head, node)


  #look into explanations for step by step explanations
  def setTail(self, node):
    if self.tail is None:
      self.setHead(node)
      return
    self.insertAfter(self.tail, node)


  #look into explanations for step by step explanations
  def insertBefore(self, node, nodeToInsert):
    if nodeToInsert == self.head and nodeToInsert == self.tail:
      return
    self.remove(nodeToInsert)
    nodeToInsert.prev = node.prev 
    nodeToInsert.next = node 
    if node.prev is None: 
      self.head = nodeToInsert
    else:
      node.prev.next = nodeToInsert
    node.prev = nodeToInsert

  #look into explanations for step by step explanations
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

  #look into explanations for step by step explanations
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

  #look into explanations for step by step explanations (REMOVE.py)
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

  #look into explanations for step by step explanations (REMOVE.py)
  def removeNodeBindings(self, node):
    if node.prev is not None:
      node.prev.next = node.next
    if node.next is not None:
      node.next.prev = node.prev
    node.prev = None
    node.next = None

