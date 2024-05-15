import heapq
from collections import Counter, defaultdict


class HuffmanCoding:
    class Node:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        def __lt__(self, other):
            return self.freq < other.freq

    def __init__(self, text):
        """As parameter it takes a text, that we want to encode."""
        self.text = text
        self.root = self.build_huffman_tree(text)
        self.codes = self.assign_codes_to_characters(self.root)

    def build_huffman_tree(self, text):
        """
        Builds the Huffman tree based on the provided text.

        Returns an array (priority queue) with characters from given text and its frequency.
        """
        frequencies = Counter(text)
        priority_queue = [self.Node(char, freq) for char, freq in frequencies.items()]
        heapq.heapify(priority_queue)

        while len(priority_queue) > 1:
            left = heapq.heappop(priority_queue)
            right = heapq.heappop(priority_queue)

            merged = self.Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right

            heapq.heappush(priority_queue, merged)

        return priority_queue[0]

    def assign_codes_to_characters(self, node, prefix="", code=None):
        """
        Assigns binary codes to characters based on the Huffman tree.

        Returns the root node of the constructed Huffman tree
        """
        if code is None:
            code = defaultdict(str)
        if node is not None:
            if node.char is not None:
                code[node.char] = prefix
            self.assign_codes_to_characters(node.left, prefix + "0", code)
            self.assign_codes_to_characters(node.right, prefix + "1", code)
        return code

    def encode_text(self):
        """Returns an encoded text using the Huffman tree as String"""
        return "".join(self.codes[char] for char in self.text)

    def decode_text(self, encoded_text):
        """
        Decodes an encoded text using the Huffman tree.

        Returns a decoded text as String
        """
        current_node = self.root
        decoded_output = []

        for bit in encoded_text:
            current_node = current_node.left if bit == "0" else current_node.right
            if current_node.char is not None:
                decoded_output.append(current_node.char)
                current_node = self.root

        return "".join(decoded_output)
