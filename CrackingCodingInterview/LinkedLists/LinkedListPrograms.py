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

    #Q1 Remove duplicates
    def removeDuplicates(self):
        current = self.head
        while current:
            runner = current
            while(runner.next):
                if(current.data == runner.next.data):
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

    #Q2 Remove kth last element
    def getKthLastElement(self, k):
        i = [0]
        return getKthLastElement_util(self.head, k, i).data

    #Q3 Delete given node in  the middle
    def deleteNodeMiddle(self, node):
        if node is None or node.next is None:
            return False

        currentNext = node.next 
        node.data = currentNext.data
        node.next = currentNext.next
        return True
    
    # Partition node at particular value of node
    def PartitionAtNode(self, value):
        finalHead = None
        leftHead = None
        left = None
        rightHead = None
        right = None

        node = self.head
        while(node):
            if(node.data < value): # left array
                if(not leftHead):
                    leftHead = node
                    left = leftHead
                else:
                    left.next = node
                    left = node
            else:                  # right array
                if(not rightHead):
                    rightHead = node
                    right = rightHead
                else:
                    right.next = node
                    right = node
            node = node.next

        if(not leftHead):           # left head doesn't exist
            finalHead = rightHead
            right.next = None
        else:
            finalHead = leftHead
            left.next = rightHead
            if(rightHead):          # if right head exists
                right.next = None

        return finalHead

def getKthLastElement_util(head, k, i):
        if(head == None):
            return None

        currentNode = getKthLastElement_util(head.next, k, i)

        i[0]=i[0]+1
        if(i[0]==k):
            return head
        return currentNode


if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.prepend(8)
    linkedList.append(7)
    linkedList.append(3)
    testNode = linkedList.append(4)
    linkedList.append(10)
    linkedList.append(1)
    linkedList.PartitionAtNode(4)
    # print(linkedList.getKthLastElement(2))
    # linkedList.deleteNodeMiddle(testNode)
    linkedList.printList()
