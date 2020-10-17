class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#Linked List Class Creation

class LinkedList:
    def __init__(self):
        self.head = None

    def Push(self,data):
        NewNode = Node(data)
        if self.head == None:
            self.head = NewNode;
        else:
            temp = self.head;
            while temp.next:
                temp = temp.next;

            temp.next = NewNode;

    def Display(self):
        temp = self.head;
        while temp:
            print("{0}->".format(temp.data),end='')
            temp = temp.next;


if __name__ == '__main__':
    L1 = LinkedList();
    L1.Push(5);
    L1.Push(10);
    L1.Display();




