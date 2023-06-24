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
                
                
    def insert_begining(self,data):
        new_node=Node(data)
        temp=self.head
        temp.prev=new_node
        new_node.next=temp
        self.head=new_node
        
        
    def insert_end(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
            if temp.next is None:
                temp.next=new_node
                new_node.prev=temp
            new_node.next=None
            
    def insert_pos(self,pos,data):
        new_node=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        new_node.prev=temp
        new_node.next=temp.next
        temp.next.prev=new_node
        temp.next=new_node
            
node_1= Node("vidhya")
node_2= Node("alekya")
node_3= Node("shiva")
node_1.next=node_2
node_2.prev=node_1
node_2.next=node_3
node_3.prev=node_2

Dl=Dll()
Dl.head=node_1
Dl.insert_begining("srija")
Dl.insert_end("prasad")
Dl.insert_pos(3,"vs")
Dl.display()
