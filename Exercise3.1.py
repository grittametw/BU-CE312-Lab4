class List():
    def __init__(self):
        self.Header = ""
        
class Node():
    def __init__(self,Value):
        self.Value = Value
        self.Next = ""

List_A = List()
Node_1 = Node(44)
List_A.Header = Node_1
Node_2 = Node(36)
Node_1.Next = Node_2
Node_3 = Node(90)
Node_2.Next = Node_3
Node_4 = Node(10)
Node_3.Next = Node_4
Node_5 = Node(60)
Node_4.Next = Node_5
Node_6 = Node(99)
Node_5.Next = Node_6