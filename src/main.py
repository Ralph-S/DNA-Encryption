from functions import *

key = "AGGTCTTGACCCACCGAGGAGGTGTCAGGGCGGGGTTTCTACCCGAGAAAGCTATTCATTATTA"

# Example usage
text_input = "This is our testing text for AES-DNA encryption"
binary_blocks = text_to_128bit_binary_blocks(text_input)
#binary_key = ''.join(format(ord(char), '08b') for char in key)
dna_key = key

#dna_key = binary_to_dna(binary_key)
print(f"DNA Key: {dna_key}")

dna_keys = key_expansion(dna_key,"1")


# for block in binary_blocks:
#     print(block)
#     dna_input = binary_to_dna(block)
#     print(f"DNA Input: {dna_input}")
#     print("\n")
