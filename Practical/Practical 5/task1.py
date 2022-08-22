# Create Link list node
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Print by traversing a Singly Linked List
    def printLinkList(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    # Add New Data Node to beginning of the singly linked list
    def AddBeginning(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode

    # Add New Data Node to the end of the singly linked list
    def AddEnd(self, data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            return
        traverse = self.head
        while traverse.next is not None:
            traverse = traverse.next
        traverse.next = NewNode

    def findSecondToLast(self):
        if self.head is None and self.head.next is None:
            return print("Empty list or list with less than 2 elements")
        # traverse the linked list
        traverse = self.head
        while traverse is not None:
            # check if the next next data is none
            if traverse.next.next is None:
                return print(traverse.data)
            else:
                # If not then continue to the next node
                traverse = traverse.next



list = SinglyLinkedList()
list.head = Node(1)
element2 = Node(2)
element3 = Node(3)
element4 = Node(4)

# Linking all the elements together
list.head.next = element2
element2.next = element3
element3.next = element4

# return a list of 1,2,3,4
print("Traversing the link list example")
list.printLinkList()


print("-" * 10)
# add data "3" to the beginning of the Node
list.AddBeginning(3)

# return a list of 3,1,2,3,4
print("Add to beginning example: ")
list.printLinkList()

print("-" * 10)
# add data "3" to the end of the Node
list.AddEnd(3)
print("Add to end example:")
# return a list of 3,1,2,3,4,3
list.printLinkList()

print("-"*10)

print("Find second to last example: ")
# current list 3,1,2,3,4,3
# expected output of 4
list.findSecondToLast()


