import sys, threading
sys.setrecursionlimit(800000)
threading.stack_size(67108864)

def dfs_topo(graph: dict, s: int, seen_nodes: set, ordered_list: list):
    seen_nodes.add(s)
    if s in graph:
        for v in graph[s]:
            if v not in seen_nodes:
                dfs_topo(graph, v, seen_nodes, ordered_list)
    ordered_list.insert(0, s)

def topo_sort(graph: dict) -> list:
    seen_nodes = set()
    ordered_list = []
    for v in graph:
        if v not in seen_nodes:
            dfs_topo(graph, v, seen_nodes, ordered_list)
    return ordered_list

def dfs_scc(graph: dict, s: int, seen_nodes: set, num_scc: int, scc: dict):
    seen_nodes.add(s)
    if num_scc in scc:
        scc[num_scc].append(s)
    else:
        scc[num_scc] = [s]
    if s in graph:
        for v in graph[s]:
            if v not in seen_nodes:
                dfs_scc(graph, v, seen_nodes, num_scc, scc)

def kosaraju(graph: dict, graph_rev: dict):
    ordered_list = topo_sort(graph_rev)
    seen_nodes = set()
    num_scc = 0
    scc = {}
    for v in ordered_list:
        if v not in seen_nodes:
            num_scc += 1
            dfs_scc(graph, v, seen_nodes, num_scc, scc)
    return scc

def read_edge_list(file_path):
    adj_list = {}
    adj_list_rev = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.split()
            tail = int(line[0])
            head = int(line[1])
            if tail not in adj_list:
                adj_list[tail] = []
            adj_list[tail].append(head)
            if head not in adj_list_rev:
                adj_list_rev[head] = []
            adj_list_rev[head].append(tail)
    return adj_list, adj_list_rev

def main():
    path = 'problem8.10.txt'
    l, l_rev = read_edge_list(path)
    components = kosaraju(l, l_rev)
    sizes = []
    for c in components:
        size = len(components[c])
        sizes.append(size)
    sizes.sort(reverse=True)
    top_five = sizes[:5]
    print(top_five) # 434821,968,459,313,211

thread = threading.Thread(target=main)
thread.start()
