queue=[]
def enqueue_element():
    if len(queue)==n:
        print("queue is full")
    else:
        ele=int(input("enter the element:"))
        queue.append(ele)
        print(queue)
    
    
def dequeue_element():
    if not queue:
        print("Q is empty,add the elements")
    else:
        p=queue.pop(0)
        print("the element reomved is:",p)
        print(queue)
        
        
n=int(input("enter the size of queue:"))
while True:
    print("select the operation 1.Enqueue 2.Dequeue 3.quit")
    choice = int(input())
    if choice==1:
        enqueue_element()
    elif choice==2:
        dequeue_element()
    elif choice==3:
        break
    else:
        print("Enter the correct operation:")