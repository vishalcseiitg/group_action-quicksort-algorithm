import networkx as nx
import numpy as np
import random
import time

# Traditional Quicksort
def quicksort(A):
    if len(A) <= 1:
        return A
    pivot = random.choice(A)
    left = [x for x in A if x < pivot]
    middle = [x for x in A if x == pivot]
    right = [x for x in A if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Group Action Quicksort
def group_action_quicksort(A):
    # Step 1: Represent the input array as a graph
    G = nx.Graph()
    for i in range(len(A)):
        G.add_node(i, value=A[i])
        if i > 0:
            G.add_edge(i-1, i)
    
    # Step 2: Define a group action on the graph
    # For simplicity, we'll use a cyclic shift of the vertices
    def cyclic_shift(G, k):
        n = len(G)
        new_labels = np.arange(n)
        new_labels = np.roll(new_labels, k)
        mapping = dict(zip(range(n), new_labels))
        return nx.relabel_nodes(G, mapping)
    
    # Step 3: Select a pivot vertex using the group action
    n = len(G)
    pivot_node = None
    for i in range(n):
        G_shifted = cyclic_shift(G, i)
        left_nodes = [node for node in G_shifted.nodes() if node < i]
        right_nodes = [node for node in G_shifted.nodes() if node >= i]
        if len(left_nodes) == len(right_nodes):
            pivot_node = i
            break
    if pivot_node is None:
        # Fallback strategy: select pivot randomly
        pivot_node = random.choice(range(n))
    
    # Step 4: Partition the array and recursively apply the algorithm
    pivot = G.nodes[pivot_node]['value']
    A1 = [A[i] for i in left_nodes]
    A2 = [A[i] for i in right_nodes]
    if len(A1) > 1:
        A1 = group_action_quicksort(A1)
    if len(A2) > 1:
        A2 = group_action_quicksort(A2)
    return A1 + [pivot] + A2

# Test on arrays of different sizes
array_sizes = [10**i for i in range(1, 4)]
traditional_quicksort_times = []
group_action_quicksort_times = []

for size in array_sizes:
    print(f"Testing with array size {size}")
    A = np.random.rand(size)
    
    # Traditional Quicksort
    start_time = time.time()
    quicksort(A)
    end_time = time.time()
    traditional_quicksort_times.append(end_time - start_time)
    
    # Group Action Quicksort
    start_time = time.time()
    group_action_quicksort(A)
    end_time = time.time()
    group_action_quicksort_times.append(end_time - start_time)

# Plot the results
import matplotlib.pyplot as plt
plt.plot(array_sizes, traditional_quicksort_times, label="Traditional Quicksort")
plt.plot(array_sizes, group_action_quicksort_times, label="Group Action Quicksort")
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Array Size")
plt.ylabel("Time (seconds)")
plt.legend()
plt.show()
