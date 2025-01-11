import math

NODE = 0
LENGTH = 1
KEY = 0
VALUE = 1
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
        minimum = self.heap[ROOT]
        last_item = self.heap[self.size - 1]
        self.heap[ROOT] = last_item
        self.heap.pop()
        self.size -= 1
        self._bubble_down(ROOT)
        return minimum

    def delete(self, item):
        item[KEY] = -1
        item_index = self.heap.index(item)
        self._bubble_up(item_index)
        self.extract_min()

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

def dijkstra(graph: dict, v: int):
    processed_nodes = {v: 0}
    while True:
        shortest_edge = {'head': None, 'dijkstra_score': math.inf}
        for tail in processed_nodes:
            for head in graph[tail]:
                if head[NODE] not in processed_nodes:
                    dijkstra_score = processed_nodes[tail] + head[LENGTH]
                    if dijkstra_score < shortest_edge['dijkstra_score']:
                        shortest_edge['head'] = head[NODE]
                        shortest_edge['dijkstra_score'] = dijkstra_score
        if shortest_edge['head'] is None:
            for node in graph:
                if node not in processed_nodes:
                    processed_nodes[node] = math.inf
            return processed_nodes
        else:
            node = shortest_edge['head']
            processed_nodes[node] = shortest_edge['dijkstra_score']

def read_weighted_adj_list(file_path):
    adj_list = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.split()
            tail = int(line[0])
            heads = []
            for edge in line[1:]:
                edge = edge.split(',')
                edge = (int(edge[0]), int(edge[1]))
                heads.append(edge)
            adj_list[tail] = heads
    return adj_list

# def main():
#     g = read_weighted_adj_list('test2.txt')
#     shortest_path_lengths = dijkstra(g, 1)
#     # for i in range(1, 9):
#     #     print(f'{shortest_path_lengths[i]},', end='')   # 0,1,2,3,4,4,3,2,
#
#     nodes = [7,37,59,82,99,115,133,165,188,197]
#     for node in nodes:
#         print(f'{shortest_path_lengths[node]},', end='')    # 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068,

# def main():
#     heap = CustomHeap()
#     item = [5, '']
#     heap.insert(item)
#     heap.insert([7, ''])
#     heap.insert([3, ''])
#     heap.insert([2, ''])
#     heap.insert([6, ''])
#     heap.insert([1, ''])
#     heap.insert([4, ''])
#
#     print(heap.heap)
#
#     heap.delete(item)
#
#     print(heap.heap)
#
#     for _ in range(heap.size):
#         minimum = heap.extract_min()
#         print(minimum[KEY])

if __name__ == "__main__":
    main()
