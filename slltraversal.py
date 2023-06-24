class Node:
    def __init__(self,data):
        self.data=data
        self.next= None
        
class SLL:
    def __init__(self):
        self.head= None
    def display(self):
        if self.head is None:
            print("empty list")
        else:
            temp=self.head
        while temp:
            print(temp.data,"-->",end=" ")
            temp=temp.next
node_1=Node("vidhya")
SL=SLL()
SL.head=node_1
node_2=Node("reddy")
node_3=Node("alekya")
node_1.next=node_2
node_2.next=node_3
#print(node_1.next)
#print(node_2.next)
#print(node_3.next)