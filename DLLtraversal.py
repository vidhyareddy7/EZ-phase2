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
    
node_1= Node("vidhya")
node_2= Node("alekya")
node_3= Node("shiva")
node_1.next=node_2
node_2.prev=node_1
node_2.next=node_3
node_3.prev=node_2

Dl=Dll()
Dl.head=node_1
Dl.display()
