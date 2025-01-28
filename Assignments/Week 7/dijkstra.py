import heapq
import math

KEY = 0
VALUE = 1
LENGTH = 0
NODE = 1
ROOT = 0

class CustomHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self._bubble_up(self.size - 1)

    def extract_min(self):
        min_value = self.heap[ROOT][VALUE]
        last_item = self.heap[self.size - 1]
        self.heap[ROOT] = last_item
        self.heap.pop()
        self.size -= 1
        self._bubble_down(ROOT)
        return min_value

    def find_min(self):
        return self.heap[ROOT][VALUE]

    def heapify(self, l: list): # wrapper
        self.heap = l
        heapq.heapify(self.heap)
        self.size = len(self.heap)

    def delete(self, item):
        item[KEY] = -1
        item_index = self.heap.index(item)
        self._bubble_up(item_index)
        self.extract_min()

    def update_key(self, new_key, item):
        item[KEY] = new_key
        item_index = self.heap.index(item)
        parent_index = (item_index - 1) // 2
        if self.heap[parent_index][KEY] > self.heap[item_index][KEY]:
            self._bubble_up(item_index)
        else:
            self._bubble_down(item_index)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _bubble_up(self, item_index):
        while item_index > 0:
            parent_index = (item_index - 1) // 2
            if self.heap[parent_index][KEY] <= self.heap[item_index][KEY]:
                break
            self._swap(item_index, parent_index)
            item_index = parent_index

    def _bubble_down(self, item_index):
        while True:
            left_child_index = 2 * item_index + 1
            right_child_index = 2 * item_index + 2
            if left_child_index > self.size - 1:
                break
            smallest_child_index = left_child_index
            if right_child_index < self.size and self.heap[right_child_index][KEY] < self.heap[left_child_index][KEY]:
                smallest_child_index = right_child_index
            if self.heap[item_index][KEY] <= self.heap[smallest_child_index][KEY]:
                break
            self._swap(item_index, smallest_child_index)
            item_index = smallest_child_index


def dijkstra(graph: dict, s: int):
    processed_nodes = []
    heap = CustomHeap()
    keys = dict()
    heap_item = dict()
    for tail, heads in graph.items():
        keys[tail] = math.inf
    keys[s] = 0
    # heap.heapify([[keys[tail], tail] for tail, heads in graph.items()])
    for node in graph.keys():
        item = [keys[node], node]
        heap.insert(item)
        heap_item[node] = item
    while heap.heap:
        min_key_tail = heap.extract_min()
        processed_nodes.append(min_key_tail)
        for head, length in graph[min_key_tail]:
            if head not in processed_nodes:
                item = heap_item[head]
                # heap.delete(item)
                keys[head] = min(keys[head], keys[min_key_tail] + length)
                # item[KEY] = keys[head]
                # heap.insert(item)
                heap.update_key(keys[head], item)
    return keys

def read_weighted_adj_list(file_path):
    adj_list = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.split()
            tail = int(line[0])
            heads = []
            for edge in line[1:]:
                edge = edge.split(',')
                edge = [int(edge[0]), int(edge[1])]
                heads.append(edge)
            adj_list[tail] = heads
    return adj_list

def test_1():
    g = read_weighted_adj_list('test1.txt')
    shortest_path_lengths = dijkstra(g, 1)
    for i in range(1, 9):
        print(f'{shortest_path_lengths[i]},', end='')

def test_2():
    g = read_weighted_adj_list('test2.txt')
    shortest_path_lengths = dijkstra(g, 1)
    nodes = [7,37,59,82,99,115,133,165,188,197]
    for node in nodes:
        print(f'{shortest_path_lengths[node]},', end='')

def test_custom_heap():
    heap = CustomHeap()

    five = [5, 'five']
    heap.insert(five)
    heap.insert([7, 'seven'])
    heap.insert([3, 'three'])
    heap.insert([2, 'two'])
    heap.insert([6, 'six'])
    one = [1, 'one']
    heap.insert(one)
    heap.insert([4, 'four'])

    print(heap.heap)
    heap.delete(five)
    print(heap.heap)
    heap.delete(one)
    print(heap.heap, '\n')

    for _ in range(heap.size):
        minimum = heap.extract_min()
        print("min:\t", minimum, '\nheap:\t', heap.heap)

if __name__ == "__main__":
    # test_custom_heap()
    # test_1()    # 0,1,2,3,4,4,3,2,
    test_2()    # 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068,
