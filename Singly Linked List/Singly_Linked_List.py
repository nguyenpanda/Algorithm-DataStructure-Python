import random


class Algorithm:
    @staticmethod
    def split(arr, length: int):
        point = length // 2
        return arr[:point], arr[point:], point, length - point
    
    @staticmethod
    def merge(arr1, arr2, arr1_len, arr2_len):
        i, j = 0, 0
        result = []
        
        while i < arr1_len and j < arr2_len:
            if arr1[i] == arr2[j]:
                result.extend([arr1[i], arr2[j]])
                i += 1
                j += 1
            elif arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        
        if i < arr1_len:
            result.extend(arr1[i:])
        else:
            result.extend(arr2[j:])
        return result
    
    @staticmethod
    def mergeSort(arr, length: int):
        if length <= 1:
            return arr
        
        left, right, left_len, right_len = Algorithm.split(arr, length)
        
        left = Algorithm.mergeSort(left, left_len)
        right = Algorithm.mergeSort(right, right_len)
        
        return Algorithm.merge(left, right, left_len, right_len)


class Node:
    dataType = int | float | str
    
    def __init__(self, value: dataType):
        self.__value: Node.dataType = value
        self.next: Node | None = None
    
    def setValue(self, value: dataType):
        self.__value = value
    
    def getValue(self) -> dataType:
        return self.__value
    
    def __repr__(self) -> str:
        return f'Node[{self.__value}] -> {self.next}'
    
    def __str__(self) -> str:
        return f'Node[{self.__value}]'


class SinglyLinkedList:
    
    def __init__(self):
        self.__head: Node | None = None
        self.__length: int = 0
        self.__tail: Node | None = None
    
    def isEmpty(self) -> bool:
        return len(self) == 0
    
    def getHead(self) -> Node:
        return self.__head
    
    def setHead(self, node: Node):
        self.__head = node
    
    def search(self, target: Node.dataType) -> Node | None:
        current: Node = self.getHead()
        
        while current:
            if current.getValue() == target:
                return current
            else:
                current = current.next
        
        return None
    
    def index(self, index: int) -> Node:
        if not (0 <= index < len(self)):
            raise IndexError(f'Index out of range, singly linked list length {len(self)}, got {index}')
        
        current: Node = self.getHead()
        for _ in range(index):
            current = current.next
        
        return current
    
    def remove(self, index: int):
        if not (-len(self) - 1 <= index <= len(self)):
            raise IndexError(f'Index out of range [{-len(self) - 1}, {len(self)}], got {index}')
        
        if self.isEmpty():
            return self
        
        current: Node = self.getHead()
        
        if index < 0:
            index = len(self) + index + 1
        
        for _ in range(index - 1):
            current = current.next
        
        current.next = current.next.next
        self.increaseLengthBy(-1)
        return self
    
    def prepend(self, value: Node.dataType) -> 'SinglyLinkedList':
        newNode: Node = Node(value)
        newNode.next = self.getHead()
        self.setHead(newNode)
        self.increaseLengthBy(1)
        return self
    
    def append(self, value: Node.dataType) -> 'SinglyLinkedList':
        newNode: Node = Node(value)
        
        if self.isEmpty():
            self.setHead(newNode)
            self.increaseLengthBy(1)
            return self
        
        current: Node = self.getHead()
        while current.next:
            current = current.next
        
        current.next = newNode
        self.increaseLengthBy(1)
        return self
    
    def insert(self, value: Node.dataType, index: int) -> 'SinglyLinkedList':
        if not (-len(self) - 1 <= index <= len(self)):
            raise IndexError(f'Index out of range [{-len(self) - 1}, {len(self)}], got {index}')
        
        if index == 0:
            self.prepend(value)
            return self
        
        if index < 0:
            index = len(self) + index + 1
        
        current: Node = self.getHead()
        newNode: Node = Node(value)
        
        for _ in range(index - 1):
            current = current.next
        
        newNode.next = current.next
        current.next = newNode
        
        self.increaseLengthBy(1)
        return self
    
    def __iter__(self):
        current: Node = self.getHead()
        while current:
            yield current.getValue()
            current = current.next
    
    def __setitem__(self, index: slice | int, value: Node.dataType | int):
        """
        self[index] = value
        
        [5]->[-6]->[-3]->[6]->[7]->[2]->[6]->[10]->[10]->[-10]->[4]->[9]
        Index: slice(2, 4, None)
        Value: [99, 98]
        start, stop, step: (2, 4, 1)
        sequence_length: 2
        [5]->[-6]->[99]->[98]->[7]->[2]->[6]->[10]->[10]->[-10]->[4]->[9]
        """
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            sequence_length = len(range(start, stop, step))

            if sequence_length != len(value):
                raise ValueError(f'attempt to assign sequence of size {len(value)} to extended slice of size {sequence_length}')
            
            current = self.index(start)
            for item in value:
                current.setValue(item)
                current = current.next
                start += step
                
        else:
            if index < 0:
                index = len(self) + index
            if index < 0 or index >= len(self):
                raise IndexError("Index out of range")
            
            current = self.index(index)
            current.setValue(value)
    
    def __len__(self) -> int:
        return self.__length
    
    def increaseLengthBy(self, length: int = 1):
        self.__length += length
        return len(self)
    
    def __str__(self) -> str:
        nodeList: list[str] = []
        current: Node | None = self.__head
        
        for _ in range(len(self)):
            nodeList.append(f'[{current.getValue()}]')
            current = current.next
        
        return '->'.join(nodeList)
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}: Head node is {self.getHead()} - total {len(self)} node(s)'


if __name__ == '__main__':
    def SLL_Testing1():
        a = SinglyLinkedList()
        searchVal = 100
        
        for i in range(5):
            a.prepend(i)
        
        print(f' \u001b[32mInitial Linked List\u001b[0m: {a}')
        
        print(f'         \u001b[32mLinked List\u001b[0m: {a}')
        print(f'           \u001b[32mRepresent\u001b[0m: {repr(a)}')
        print(f'  \u001b[32mLinked List Length\u001b[0m: {len(a)}')
        print('-----------------------------------------------------------------------------')
        print(f'      \u001b[32mSearch for {searchVal}\u001b[0m: {a.search(searchVal)}')
        # print(f'      \u001b[32mSorting {}\u001b[0m: {a.search(searchVal)}')
        print('-----------------------------------------------------------------------------')
    
    def SLL_Testing2():
        # def getValue(self) -> Node.dataType:
        #     current: Node | None = self.getHead()
        #     while True:
        #         yield current.getValue()
        #         current = current.next
        a = SinglyLinkedList()
        
        for _ in range(12):
            i = random.randint(-10, 10)
            a.prepend(i)
        
        print(a)
        a[2:4] = [99, 98]
        print(a)
        
        # b = Algorithm.mergeSort(a, 12)
        
    
    def Merge_Testing():
        ls1 = [1, 2, 2, 6, 7, 9]
        l1_len = len(ls1)
        ls2 = []
        ls2_len = len(ls2)
        
        ls = []
        for _ in range(100):
            i = random.randint(-20, 20)
            ls.append(i)
        
        print(ls)
        a = Algorithm.mergeSort(ls, len(ls))
        print(a)
    
    
    # Merge_Testing()
    # SLL_Testing1()
    SLL_Testing2()
    
