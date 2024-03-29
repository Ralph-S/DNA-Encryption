def text_to_128bit_binary_blocks(text):
    binary_data = ''.join(format(ord(char), '08b') for char in text)
    padding_length = 128 - (len(binary_data) % 128)
    binary_data_padded = binary_data + '0' * padding_length
    binary_blocks = [binary_data_padded[i:i+128] for i in range(0, len(binary_data_padded), 128)]

    return binary_blocks

def binary_to_dna(binary_input):
    bin_to_dna = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
    dna_sequence = ''.join(bin_to_dna[binary_input[i:i+2]] for i in range(0, len(binary_input), 2))
    
    return dna_sequence

def dna_xor(dna1, dna2):
    inverse_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    # Rule 1: If the two inputs are the same, output is 'A'
    if dna1 == dna2:
        return 'A'
    # Rule 2: If one of the inputs is the inverse of the other, output is 'T'
    if inverse_map[dna1] == dna2 or inverse_map[dna2] == dna1:
        return 'T'
    # Rule 3: If one of the inputs is 'A', output is the other DNA base
    if dna1 == 'A':
        return dna2
    if dna2 == 'A':
        return dna1
    # Rule 4: If one of the inputs is 'T', output is the inverse of the other DNA base
    if dna1 == 'T':
        return inverse_map[dna2]
    if dna2 == 'T':
        return inverse_map[dna1]

    return 'Error'

def dna_rotword(word):
    return word[2:] + word[:2]
