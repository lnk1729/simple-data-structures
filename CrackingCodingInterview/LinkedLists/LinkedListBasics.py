class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        if(self.head == None):
            self.head = Node(data)
        else:
            tmp = Node(data)
            tmp.next = self.head
            self.head = tmp

        return self.head

    def append(self, data):
        if(self.head == None):
            self.head = Node(data)
            return self.head
        else:
            tmp = self.head
            while(tmp.next):
                tmp = tmp.next
            tmp.next = Node(data)
            return tmp.next

    def insertByPos(self, pos, data):
        if(self.head == None and pos == 0):
            self.head = Node(data)
            return self.head
        
        if(pos == 0):
            self.prepend(data)

        i = 0
        tmp = self.head
        while(i<pos-1):
            tmp = tmp.next
            i+=1
        
        if tmp is None:
            return None

        actualNext = Node(data)
        actualNext.next = tmp.next
        tmp.next = actualNext
        return actualNext            

    def deleteByPos(self, pos):
        if(self.head == None):
            return None

        if(self.head.next == None):
            self.head = None
            return self.head

        tmp = self.head
        i=1
        while (i < pos):
            tmp = tmp.next
            i+=1

        if tmp is None or tmp.next is None:
            return None

        actualNext = tmp.next.next
        tmp.next = None
        tmp.next = actualNext

    def deleteByData(self,data):
        if(self.head is None):
            return None

        if(self.head.data == data and self.head.next is None):
            self.head = None
            return None

        tmp = self.head
        while(tmp):
            if(tmp.next.data == data):
                actualNext = tmp.next.next
                tmp.next = None
                tmp.next = actualNext
                return self.head
            else:
                tmp = tmp.next

    def printList(self):
        listStr = ""
        tmp = self.head
        while(tmp):
            listStr+=str(tmp.data) + " "
            tmp = tmp.next
        print(listStr)
            


if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.append(20)
    linkedList.append(10)
    linkedList.append(30)
    linkedList.append(50)
    linkedList.prepend(5)
    linkedList.insertByPos(2, 25)
    # linkedList.deleteByData(30)
    # linkedList.deleteByPos(2)
    linkedList.printList()
