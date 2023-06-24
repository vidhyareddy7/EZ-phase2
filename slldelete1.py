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
    def delete_begining(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        
    def delete_end(self):
        prev=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        
    def delete_pos(self,pos):
        prev=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        
node_1=Node("vidhya")
SL=SLL()
SL.head=node_1
node_2=Node("srija")
node_3=Node("alekya")
node_1.next=node_2
node_2.next=node_3
#SL.delete_begining()
#SL.delete_end()
SL.delete_pos(2)
SL.display()