from functions import *

key = "AGGTCTTGACCCACCGAGGAGGTGTCAGGGCGGGGTTTCTACCCGAGAAAGCTATTCATTATTA"

# Example usage
text_input = "This is our testing text for AES-DNA encryption"
binary_blocks = text_to_128bit_binary_blocks(text_input)
#binary_key = ''.join(format(ord(char), '08b') for char in key)
dna_key = key

#dna_key = binary_to_dna(binary_key)
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


# for block in binary_blocks:
#     print(block)
#     dna_input = binary_to_dna(block)
#     print(f"DNA Input: {dna_input}")
#     print("\n")
