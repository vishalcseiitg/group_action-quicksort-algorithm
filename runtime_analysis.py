import matplotlib.pyplot as plt

# Define datasets and their names

import random

def generate_random_list(length):
    return [random.randint(0, 999) for _ in range(length)]

import random

def generate_almost_sorted_list(n):
    """Generates an almost sorted list of length n."""
    lst = list(range(n))
    num_swaps = int(n * 0.1)
    for i in range(num_swaps):
        j = random.randint(0, n-2)
        lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def generate_reversed_list(n):
    """Generate a reversed list of n integers."""
    return list(range(n, 0, -1))



datasets = [(generate_random_list(1000), 'Random'),(generate_almost_sorted_list(1000), 'Almost Sorted'),(generate_reversed_list(1000), 'Reversed')]

# Run both algorithms and record their runtimes
traditional_quicksort_times = []
group_action_quicksort_times = []

for name, dataset in datasets:
    # Traditional Quicksort
    start_time = time.time()
    quicksort(dataset)
    end_time = time.time()
    traditional_quicksort_times.append(end_time - start_time)

    # Group Action Quicksort
    start_time = time.time()
    group_action_quicksort(dataset)
    end_time = time.time()
    group_action_quicksort_times.append(end_time - start_time)

# Plot the bar chart
labels = ['Random', 'Almost Sorted', 'Reversed']
x = np.arange(len(labels))
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, traditional_quicksort_times, width, label='Traditional')
rects2 = ax.bar(x + width/2, group_action_quicksort_times, width, label='Group Action')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Runtime (seconds)')
ax.set_title('Comparison of Traditional and Group Action Quicksort')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Add labels to the bars
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)

# Change the color of the bars
rects1[0].set_color('#FDB813')
rects2[0].set_color('#0D5C63')
rects1[1].set_color('#FDB813')
rects2[1].set_color('#0D5C63')
rects1[2].set_color('#FDB813')
rects2[2].set_color('#0D5C63')

fig.tight_layout()

plt.show()
