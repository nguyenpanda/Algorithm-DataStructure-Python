from Linked_list import SinglyLinkedList, Node
import random
from MyPackage.Tool import performance

def check(linked_list: SinglyLinkedList) -> bool:
    length = len(linked_list)
    
    if length == 0 or length == 1:
        return True
    
    current = linked_list.head
    for i in range(length):
        if current.data > current.next.data:
            return False
    return True

def split_list(linked_list: SinglyLinkedList) -> [SinglyLinkedList, SinglyLinkedList]:
    if linked_list.head is None:
        return linked_list, None
    else:
        length = len(linked_list)
        mid = length // 2
        mid_node: Node = linked_list.index(mid - 1)  # last node of the left half
        
        left = linked_list
        right = SinglyLinkedList()
        
        right.head = mid_node.next
        mid_node.next = None  # disconnection between left and right linked list
        
        left.set_length(mid)
        right.set_length(length - mid)
        return left, right

def merge(linked_list1: SinglyLinkedList, linked_list2: SinglyLinkedList) -> SinglyLinkedList:
    new_list = SinglyLinkedList()
    new_list.prepend(0)
    new_list.set_length(len(linked_list1) + len(linked_list2))
    
    current = new_list.head
    current_node_1 = linked_list1.head
    current_node_2 = linked_list2.head
    
    while current_node_1 and current_node_2:
        if current_node_1.data <= current_node_2.data:
            current.next = current_node_1
            current = current.next
            current_node_1 = current_node_1.next
        else:
            current.next = current_node_2
            current = current.next
            current_node_2 = current_node_2.next
    
    # Append all element that remain in current_node_1 into new_list
    while current_node_1:
        current.next = current_node_1
        current_node_1 = current_node_1.next
        current = current.next
    
    # Append all element that remain in current_node_1 into new_list
    while current_node_2:
        current.next = current_node_2
        current_node_2 = current_node_2.next
        current = current.next
    
    new_list.head = new_list.head.next

    return new_list

def merge_sort(linked_list: SinglyLinkedList) -> SinglyLinkedList:
    if linked_list.head is None or len(linked_list) == 1:
        return linked_list
    
    left, right = split_list(linked_list)
    
    # Recursively sort the left and right halves
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Merge the sorted_list halves
    return merge(left, right)

if __name__ == '__main__':
    
    pass

