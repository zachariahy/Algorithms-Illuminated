import math

NODE = 0
LENGTH = 1

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

def main():
    g = read_weighted_adj_list('test2.txt')
    shortest_path_lengths = dijkstra(g, 1)
    # for i in range(1, 9):
    #     print(f'{shortest_path_lengths[i]},', end='')   # 0,1,2,3,4,4,3,2,

    nodes = [7,37,59,82,99,115,133,165,188,197]
    for node in nodes:
        print(f'{shortest_path_lengths[node]},', end='')    # 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068,

if __name__ == "__main__":
    main()
