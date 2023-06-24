class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class Dll:
    def __int__(self):
        self.head=none
node_1= Node("vidhya")
node_2= Node("alekya")
node_3= Node("shiva")
#node_4= Node("sai")
#node_5= Node("ram")
node_1.next=node_2
node_2.prev=node_1
#print(node_1)
#print(node_1.next)
node_2.next=node_3
node_3.prev=node_2
#print(node_2)
#print(node_2.next)
#node_3.next=node_4
#node_4.prev=node_3
"""print(node_3)
print(node_3.next)
node_4.next=node_5
node_5.prev=node_4
print(node_4)
print(node_4.next)
print(node_5)
print(node_5.prev)"""
Dl=Dll()
Dl.head=node_1
"""print(node_1)#prints adress of node1
print(node_1.data)#prints vidhya
print(node_1.next)"""
#print(Dl.head)
#print(Dl.head.data)
