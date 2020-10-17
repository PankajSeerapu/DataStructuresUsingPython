class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#Linked List Class Creation

class LinkedList:
    def __init__(self):
        self.head = None
#The Method Append is used to add New Node to the End of the Linked List
    def Append(self,data):
        NewNode = Node(data)
        if self.head == None: #if Head is None Make Head as New Node
            self.head = NewNode
        else:
            temp = self.head
            while temp.next:    #Traverse till the end of the Linked List and Add New Node
                temp = temp.next

            temp.next = NewNode

#The Method Push is used to add New Node to the Beginning of the Linked List
    def Push(self,data):
        NewNode = Node(data)
        if self.head == None:  #if Head is None Make Head as New Node
            self.head = NewNode
        else:
            NewNode.next = self.head
            self.head = NewNode

#The Method InsertAfter is used to add New Node after a Node with Given Data is Found
    def InsertAfter(self, NodeData , Data):
        prevNode = self.head
        nextNode = self.head
        NewNode = Node(Data)
        if self.head == None:
            print("This Method cannot be used if the Given Linked List is Empty")
            return
        else:
            while prevNode != None:
                if prevNode.data == NodeData:
                    nextNode = prevNode.next
                    NewNode.next = nextNode
                    prevNode.next = NewNode
                    return
                else:
                    prevNode = prevNode.next
            if prevNode == None:
                print("The Node with the Given Data was not Found")
        return

#The Method Display is used to Display the Created Linked List
    def Display(self):
        temp = self.head
        while temp:
            print("{0}->".format(temp.data),end='')
            temp = temp.next


if __name__ == '__main__':
    L1 = LinkedList()
    L1.InsertAfter(10,6)
    L1.Append(5)
    L1.Append(10)
    L1.Append(12)
    L1.Push(14);
    L1.Push(20);
    L1.InsertAfter(12,24)
    L1.InsertAfter(20,18)
    L1.InsertAfter(5,9)
    L1.InsertAfter(78,16)
    L1.Display()




