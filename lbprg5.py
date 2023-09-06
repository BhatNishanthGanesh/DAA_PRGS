#5.Develop a program  for the following:
#a.To construct a Huffman code for a given English text and encode it .
# To decode an English text which has been encoded with a Huffman code

import heapq

class HuffmanNode:
    def __init__(self,char,freq):
        self.char=char
        self.freq=freq
        self.Left=None
        self.right=None
    def __lt__(self,others):
        return self.freq<others.freq
    
def Build_huffman_tree(characters,frequencies):
    heap=[]
    for i in range(len(characters)):
        node=HuffmanNode(characters[i],frequencies[i])
        heapq.heappush(heap,node)
    while len(heap)>1:
        left_node=heapq.heappop(heap)
        right_node=heapq.heappop(heap)
        combined_freq=left_node.freq+right_node.freq
        combined_node=HuffmanNode(None,combined_freq)
        combined_node.Left=left_node
        combined_node.right=right_node
        heapq.heappush(heap,combined_node)
    return heapq.heappop(heap)

def build_huffman_codes(root,current_codes,huffman_codes):
    if root is None:
        return 
    elif root.char is not None:
        huffman_codes[root.char]=current_codes
        return
    
    build_huffman_codes(root.Left,current_codes+'0',huffman_codes)
    build_huffman_codes(root.right,current_codes+'1',huffman_codes)

def encode_string(string,huffman_codes):
    encoded_string=''
    for char in string:
        encoded_string+=huffman_codes[char]
    return encoded_string

def decode_string(encoded_string,root):
    decoded_string=''
    current_node=root
    for bit in encoded_string:
        if bit=='0':
            current_node=current_node.Left
        else:
            current_node=current_node.right
        if current_node.char is not None:
           decoded_string+=current_node.char
           current_node=root
    return decoded_string

n=int(input("Enter the total number of characters: "))
characters=[]
frequencies=[]
for i in range(n):
    char=input("Enter a character: ")
    freq=float(input("Enter the probability: "))
    characters.append(char)
    frequencies.append(freq)
huffman_codes={}
huffman_tree=Build_huffman_tree(characters,frequencies)
build_huffman_codes(huffman_tree,'',huffman_codes)
string=input("Enter a string to encode ")
encoded_string=encode_string(string,huffman_codes)
print("Huffman codes: ")
for char,code in huffman_codes.items():
    print(char,":",code)
print("Encoded string is: ",encoded_string)
y=input("Do you want to decode the encoded string? (y/n):")
if y.lower()=='y':
    decoded_string=decode_string(encoded_string,huffman_tree)
    print("The decoded string is : ",decoded_string)
choice=input("Do you want to decode the binary number:(y/n) ")
if choice.lower()=='y':
    binary_number=input("Enter the binary number to decode")
    decoded_new_string=decode_string(binary_number,huffman_tree)
    print("The decoded binary number is: ",decoded_new_string)