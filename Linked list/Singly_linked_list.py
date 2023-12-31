# Creating a Node class for single node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Creating LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    # Inserting elements at the last of the linkedlist 

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    # Inserting elements at the first of the linkedlist

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # Inserting elements at the speficied index value

    def insert(self, index, value):
        new_node = Node(value)
        if index < -1 or index > self.length:
            return False
        elif index == -1:
            self.tail.next = new_node
            self.tail = new_node
        elif index == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # Deleting all the elements in the linkedlist

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Traverse the linkedlist to print the elements

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    # Poping the first element

    def pop_first(self):
        if self.head is None:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node

    # Poping the last element

    def pop(self):
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return temp
    
    # Deleting the particular element

    def delete_particular(self, index):
        if (index < 0 or index >= self.length):
            return None
        if self.length == 1:
            return self.pop_first()
        elif index == -1:
            return self.pop()
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            empty = temp.next
            temp.next = empty.next
            empty.next = None
        self.length -= 1
        
        


    # Reversing the linkedlist

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        self.length -= 1

linkedlist = LinkedList()
linkedlist.append(20)
linkedlist.prepend(10)
linkedlist.insert(1,30)
linkedlist.insert(3,40)
print(linkedlist.traverse())
print('--------------------------------------------')
linkedlist.delete_particular(1)
print(linkedlist.traverse())
print('--------------------------------------------')
linkedlist.reverse()
print(linkedlist.traverse())

