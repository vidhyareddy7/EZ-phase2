def Insert_beginning(self,data):
    new_node=Node(data)#creating a new node
    new_node.next=self.head# pointing the new node (next) to the head node
    self.head=new_node #making new node as the head node


def insert_end(self,data):
    new_node=Node(data)
    temp=temp.next
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
    