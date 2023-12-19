class Node():
    def __init__(self,Value):
        self.Value = Value
        self.Next = ""
        
class LinkedList():
    
    def __init__(self):
        self.Header = ""
        
    def list_append(self,value):
        if self.Header != "":
            self = self.Header
        while self.Next != "" :
            self = self.Next
        self.Next = Node

List_A = LinkedList()

Node_1 = Node(44)
List_A.Next = (Node_1)
Node_2 = Node(36)
Node_1.Next = (Node_2)
Node_3 = Node(90)
Node_2.Next = (Node_3)
Node_4 = Node(10)
Node_3.Next = (Node_4)
Node_5 = Node(60)
Node_4.Next = (Node_5)
Node_6 = Node(99)
Node_5.Next = (Node_6)

#Insert
Node_7 = Node(104)
Node_7.Next = (Node_1)
List_A.Next = Node_7

#Append
Node_8 = Node(57)
Node_6.Next = (Node_8)

#Remove
Node_3.Next = (Node_5)
Node_4.Next = ()