from dna_functions import dna_to_binary, binary_to_dna, dna_xor, bin_xor

pol = [['0002','0003','0001','0001'],
        ['0001','0002','0003','0001'],
        ['0001','0001','0002','0003'],
        ['0003','0001','0001','0002'],]

def fill_matrix(matrix, block):
    counter = 4
    for i in range(0,len(block),counter):
        index = i // counter
        column = index // 4
        row = index % 4
        matrix[row][column] = block[i:i+4]
    return matrix

def decimalToBinary(n): 
    bin_str = bin(n).replace("0b", "") 
    x = bin_str.zfill(4)
    return x

def mix_columns(matrix):
    result = [['' for _ in range(4)] for _ in range(4)]
    for i in range(0,len(matrix)):
        for j in range(len(pol[0])):
            row_val = ''.join(str(item) for item in matrix[i])
            column = [row[j] for row in pol]
            col_val = ''.join(str(item) for item in column)
            output_value = ''
            for k in range(0,len(row_val),4):
                print(f"k: {k}")
                temp = row_val[k:k+4]
                pol_val = col_val[k:k+4]
                if pol_val == '0002':
                    val = dna_to_binary(temp)
                    rotated = val
                    if val[0] == '1':
                        rotated = rotated+'0'
                        final_output = bin_xor(rotated,'100011011')
                        final_output = final_output[1:]
                    else:
                        rotated = rotated+'0'
                        final_output = rotated[1:]
                elif pol_val == '0003':
                    val = dna_to_binary(temp)
                    rotated = val
                    if val[0] == '1':
                        rotated = rotated+'0'
                        output = bin_xor(rotated,'100011011')
                        output = output[1:]
                    else:
                        rotated = rotated+'0'
                        output = rotated[1:]
                    final_output = bin_xor(output,val)
                else:
                    final_output = dna_to_binary(temp)
                if k==0:
                    output_value = binary_to_dna(final_output)
                else:
                    temp2 = ''
                    for s in range(0,len(output_value)):
                        temp2 += dna_xor(output_value[s],binary_to_dna(final_output)[s])
                    output_value = temp2
                print(f"current output value: {output_value}")
            print(f"\noutput sent: {output_value}\n")
            result[i][j] = output_value
    return result
