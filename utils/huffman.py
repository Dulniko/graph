import heapq
from collections import Counter, defaultdict


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    frequencies = Counter(text)
    priority_queue = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(priority_queue, merged)

    return priority_queue[0]


def assign_codes_to_characters(node, prefix="", code=None):
    if code is None:
        code = defaultdict(str)
    if node is not None:
        if node.char is not None:
            code[node.char] = prefix
        assign_codes_to_characters(node.left, prefix + "0", code)
        assign_codes_to_characters(node.right, prefix + "1", code)
    return code


def encode_text(text, codes):
    return "".join(codes[char] for char in text)


def decode_text(encoded_text, root):
    current_node = root
    decoded_output = []

    for bit in encoded_text:
        current_node = current_node.left if bit == "0" else current_node.right
        if current_node.char is not None:
            decoded_output.append(current_node.char)
            current_node = root

    return "".join(decoded_output)


if __name__ == "__main__":
    text = "Ala ma kota a kot ma ale"
    root = build_huffman_tree(text)
    codes = assign_codes_to_characters(root)
    encoded_text = encode_text(text, codes)
    decoded_text = decode_text(encoded_text, root)

    print("Kody Huffmana:", codes)
    print("Tekst zakodowany:", encoded_text)
    print("Tekst odkodowany:", decoded_text)
