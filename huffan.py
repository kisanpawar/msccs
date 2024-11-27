import heapq

# Node structure for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Comparator for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

# Function to generate Huffman codes
def huffman_codes(frequency_map):
    # Create a priority queue
    heap = [Node(char, freq) for char, freq in frequency_map.items()]
    heapq.heapify(heap)

    # Build the Huffman tree
    while len(heap) > 1:
        # Extract two nodes with the lowest frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Merge the two nodes
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Add the merged node back to the heap
        heapq.heappush(heap, merged)

    # The root of the Huffman tree
    root = heap[0]

    # Generate codes from the tree
    codes = {}
    _generate_codes(root, "", codes)
    return codes

# Helper function to recursively generate codes
def _generate_codes(node, current_code, codes):
    if not node:
        return

    # If it's a leaf node, store the character's code
    if node.char is not None:
        codes[node.char] = current_code

    # Traverse left and right
    _generate_codes(node.left, current_code + "0", codes)
    _generate_codes(node.right, current_code + "1", codes)

# Example usage
def main():
    text = "huffman coding algorithm"
    
    # Count the frequency of each character
    frequency_map = {}
    for char in text:
        frequency_map[char] = frequency_map.get(char, 0) + 1

    # Generate Huffman codes
    codes = huffman_codes(frequency_map)

    # Display the Huffman codes
    print("Character\tHuffman Code")
    for char, code in codes.items():
        print(f"{repr(char)}\t\t{code}")

    # Encoding the text
    encoded_text = "".join(codes[char] for char in text)
    print("\nEncoded Text:", encoded_text)

    # Decoding the encoded text
    decoded_text = decode_text(encoded_text, codes)
    print("\nDecoded Text:", decoded_text)

# Function to decode the encoded text using the Huffman codes
def decode_text(encoded_text, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    current_code = ""
    decoded_text = ""

    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""

    return decoded_text

if __name__ == "__main__":
    main()
