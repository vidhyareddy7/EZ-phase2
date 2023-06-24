stack=[]
def push_element():
    if len(stack)==n:
        print("stack is full")
    else:
        element=int(input("enter an element:"))
        stack.append(element)
        print(stack)
    
def pop_element():
    if not stack:
        print("stack is empty,add the elements")
    else:
        p=stack.pop()
        print("removed the element:",p)
        print(stack)
n=int(input("enter the size of stack:"))       
while True:
    print("select the operation 1.push 2.pop 3.quit")
    choice = int(input())
    if choice==1:
        push_element()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("Enter the correct operation:")
        