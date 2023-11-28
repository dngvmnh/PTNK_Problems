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
   
   def swap_node(self,node_x,node_y):
      if node_x == node_y :
         return
      
      prev_x = None
      current_x = self.head

      while current_x is not None and current_x.data != node_x:
         prev_x = current_x
         current_x = current_x.next

      prev_y = None
      current_y = self.head

      while current_y is not None and current_y.data != node_y:
         prev_y = current_y
         current_y = current_y.next

      if current_x == None or current_y == None:
         return

      if prev_x is not None:
         prev_x.next = current_y
      else :
         self.head = current_y

      if prev_y is not None:
         prev_y.next = current_x
      else :
         self.head = current_x

      temp = current_x .next
      current_x.next = current_y.next
      current_y.next = temp

   def bubble_sort(self):
      count = 0
      start = self.head 
      while start != None: 
         count+= 1
         start = start.next

      # for i in range(0, count): 
      sorted = False 

      while not sorted :
         sorted = True
         
         list_node = self.head
 
         while list_node is not None :
            next_node = list_node.next
            if next_node is not None :
               if list_node.data < next_node.data:
                  self.swap_node(list_node.data, next_node.data)
                  sorted = False
            list_node = list_node.next
         
               


   
      
   








