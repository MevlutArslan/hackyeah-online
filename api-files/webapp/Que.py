class Node:
    def __init__(self,val : int):
        self.next = None
        self.val = val

    def __str__(self):
        return 'Value is : ' + str(self.val) + ", Next is + " + str(self.next)

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data): 
        new_node = Node(new_data) 
  
        new_node.next = self.head 
  
        self.head = new_node

    def getCount(self): 
        temp = self.head 
        count = 0 

        while (temp): 
            count += 1
            temp = temp.next
        return count

    def getPosition(self, _id : int):
        counter = 1
        temp = self.head
        while(_id != temp.val):
            temp = temp.next
            counter += 1
        return counter

    def shiftQue(self):
        self.head = self.head.next

    def toDict(self):
        return {"head" : self.head}

# que = LinkedList()

# command = input('enter what to do')
# curr = ""
# while(command != "quit"):
#     if(command == "add"):
#         _id = input("id pls : ")
#         if(que.getCount() == 0):
#             que.head = Node(_id)
#             curr = que.head
#         else:
#             while(curr.next != None):
#                 curr = curr.next
#             curr.next = Node(_id)
            
#     command = input('enter what to do')
#     if(command == "get position"):
#         print(que.getPosition(input("enter the id you want to search for")))
    
#     if(command == "shift que"):
#         que.shiftQue()
#         print(que.head)

