"""datastruct.py

# Data Structures

This module defines the LinkedList abstract data type
"""
############################### 72 chars ###############################


class Node:
    """Represents a node in a linkedlist.

    Arguments
        - data
          The data encapsulated in the node.

    Attributes
        - next: Node | None
          The next node in the linkedlist, or None if the node is the tail.

    Methods
        - get() -> data
          Return the data stored in the node.
    """

    def __init__(self, data: tuple[int, int]):
        self.next = None
        self.data = data

    def __repr__(self) -> str:
        return f'Node({self.get()})'

    def get(self) -> tuple[int, int]:
        """Return the data stored in the node.

        Arguments
            None

        Return
            tuple[int, int]
        """
        return self.data


class LinkedList:
    """Represents a sequence of data items.

    Arguments
        None

    Attributes
        None

    Methods
        - length() -> int
        - get(index) -> item
        - insert(index, item) -> None
        - append(item) -> None
        - delete(index) -> None
    """

    def __init__(self):
        self._head = None

    def __repr__(self) -> str:
        return 'LinkedList()'

    def length(self) -> int:
        """Returns the number of nodes in the linkedlist.

        Arguments
            None

        Return
            length of linkedlist as an integer (zero or positive)
        """
        # Replace the line below with your code
        curr = self._head
        length = 0
        if self._head == None:
            return 0
        else:
            if self._head.next == None:
                return 1
        while curr != None: 
            length += 1
            curr = curr.next
        return length


    def get(self, n: int) -> tuple[int, int]:
        """Returns item at n-th node.

        Arguments
            - n: int
              sequence number of item to be retrieved.

        Returns
            item

        Raises
            IndexError if n >= length
        """
        # Replace the line below with your code
        current = 0
        currnode = self._head
        prevnode = None
        if n >= self.length():
            raise IndexError
        if n == 0:
            return self._head.get()
        while current <= n:
            prevnode = currnode
            currnode = currnode.next
            current += 1
        return prevnode.get()

    def insert(self, n: int, item: tuple[int, int]) -> None:
        """Insert item into linkedlist at position n.

        If n == 0, inserts item at the head.
        If n == length, appends item at the tail of the linkedlist.

        Arguments
            - n: int
              sequence number of item to be inserted.

        Raises
            IndexError if n > length
        """
        # Replace the line below with your code
        current = 0
        currnode = self._head
        prevnode = None
        nextnode = None
        if n > self.length():
            raise IndexError
        elif n == self.length():
            self.append(item)
            return
        elif n == 0:
            old_head = self._head
            self._head = Node(item)
            self._head.next = old_head
            return
        while current < n:
            prevnode = currnode
            currnode = currnode.next
            current += 1
        newnode = Node(item)
        prevnode.next = newnode
        newnode.next = currnode


    def append(self, item: tuple[int, int]) -> None:
        """Append item at the end of linkedlist.

        Arguments
            - item
              The item to be appended.

        Returns
            None
        """
        # Replace the line below with your code
        curr = self._head
        if self.length() == 0:
            self._head = Node(item) #activates if the start is empty
            return
        while curr != None:
            if curr.next == None:
                curr.next = Node(item)
                return
            else:
                curr = curr.next
        

    def delete(self, n: int) -> None:
        """Delete n-th item from linkedlist.

        Arguments
            - n: int
              sequence number of item to be retrieved.

        Raises
            IndexError if n > length
        """
        # Replace the line below with your code
        current = 0
        currnode = self._head
        if n >= self.length() or self.length() == 0:
            raise IndexError
        elif n == 0:
            if self._head != None:
                if self._head.next == None:
                    self._head = None
                else:
                    self._head = self._head.next
        else:
            prevnode = None
            while current < n:
                prevnode = currnode
                currnode = currnode.next
                current += 1
            if currnode.next == None: #deleting at the end
                    currnode = None
                    prevnode.next = None
            else: # deleting in the middle
                prevnode.next = currnode.next
            
    
    def contains(self, item: tuple[int, int]) -> bool:
        """Checks whether an item is in the linkedlist.
        Returns a boolean value to indicate the status of the search.

        Arguments
            - item
              The item to be searched for.

        Returns
            True if item is found in the linkedlist,
            otherwise False
        """
        # Replace the line below with your code
        curr = self._head
        if self.length() == 0:
            return False
        while curr != None:
            if curr.data == item:
                return True
            curr = curr.next
        return False


if __name__ == "__main__":
    # Write any test code here and run it with
    # `python datastruct.py`
    
    pass