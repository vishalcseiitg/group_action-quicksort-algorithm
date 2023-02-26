import random
import time

# define a node class for the graph
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# create a new node with the given value
def create_node(value):
    return Node(value)

# add a node with the given value to the end of the list
def add_node(head, value):
    n = create_node(value)
    if head is None:
        head = n
    else:
        curr = head
        while curr.next is not None:
            curr = curr.next
        curr.next = n
    return head

# compute the cyclic shift of the graph by i positions
def cyclic_shift(head, i):
    if head is None:
        return None
    n = 0
    curr = head
    while curr is not None:
        n += 1
        curr = curr.next
    i = (i % n + n) % n  # handle negative values of i
    if i == 0:
        return head
    curr = head
    for j in range(i-1):
        curr = curr.next
    tail = curr
    while tail.next is not None:
        tail = tail.next
    tail.next = head
    head = curr.next
    curr.next = None
    return head

# compute the node at index i in the graph
def node_at_index(head, i):
    curr = head
    for j in range(i):
        curr = curr.next
    return curr

# partition the graph using the node at index i as the pivot
def partition(head, i):
    p = node_at_index(head, i)
    left = None
    right = None
    curr = head
    while curr is not None:
        next = curr.next
        if curr == p:
            pass
        elif curr.value < p.value:
            curr.next = left
            left = curr
        else:
            curr.next = right
            right = curr
        curr = next
    if left is None:
        left = p
    else:
        tail = left
        while tail.next is not None:
            tail = tail.next
        tail.next = p
    p.next = right
    return left

# sort the graph using GroupActionQuicksort
def group_action_quicksort(head):
    # Base case
    if head is None or head.next is None:
        return head
    
    # Determine the length of the list
    n = 0
    curr = head
    while curr is not None:
        n += 1
        curr = curr.next
    
    # Find the pivot element and partition the list around it
    p = None
    for i in range(n):
        g = head
        g_prime = cyclic_shift(g, i)
        l = partition(g_prime, i)
        r = l.next
        l.next = None
        if r is not None:
            r = cyclic_shift(r, n-i-1)
        if l is None:
            p = node_at_index(head, i)
            break
        elif r is None:
            r = node_at_index(head, i+1)
            break
        else:
            g = create_node(None)
            g.next = l
            l = g
            g = create_node(None)
            g.next = r
            r = g
            l = group_action_quicksort(l)
            r = group_action_quicksort(r)
            p = node_at_index(head, i)
            break
    
    # Concatenate the three sublists
    if l is None:
        left = p
    else:
        left = l
        tail = left
        while tail.next is not None:
            tail = tail.next
        tail.next = p
    
    if r is None:
        right = None
    else:
        right = r
        right = cyclic_shift(right, 1)
    
    if left is None:
        head = p
    else:
        head = left
        tail = left
        while tail.next is not None:
            tail = tail.next
        tail.next = p
    p.next = right
    
    # Return the sorted list
    return head

# Define the input and output file paths
input_file = "input.txt"
output_file = "output.txt"
time_file = "time.txt"

# Read the input list from the input file
with open(input_file, "r") as f:
    nums = list(map(int, f.readline().strip().split()))

# Convert the input list to a linked list
head = None
for num in nums:
    head = add_node(head, num)

# Sort the linked list using group_action_quicksort and measure the time taken
start_time = time.time()
head = group_action_quicksort(head)
end_time = time.time()
time_taken = end_time - start_time

# Write the sorted list and time taken to the output and time files
with open(output_file, "w") as f:
    curr = head
    while curr is not None:
        f.write(str(curr.value) + " ")
        curr = curr.next

with open(time_file, "w") as f:
    f.write(str(time_taken))
