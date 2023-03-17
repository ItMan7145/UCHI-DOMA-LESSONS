class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


def del_element(element):
    if element == 0:
        n1.value = None
        n1.next = None
        print_linked_list(n2)

    elif element == 1:
        n1.next = n3
        n2.value = None
        n2.next = None
        print_linked_list(n1)

    elif element == 2:
        n2.next = None
        n3.value = None
        n3.next = None
        print_linked_list(n1)


def print_linked_list(vertex):
    while vertex:
        print(vertex.value, end=" -> ")
        vertex = vertex.next
    print("None")


n3 = Node('third', None)
n2 = Node('second', n3)
n1 = Node('first', n2)

num_del = int(input())
del_element(num_del)
