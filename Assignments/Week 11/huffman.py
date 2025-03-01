import heapq

class BinaryTreeNode:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left_child = None
        self.right_child = None

    def __lt__(self, other):
        # Allows heapq to heapify BinaryTreeNode objects by defining less than (<) comparison.
        return self.frequency < other.frequency

def huffman(symbols: list):
    forest = [BinaryTreeNode(symbol, frequency) for symbol, frequency in symbols]
    heapq.heapify(forest)
    while len(forest) >= 2:
        smallest_one = heapq.heappop(forest)
        smallest_two = heapq.heappop(forest)
        internal_node = BinaryTreeNode(None, smallest_one.frequency + smallest_two.frequency)
        internal_node.left_child = smallest_one
        internal_node.right_child = smallest_two
        heapq.heappush(forest, internal_node)
    return forest.pop()

def get_symbols_from_file(filename):
    symbols = []
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            symbols.append((count, int(line)))
            count += 1
    return symbols[1:]

def print_huffman_tree(node, prefix="", is_left=True):
    # AI-generated function for debugging
    if node is not None:
        connector = "├── " if is_left else "└── "
        if node.symbol is None:
            print(prefix + connector + f"• ({node.frequency})")  # Internal node
        else:
            print(prefix + connector + f"{node.symbol}: {node.frequency}")  # Leaf node

        # Increase prefix spacing for child nodes
        new_prefix = prefix + ("│   " if is_left else "    ")
        print_huffman_tree(node.left_child, new_prefix, True)
        print_huffman_tree(node.right_child, new_prefix, False)

def get_codes(node: BinaryTreeNode, prefix="", codes=None):
    if codes is None:
            codes = dict()

    if node is not None:
        if node.symbol is not None:
            codes[node.symbol] = prefix

        get_codes(node.left_child, prefix + "0", codes)
        get_codes(node.right_child, prefix + "1", codes)

    return codes

if __name__ == "__main__":
    # syms = get_symbols_from_file("problem14.6test1.txt")    # 2, 5
    # syms = get_symbols_from_file("problem14.6test2.txt")    # 3, 6
    syms = get_symbols_from_file("problem14.6.txt")    # 9, 19

    huffman_tree = huffman(syms)

    print_huffman_tree(huffman_tree)

    print("\nHuffman Encodings:")
    bin_codes = get_codes(huffman_tree)
    for sym in bin_codes:
        print(f"\t{sym}: {bin_codes[sym]}")

    encoding_lengths = [len(value) for value in bin_codes.values()]
    print(f"Min len encoding: {min(encoding_lengths)}\nMax len encoding: {max(encoding_lengths)}")
