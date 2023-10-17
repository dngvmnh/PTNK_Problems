class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self, seq=None):
        self.head = None 
        if seq is not None:
            for val in reversed(seq):
                self.head = Node(val, self.head)

   def print_list(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         # print("\n")
         printval = printval.nextval

   def ins_at_begining(self,newdata):
      NewNode = Node(newdata)

      NewNode.nextval = self.headval
      self.headval = NewNode

   def ins_at_end(self, newdata):
      NewNode = Node(newdata)
      if self.headval is None:
         self.headval = NewNode
         return
      laste = self.headval
      while(laste.nextval):
         laste = laste.nextval
      laste.nextval=NewNode



e_list = [1,2,3,4,5,6,7,8,9]
demo_list = SLinkedList()
node = Node(e_list[0])
demo_list = node
for val in e_list[1:]:
    node.nextval = Node(val)
    node = node.nextval
# demo_list.headval = Node("one")

# demo_list.headval.nextval = e_list[0]

# for i in range(0,8) :
   
#    e_list[i].nextval = e_list[i+1]



# demo_list.ins_at_end("qwerty")
demo_list.print_list()

# e1 = Node("one")
# e2 = Node("two")
# e3 = Node("three")
# demo_list = SLinkedList()
# demo_list.headval = e1
# e1.nextval = e2
# e2.nextval = e3
# demo_list.print_list()

