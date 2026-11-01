from typing import List


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        curr = self.head
        i = 0

        while curr:
            if i == index:
                return curr.val

            curr = curr.next
            i += 1

        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)

        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        # Removing the head
        if index == 0:
            self.head = self.head.next

            if self.head is None:
                self.tail = None

            return True

        # Find the node before the target
        curr = self.head
        i = 0

        while i < index - 1 and curr:
            curr = curr.next
            i += 1

        # Target does not exist
        if curr is None or curr.next is None:
            return False

        # Remove the target node
        if curr.next == self.tail:
            self.tail = curr

        curr.next = curr.next.next

        return True

    def getValues(self) -> List[int]:
        values = []
        curr = self.head

        while curr:
            values.append(curr.val)
            curr = curr.next

        return values
