from dna_functions import *
from aes_functions import *

key = "AGGTCTTGACCCACCGAGGAGGTGTCAGGGCGGGGTTTCTACCCGAGAAAGCTATTCATTATTA"

# Example usage
text_input = "This is our testing text for AES-DNA encryption"
binary_blocks = text_to_128bit_binary_blocks(text_input)
dna_input = []
for ele in binary_blocks:
    x = binary_to_dna(ele)
    dna_input.append(x)
    

dna_key = key

#dna_key = binary_to_dna(binary_key)
print(f"DNA Key: {dna_key}")
rounds=1
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
        print(prev + "\n")
    else:
        #break
        result = key_expansion(prev,str(i),res1,res2,res3,res4)
        res1=result[0]
        res2=result[1]
        res3=result[2]
        res4=result[3]
        prev = res1+res2+res3+res4
        print(prev + "\n")


print("#######################################################")

input_matrix = [['' for _ in range(4)] for _ in range(4)]
key_matrix = [['' for _ in range(4)] for _ in range(4)]
state_input = fill_matrix(input_matrix,dna_input[0])
state_key = fill_matrix(key_matrix,key)
print(state_input)
print(state_key)

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

prev = ""
for r in range(1,rounds+1):
    subbed_matrix = [['' for _ in range(4)] for _ in range(4)]
    rotated_matrix = [['' for _ in range(4)] for _ in range(4)]
    for i in range(0,len(input_matrix)):
        for j in range(len(input_matrix[0])):
            if r == 1:
                prev = xored_matrix[i][j]
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
        