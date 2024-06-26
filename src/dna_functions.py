dna_sbox = {
    "AA": "CGATCTTACTCTCTGTTTAGCGGTCGTTTACCATAAAAACCGCTAGGTTTTGTCCTGGGTCTCG",
    "AC": "TAGGGAAGTAGCCTTCTTGGCCGCCACTTTAAGGTCTCCAGGAGGGTTGCTAGGCACTAGTAAA",
    "AG": "GTCTTTTCGCATAGCGATCGATTTTTCTTATAATCAGGCCTGCCTTACCTACTCGAATACACCC",
    "AT": "AACATACTAGATTAATACGAGCCGAACCGCGGAACTACAGGAAATGAGTGGTAGCTGTAGCTCC",
    "CA": "AAGCGAATAGTAACGGACGTCGTGCCGGGGAACCAGATGTTCCGGTATAGGCTGATAGTTGACA",
    "CC": "CCATTCACAAAATGTCAGAATTTAGTACCCGTCGGGTAGTGTTGATGCCAGGCATACCGATATT",
    "CG": "TCAATGTTGGGGTTGTCAATCATCATATGACCCACCTTGCAAAGCTTTCCAAATTAGCTTGGGA",
    "CT": "CCACGGATCAAAGATTGCAGGCTCATGATTCCGTTAGTCGTCGGAGACACAATTTTTTATTCAG",
    "GA": "TATCAATAACATTGTACCTTGCCTCACAACCTTACAGGCTCTTGATTCCGCACCTCACGCCTAT",
    "GC": "CGAAGAACCATTTCTAAGAGAGGGGCAAGAGACACGTGTGGTGAACCATCTGCCTGAAGTTCGT",
    "GG": "TGAAATAGATGGAAGGCAGCAACGAGCACCTATAAGTCATGGTACGAGGCACGCCCTGCACTGC",
    "GT": "TGCTTAGAATCTCGTCGATCTCCCCATGGGGCCGTACCCGTTCATGGGCGCCCTGGGGTGAAGA",
    "TA": "GTGGCTGAAGCCAGTGACTAGGCGGTCATACGTGGATCTCCTCAACTTCAGTGTTCGAGTGAGG",
    "TC": "CTAAATTGGTCCCGCGCAGAAAATTTCGAATGCGACATCCCCCTGTGCGACGTAACACTCGCTG",
    "TG": "TGACTTGAGCGAACACCGGCTCGCGATGGCCAGCGTACTGGACTTGGCTATGCCCCAGGATCTT",
    "TT": "GATAGGACGAGCAATCGTTTTGCGCAAGCGGACAACGCGCAGTCAATTGTAACCCAGTGTACCG"
}

R_con={
    "1":"AAACAAAAAAAAAAAA",
    "2":"AAAGAAAAAAAAAAAA",
    "3":"AACAAAAAAAAAAAAA",
    "4":"AAGAAAAAAAAAAAAA",
    "5":"ACAAAAAAAAAAAAAA",
    "6":"AGAAAAAAAAAAAAAA",
    "7":"CAAAAAAAAAAAAAAA",
    "8":"GAAAAAAAAAAAAAAA",
    "9":"ACGTAAAAAAAAAAAA",
    "10":"ATCGAAAAAAAAAAAA"
}

def hex_to_binary(hex_string):
    hex_values = hex_string.split()
    binary_values = [bin(int(h,16))[2:].zfill(8) for h in hex_values]
    binary_string = ''.join(binary_values)
    
    return binary_string

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

def dna_to_binary(dna_input):
    dna_to_bin = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}
    bin_sequence = ''.join(dna_to_bin[dna_input[i:i+1]] for i in range(0, len(dna_input)))
    
    return bin_sequence

def dna_xor(dna1, dna2):
    inverse_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    # Rule 1
    if dna1 == dna2:
        return 'A'
    # Rule 2
    if inverse_map[dna1] == dna2 or inverse_map[dna2] == dna1:
        return 'T'
    # Rule 3
    if dna1 == 'A':
        return dna2
    if dna2 == 'A':
        return dna1
    # Rule 4
    if dna1 == 'T':
        return inverse_map[dna2]
    if dna2 == 'T':
        return inverse_map[dna1]

    return 'Error'

def bin_xor(str1,str2):
    answer = ''
    for i in range(0,len(str1)):
        if (str1[i] == '0' and str2[i] == '0') or (str1[i] == '1' and str2[i] == '1'):
            answer += '0'
        else:
            answer += '1'
    return answer

def move_pointer(dna_input):
    first_character_moves = {"A":0,"C":4,"G":8,"T":12}
    second_character_moves = {"A":0,"C":1,"G":2,"T":3}
    total_moves = first_character_moves[dna_input[2]]+second_character_moves[dna_input[3]]
    return total_moves

def get_substitution(dna_key):
    sbox_key = dna_key[:2]
    move=move_pointer(dna_key)
    sbox_value = dna_sbox[sbox_key]
    position=move*4
    return sbox_value[position:position+4:1]

def key_expansion(key,round,resa,resb,resc,resd):
    keys=[]
    sub_key= [key[i:i+16] for i in range(0,64,16)]
    to_rotate = sub_key[3]
    rotated = to_rotate[4:] + to_rotate[:4]
    rotated_bytes = [rotated[i:i+4] for i in range(0,16,4)]
    first=sub_key[0]
    second=sub_key[1]
    third=sub_key[2]
    fourth=sub_key[3]
    res1=""
    res2=""
    res3=""
    res4=""
    temp=""
    for k,element in enumerate(rotated_bytes):
        temp+=get_substitution(element)
        row=R_con[round]
    xored=""
    for i in range(0,16):
        xored+=dna_xor(row[i],temp[i])
    for j in range(0,16):
        if round == "1":
            res1+=dna_xor(xored[j],first[j])
        else:
            res1+=dna_xor(xored[j],resa[j])
    keys.append(res1)
    
    for j in range(0,16):
        if round == "1":
            res2+=dna_xor(second[j],res1[j])
        else:
            res2+=dna_xor(resb[j],res1[j])
    keys.append(res2)

    for j in range(0,16):
        if round == "1":
            res3+=dna_xor(third[j],res2[j])
        else:
            res3+=dna_xor(resc[j],res2[j])
    keys.append(res3)
        
    for j in range(0,16):
        if round == "1":
            res4+=dna_xor(fourth[j],res3[j])
        else:
            res4+=dna_xor(resd[j],res3[j])
    keys.append(res4)
    return keys