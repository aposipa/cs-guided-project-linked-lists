
class LinkedListNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next  = next
        self.prev = prev


# class LinkedList:
#     def __init__(self, head=None):
#         self.head = head

#     def append(self, data):
#         new_node = LinkedListNode(data)

#         if self.head:
#             current = self.head

#             while current.next: 
#                 current = current.next

#             current.next = new_node
#         else:
#             self.head = new_node

class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail


    def add_to_head(self, data):
        new_node = LinkedListNode(data)

        if self.head:
            current = self.head
            current.prev = new_node
            new_node.next = current
            self.head = new_node

    def add_to_tail(self, data):
        new_node = LinkedListNode(data)

        if self.tail:
            current = self.tail
            current.next = new_node
            new_node.prev = current
            self.tail = new_node
        



# (10) ->
lln = LinkedListNode(10)

ll = DoublyLinkedList(lln)
ll.add_to_tail(20)
# (10) -> (20)