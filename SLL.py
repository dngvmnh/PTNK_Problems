class Node:
   def __init__(self, data=None):
      self.data = data
      self.prev = None
      self.next = None

class SLL:
   def __init__(self, seq=None):
      self.head = None 
      if seq is not None:
            for val in seq:
               self.insert_end(val)

   def sll_append(self, data):
      element = Node(data)
      current_node = self.head
      if current_node is None:
         current_node.next = element
      else :
         while current_node.next :
            current_node = current_node.next
         current_node.next = element

   def print_list(self):
      current = self.head
      while current:
            print(current.data, end=" -> ")
            current = current.next
      print("None")

   def insert_begining(self, newdata):
      NewNode = Node(newdata)

      NewNode.next = self.head
      self.head = NewNode

   def insert_end(self, newdata):
      NewNode = Node(newdata)
      if self.head is None:
         self.head = NewNode
         return
      last_e = self.head
      while(last_e.next):
         last_e = last_e.next
      last_e.next=NewNode

   def insert_after(self,middle_node,newdata):
      if middle_node is None:
         return

      NewNode = Node(newdata)
      NewNode.next = middle_node.next
      middle_node.next = NewNode

   def compare(self, compare_target):
      current = self.head
      while current is not None:
         if current.data == compare_target:
               return current
         current = current.next
      return False
   

   
      
   








