def delete_begining(self):
    temp=self.head
    self.head=temp.next
    temp.next=None
#obj.delete_begining()
  
  

def delete_end(self):
    prev=self.head
    temp=self.head.next
    while temp.next is not None:
        temp=temp.next
        prev=prev.next
    prev.next=None
#obj.delete_end()
    
    
def delete_pos(self,pos):
    prev=self.head
    temp=self.head.next
    for i in range(1,pos-1):
        temp=temp.next
        prev=prev.next
    prev.next=temp.next