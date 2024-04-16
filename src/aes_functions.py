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
            print(f"row_val: {row_val}")
            column = [row[j] for row in pol]
            col_val = ''.join(str(item) for item in column)
            output_value = ''
            print(f"row:{i}column:{j}")
            for k in range(0,len(row_val),4):
                print(f"k: {k}")
                temp = row_val[k:k+4]
                print(f"temp: {temp}")
                pol_val = col_val[k:k+4]
                print(f"pol_val: {pol_val}")
                if pol_val == '0002':
                    val = dna_to_binary(temp)
                    rotated = val
                    print(f"rotated: {rotated}")
                    if val[0] == '1':
                        rotated = rotated+'0'
                        print(f"expanded rotated: {rotated}")
                        final_output = bin_xor(rotated,'100011011')
                        print(f"final_output before substring: {final_output}")
                        final_output = final_output[1:]
                        print(f"final_output 2.1: {final_output}")
                    else:
                        rotated = rotated+'0'
                        print(f"expanded rotated: {rotated}")
                        final_output = rotated[1:]
                        print(f"final_output 2.2: {final_output}")
                elif pol_val == '0003':
                    val = dna_to_binary(temp)
                    print(f"val in 3: {val}")
                    rotated = val
                    print(f"rotated: {rotated}")
                    if val[0] == '1':
                        rotated = rotated+'0'
                        print(f"expanded rotated: {rotated}")
                        output = bin_xor(rotated,'100011011')
                        print(f"pre-output: {output}")
                        output = output[1:]
                    else:
                        rotated = rotated+'0'
                        print(f"expanded rotated: {rotated}")
                        output = rotated[1:]
                        print(f"output in 3: {output}")
                    final_output = bin_xor(output,val)
                    print(f"final_output 3: {final_output}")
                else:
                    final_output = dna_to_binary(temp)
                    print(f"final_output 1: {final_output}")
                if k==0:
                    output_value = binary_to_dna(final_output)
                else:
                    temp2 = ''
                    print(f"output debug: {output_value}")
                    print(f"final_output_dna: {binary_to_dna(final_output)}")
                    for s in range(0,len(output_value)):
                        temp2 += dna_xor(output_value[s],binary_to_dna(final_output)[s])
                    output_value = temp2
                print(f"current output value: {output_value}")
            print(f"\noutput sent: {output_value}\n")
            result[i][j] = output_value
    return result
