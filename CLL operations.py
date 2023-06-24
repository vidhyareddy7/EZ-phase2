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
    def loop_exists(self):
        if self.head is not None:
            print("loop exists")
        else:
            print("loop doesn't exixts")
    def delete_begining(self):
        if self.head is None:
            print("cll is not existing")
        else:  
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
        
        
    def length_of_list(self):
        if self.head is None:
            return 0
        count = 0
        temp=self.head
        while temp:
            count +=1
            temp=temp.next
            if temp==self.head:
                break
        return count
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
# cl.delete_end()
print(cl.length_of_list())
cl.loop_exists()
cl.display()    