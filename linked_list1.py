class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head_ref, new_data):
    new_node = Node()
    new_node.val = new_data
    new_node.next = (head_ref)
    (head_ref) = new_node
    return head_ref


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        current = self.head
        count = 0

        while (current):
            if (count == index):
                return current.data
            count += 1
            current = current.next
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        cur = Node(val)
        cur.next = self.head
        self.head = cur

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        cur = Node(val)
        if self.head is None:
            self.head = cur
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = cur

    def getNode(self, data):

        # allocating space
        newNode = Node(data)
        return newNode

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        new_node = Node(val)

        if self.head is None:
            if index != 0:
                return
            else:
                self.head = new_node

        if self.head != None and index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        prev = None

        i = 0
        while i < index:
            prev = current
            current = current.next

            if not current:
                break
            i += 1

        new_node.next = current
        prev.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.head == None:
            return
        temp = self.head
        if index == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(index - 1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None

        temp.next = next

    def hasCycle(self, head):
        slow_p = head
        fast_p = head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True
        return False

    # for 2 sorted linked lists
    def getIntersectionNode(self, a, b):
        dummy = Node()
        tail = dummy
        dummy.next = None

        while (a != None and b != None):
            if (a.val == b.val):
                tail.next = push((tail.next), a.val)
                tail = tail.next
                a = a.next
                b = b.next

            elif(a.val < b.val):
                a = a.next
            else:
                b = b.next 
        return (dummy.next)

    def removeNthFromEnd(self, head, n):
        fast = head
        slow = head
        
        while n:
            fast = fast.next
            n -= 1
        
        if not fast:
            return head.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return head


    
