# from MyPackage.Random import Random
import random

class Node:
    """
    - Node class
    """
    
    def __init__(self, data):
        self.data = data
        self.next: [Node, None] = None
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self.data})'
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.data})'


class SinglyLinkedList:
    def __init__(self):
        """
        - Create a singly linked list
        """
        self.head: [Node, None] = None
        self.__length: int = 0
    
    def increase_len_by(self, num: int = 1):
        self.__length += num
    
    def set_length(self, length: int):
        self.__length = length
        
    def is_empty(self) -> bool:
        """
        Takes O(1) space and time
        :return: True if the list is empty, False otherwise
        """
        return self.head is None
    
    def search(self, target) -> [Node, None]:
        """
        - Linear Search Algorithm
        - Takes O(n) complexity and O(1) space complexity
        :param target:
        :return: Node, if found, else None
        """
        current: Node = self.head
        
        while current:
            if current.data == target:
                return current
            else:
                current = current.next
        
        return None
    
    # Miss the out of range situation
    def index(self, index: int) -> Node:
        """
        - Takes O(n) time and O(1) space complexity
        :param index: integer index to look for
        :retur n: a Node that is indexed by index
        """
        if not isinstance(index, int):
            raise IndexError(f"Linked list index out of range! Linked list length: {len(self)}, got index {index}")
        
        if index == 0:
            return self.head
        
        if index < 0:
            index = len(self) + index
        
        current: Node = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def nodes_are_equal(self, target) -> list[int, None]:
        """
        
        :param target: node data
        :return: list of node indexes that are equal to target
        """
        result: list[int, None] = []
        current: Node = self.head
        
        for index in range(len(self)):
            if current.data == target:
                result.append(index)
                current = current.next
            else:
                current = current.next
        
        return result
    
    def append(self, data):
        """
        - Adds data to the end of the list
        - Takes O(n) time and O(1) space complexity
        :param data:
        """
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            self.increase_len_by()
            return
        
        current: Node = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
        
        self.increase_len_by()
        return self
    
    def prepend(self, data):
        """
        - Adds data to the beginning of the list
        - Takes O(1) time and space complexity
        :param data:
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
        self.increase_len_by()
        return self
    
    # Need to be optimized
    def insert(self, index: int, data):
        """
        - Insert an element into a singly linked list at a specific position
        :param index:
        :param data:
        :return:
        """
        length = len(self)
        if index < 0 or not isinstance(index, int):
            raise ValueError(f"Index must be a non-negative integer, got {index}")
        elif index > length:
            raise ValueError(f"Linked list out of range! Linked list length: {length}, got index {index}")
        
        if index == 0:
            self.prepend(data)
            self.increase_len_by()
            return self
        
        new_node = Node(data)
        current = self.head
        
        # Move current node to the forward insertion node
        for _ in range(index - 1):
            # if current.data is None and current.next is None:
            #     raise ValueError(f"Index {index} out of")
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        
        self.increase_len_by()
        return self
    
    def link(self, linked_list):
        """
        - Take O(|self|) time and O(0) space complexity
        - self: change into self -> linked_list
        - linked_list: remain unchanged after adding
        :param linked_list: SinglyLinkedList
        """
        if not isinstance(linked_list, SinglyLinkedList):
            raise ValueError(f'Input must be a SinglyLinkedList object, got {type(linked_list)}')
        
        if self.head is None:
            self.head = linked_list.head
        else:
            self.index(-1).next = linked_list.head
        
        self.increase_len_by(len(linked_list))
        return self
    
    def remove(self, index: int):
        if index == 0:
            if self.head is not None:
                self.head = self.head.next
                self.increase_len_by(-1)
                return self
            else:
                raise IndexError("Linked list is empty.")
        
        current: Node = self.head
        
        # Move current node to the forward insertion node
        for _ in range(index - 1):
            current = current.next
        
        if current.next is not None:
            current.next = current.next.next
        else:
            raise IndexError(f"Linked list out of range! Linked list length: {len(self)}, got index {index}")
        
        self.increase_len_by(-1)
        return self
    
    def __add__(self, *other):
        new_list = SinglyLinkedList()
        
        # Add nodes from the current linked list
        current_node = self.head
        while current_node:
            new_list.append(current_node.data)
            current_node = current_node.next
        
        # Add nodes from other linked lists in the tuple
        for linked_list in other:
            if not isinstance(linked_list, SinglyLinkedList):
                raise ValueError(f'Input must be a SinglyLinkedList object, got {type(linked_list)}')
            
            current_node = linked_list.head
            while current_node:
                new_list.append(current_node.data)
                current_node = current_node.next
        
        return new_list
    
    def __iter__(self):
        """
        Returns an iterator object that iterates over the nodes of the linked list.
        """
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next
    
    def __len__(self) -> int:
        """
        - Takes O(1) time and space complexity
        :return: Length of the linked list
        """
        return self.__length
    
    def __str__(self) -> str:
        """
        - Takes O(n) time and O(1) space complexity
        :return: string representation of the list
        """
        node_list = []
        
        current: Node = self.head
        while current:
            node_list.append(str(f'[{current.data}]'))
            current = current.next
        
        return '->'.join(node_list)
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__} - {len(self)} Nodes'


def fourLL():
    a = SinglyLinkedList()
    b = SinglyLinkedList()
    c = SinglyLinkedList()
    d = SinglyLinkedList()
    
    a.set_length = 10
    b.set_length = 10
    c.set_length = 10
    d.set_length = 10
    
    for i in range(0, 10):
        a.append(i)
    
    for i in range(10, 20):
        b.append(i)
    
    for i in range(20, 30):
        c.append(i)
    
    for i in range(30, 40):
        d.append(i)
    return a, b, c, d


def randomLL(length: int, a, b):
    linked_list = SinglyLinkedList()
    for _ in range(length):
        num = random.randint(a, b)
        linked_list.append(num)
    linked_list.set_length(length)
    return linked_list


if __name__ == '__main__':
    pass
