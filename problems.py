"""detecting loop in a CLL
you r given a CLL,but you suspect that it might contain a loop.
a loop occours when a node next pointer points to a node that has been visted before in the traversal
detect whether it is in loop or not"""


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class CLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        if self.head is None:
            print("CLL is empty,add ele")
        else:
            temp=self.head
            print(temp.data,"-->",end=" ")
            while temp.next!=self.head:
                temp=temp.next
                print(temp.data,"-->",end=" ")
            print(temp.next.data)
    def detect_loop(self):
        if self.tail.next==self.head:
            print("loop exists")
        else:
            print("loop don't exits")
cl=CLL()     
node_1=Node(1)
node_2=Node(2)
node_3=Node(3)
node_4=Node(4)

cl.head=node_1
cl.tail=node_1
cl.tail.next=cl.head

node_1.next=node_2
cl.tail=node_2
cl.tail.next=cl.head

node_2.next=node_3
cl.tail=node_3
cl.tail.next=cl.head

node_3.next=node_4
cl.tail=node_4
cl.tail.next=cl.head

cl.detect_loop()
cl.display()
