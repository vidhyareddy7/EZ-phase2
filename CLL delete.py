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
    def delete_begining(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.tail.next=self.head
    def delete_end(self):
        if self.head is None:
            print("cll is empty")
        else:
            prev=self.head
            temp1=self.head.next
            while temp1.next != self.head:
                temp1=temp1.next
                prev=prev.next
            temp1.next=None
            self.tail=prev
            self.tail.next=self.head
                
    def delete_pos(self,pos):
        prev=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next     
        
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
#cl.delete_begining()
#cl.delete_end()
cl.delete_pos(1)
cl.display()