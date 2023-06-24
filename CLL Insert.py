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
            
    def insert_begining(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=self.head
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=new_node
        else:
            self.tail.next=new_node
            new_node.next=self.head
            
    def insert_position(self,pos,data):
        new_node=Node(data)
        temp=self.head
        for i in range (pos-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
cl=CLL()     
node_1=Node(10)
node_2=Node(20)
node_3=Node(30)
        
cl.head=node_1
cl.tail=node_1
cl.tail.next=cl.head

node_1.next=node_2
cl.tail=node_2
cl.tail.next=cl.head

node_2.next=node_3
cl.tail=node_3
cl.tail.next=cl.head       
cl.insert_begining(40)
cl.insert_end(50)
cl.insert_position(4,35)
cl.display()
