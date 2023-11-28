class Node:
   def __init__(self, data=None):
      self.data = data
      self.prev = None
      self.next = None

class DLL:
    def __init__ (self):
        self.head = None

    def dll_append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def insert_after(self, target_node, data):
        if target_node is None:
            return
        new_node = Node(data)
        new_node.next = target_node.next
        if target_node.next:
            target_node.next.prev = new_node
        target_node.next = new_node
        new_node.prev = target_node

    def compare(self, compare_target):
        current = self.head
        while current is not None:
            if current.data == compare_target:
                return current
            current = current.next
        return False
        
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