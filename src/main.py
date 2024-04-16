from dna_functions import *
from aes_functions import *

def run(text_from_user,key_from_user):
    key_binary = hex_to_binary(key_from_user)
    key = binary_to_dna(key_binary)
    
    # Example usage
    text_input = text_from_user
    binary_blocks = text_to_128bit_binary_blocks(text_input)
    dna_input = []
    for ele in binary_blocks:
        x = binary_to_dna(ele)
        dna_input.append(x)
    print(dna_input)

    dna_key = key

    print(f"DNA Key: {dna_key}")
    rounds=10
    keys_list=[]
    res1=""
    res2=""
    res3=""
    res4=""
    val = dna_key
    prev=""

    for i in range(1,rounds+1):
        if i==1:
            result = key_expansion(val,str(i),res1,res2,res3,res4)
            res1=result[0]
            res2=result[1]
            res3=result[2]
            res4=result[3]
            prev = res1+res2+res3+res4
            keys_list.append(prev)
        else:
            result = key_expansion(prev,str(i),res1,res2,res3,res4)
            res1=result[0]
            res2=result[1]
            res3=result[2]
            res4=result[3]
            prev = res1+res2+res3+res4
            keys_list.append(prev)

    print("#"*100)
    list_output = []
    for a in range(len(dna_input)):
        input_matrix = [['' for _ in range(4)] for _ in range(4)]
        key_matrix = [['' for _ in range(4)] for _ in range(4)]
        state_input = fill_matrix(input_matrix,dna_input[a])
        state_key = fill_matrix(key_matrix,key)

        xored_matrix = [['' for _ in range(4)] for _ in range(4)]
        for i in range(len(input_matrix)):
            for j in range(len(input_matrix[0])):
                block1 = input_matrix[i][j]
                block2 = key_matrix[i][j]
                xored = ""
                for k in range(0,len(input_matrix[i][j])):
                    first = block1[k:k+1]
                    second = block2[k:k+1]
                    xored += dna_xor(first,second)
                xored_matrix[i][j] = xored
        print(xored_matrix)

        x = [['' for _ in range(4)] for _ in range(4)]
        prev = ""
        round_output = [['' for _ in range(4)] for _ in range(4)]
        for r in range(1,rounds+1):
            print(f"Round: {r}")
            subbed_matrix = [['' for _ in range(4)] for _ in range(4)]
            rotated_matrix = [['' for _ in range(4)] for _ in range(4)]
            for i in range(0,len(input_matrix)):
                for j in range(len(input_matrix[0])):
                    if r == 1:
                        prev = xored_matrix[i][j]
                    else:
                        prev = x[i][j]
                    subbed_matrix[i][j] = get_substitution(prev)
                if i==0:
                    val = ''.join(subbed_matrix[i])
                    rotated = val[0:] + val[:0]
                elif i==1:
                    val = ''.join(subbed_matrix[i])
                    rotated = val[4:] + val[:4]
                elif i==2:
                    val = ''.join(subbed_matrix[i])
                    rotated = val[8:] + val[:8]
                else:
                    val = ''.join(subbed_matrix[i])
                    rotated = val[12:] + val[:12]
                result = [rotated[k:k+4] for k in range(0,len(rotated),4)]
                rotated_matrix[i] = result
            print(f"rotated_matrix: {rotated_matrix}")
            
            if r!=10:
                mixed = mix_columns(rotated_matrix)
            print(mixed)
            
            round_key_matrix = [['' for _ in range(4)] for _ in range(4)]
            round_key = keys_list[r-1]
            round_key_matrix = fill_matrix(round_key_matrix,round_key)
            for i in range(0,len(mixed)):
                for j in range(len(mixed[0])):
                    block1 = mixed[i][j]
                    block2 = round_key_matrix[i][j]
                    xored = ""
                    for k in range(0,len(mixed[i][j])):
                        first = block1[k:k+1]
                        second = block2[k:k+1]
                        xored += dna_xor(first,second)
                    round_output[i][j] = xored
            print(round_output)
            x = round_output
        list_output.append(round_output)
    return list_output