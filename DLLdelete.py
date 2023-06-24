class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class Dll:
    def __int__(self):
        self.head=none
        
    def display(self):
        if self.head is None:
            print("DLL IS EMPTY")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<==>",end=" ")
                temp=temp.next
    def delete_begining(self):
        temp=self.head
        self.head=temp.next
        temp.next.prev=None
        temp.next=None
        
        
    def delete_end(self):
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=None
        temp.prev.next=None
        
    def delete_pos(self,pos):
        prev=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
        temp.prev=prev
        
            
node_1= Node("vidhya")
node_2= Node("alekya")
node_3= Node("shiva")
node_1.next=node_2
node_2.prev=node_1
node_2.next=node_3
node_3.prev=node_2

Dl=Dll()
Dl.head=node_1
#Dl.delete_begining()
Dl.delete_pos(2)
#Dl.delete_end()
Dl.display()
