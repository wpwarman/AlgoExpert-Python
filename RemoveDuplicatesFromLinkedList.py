from tempfile import tempdir


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

def printLinkedList(list, index = 0):
    if list:
        print(f"{list.value} / {index}")
        printLinkedList(list.next, index + 1)
    return

def removeDuplicatesFromLinkedList(linkedList):
    temp = []
    def worker(linkedList):
        if linkedList:
            temp.append(linkedList.value)
            worker(linkedList.next)
    worker(linkedList)
    return temp
        

array = [56,68,46,6,35,654,8,6,35,56,98]
test = createLinkedList(array)
printLinkedList(test)
test2 = removeDuplicatesFromLinkedList(test)
print(test2)