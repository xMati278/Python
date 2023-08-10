class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def remove_duplicates(self):
        if not self.head:
            return

        current = self.head
        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next


input_numbers = input("Enter a list of integers separated by a space: ").split()
int_numbers = [int(num) for num in input_numbers]

linked_list = LinkedList()
for num in int_numbers:
    linked_list.append(num)

print("Original list:")
linked_list.display()

linked_list.remove_duplicates()

print("List after removing duplicates:")
linked_list.display()
