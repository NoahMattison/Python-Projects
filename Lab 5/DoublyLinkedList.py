#
# ================================================================================
# Noah Mattison     10/20/2023
# Lab 5
# Purpose: Doubly Linked List
# References: educative, geeksforgeeks, code academy, Jude Vargas
# ================================================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        """
        allows the doubly linked list to be iterated over by something like a for loop
        Parameters: None
        Returns: None (yields each item in the linked list for iterators)
        """
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def add(self, item):
        """
        adds the specified item (as a node) to the beginning (head) of the doubly linked list
        Parameters:
            item: the item to add to the doubly linked list
        Returns: None
        """
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def pop(self, pos=None):
        """
        removes the item at the specified position (or the last position if pos = None)
        """
        previous, current = self.head, self.head

        if self.is_empty() or (pos is not None and pos >= self.length):
            raise IndexError("PLEASE FOR THE LOVE OF GOD ITS OUT OF RANGE PLEASE... ")
        if pos is not None and pos < 0:
            raise ValueError("unga chunga wunga pos needs to be positive")
        if self.size() == 1:
            self.head = None
        elif pos is not None:
            if pos == 0:
                self.head = current.next
            else:
                count = 0
                while count != pos:
                    previous = current
                    current = current.next
                    count += 1
                previous.next = current.next
        else:
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = None
        self.length -= 1
        return current

    def search(self, item):
        """
        Searches for the item in the list. Returns true if the item is in the list, False otherwise
        :param item:
        :return: Boolean
        """
        is_found, current = False, self.head
        if not self.is_empty():
            while not is_found and current is not None:
                if current.data == item:
                    is_found = True
                else:
                    current = current.next
            return is_found

    def remove(self, item):
        """
        Removes an item from the list
        :param item:
        :return: none
        """
        previous, current, is_found = self.head, self.head, False
        if self.is_empty():
            raise ValueError("list.remove(x) x not in list...")
        if self.head.data == item:
            is_found = True
            self.head = self.head.next
        else:
            while not is_found and current is not None:
                if current.data == item:
                    is_found = True
                    previous.next = current.next
                else:
                    previous = current
                    current = current.next
        if not is_found:
            raise ValueError("list.remove(x) x not in list...")
        self.length -= 1

    def is_empty(self):
        """
        returns True if the linked list is empty, else False
        Parameters: None
        Returns: True if the linked list is empty, else False
        """
        return self.head is None

    def size(self):
        """
        returns an int representing the length of the linked list
        Parameters: None
        Returns: an int representing the length of the linked list
        """
        return self.length