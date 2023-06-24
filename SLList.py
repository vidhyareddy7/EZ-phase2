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
            
    def Insert_beginning(self,data):
        new_node=Node(data)#creating a new node
        new_node.next=self.head# pointing the new node (next) to the head node
        self.head=new_node #making new node as the head node
    def insert_end(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.next=None
        
        
    def insert_position(self,pos,data):
        new_node=Node(data)
        temp=self.head
        for i in range (pos-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
        
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
SL.Insert_beginning("ram")
SL.insert_end("krishna")
SL.insert_position(3,"shiva")
SL.display()
#print(SL.head.data)