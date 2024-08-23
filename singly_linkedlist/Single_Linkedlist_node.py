class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.temp = None
    
    def creation(self):
        num = int(input("Enter the no of nodes"))
        for i in range(num):
            data = int(input("Enter the data for nodes"))
            newnode = Node(data)
            if self.head is None:
                self.head=newnode
                self.temp = newnode
            else:
                self.temp.next = newnode
                self.temp = newnode
   

    def display(self):
        self.temp = self.head
        while self.temp is not None:
            print(self.temp.data,end = "->")
            self.temp = self.temp.next

    def insertionATbeg(self):
        data=int(input("enter data to insert"))
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode


    def insertATlast(self):
        self.temp = self.head
        data=int(input("enter data to insert at last "))
        newnode=Node(data)
        while(self.temp.next is not None):
            self.temp = self.temp.next
        self.temp.next = newnode
    
    def insertATmid(self):
        self.temp = self.head
        pos = int(input("Enter the position to add"))
        data=int(input("enter data to insert at middle"))
        newnode=Node(data)
        for i in range(pos-1):
            prev = self.temp
            self.temp = self.temp.next
        newnode.next = self.temp
        prev.next = newnode
    
    def deleAtbeg(self):
        self.temp = self.head
        self.head = self.temp.next 

    def deleAtend(self):
        self.temp = self.head
        while self.temp.next is not None:
            prev = self.temp
            self.temp = self.temp.next 
        prev.next = None 
    
    def deleAtmid(self):
        n = int(input("Enter the position to delete node:"))
        self.temp = self.head
        for i in range(n-1):
            prev = self.temp
            self.temp = self.temp.next 
        prev.next = self.temp.next
        
    
  




    



linkedlist=SLL()

linkedlist.creation()

# linkedlist.insertionATbeg()
# linkedlist.insertATlast()
# linkedlist.insertATmid()
# linkedlist.deleATstart()
linkedlist.display()
print()
# linkedlist.deleAtbeg()
# linkedlist.deleAtend()
linkedlist.deleAtmid()
linkedlist.display()

