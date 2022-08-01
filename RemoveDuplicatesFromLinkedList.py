print("Remove Duplicates from Linked List")

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def createLinkedList(array):
    if len(array) > 0:
        link = LinkedList(array.pop())
        link.next = createLinkedList(array)
        return link

def printLinkedList(list):
    if list != None:
        print(f"{list.value}")
        printLinkedList(list.next)
    return

def removeDuplicatesFromLinkedList(linkedList):
    while linkedList.next != None:
        print (linkedList.value)
    return None

array = [56,68,46,6,35,654,8,6,35,56,98]
test = createLinkedList(array)
printLinkedList(test)