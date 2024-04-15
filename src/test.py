from dna_functions import bin_xor

pol = [['02','03','01','01'],
        ['01','02','03','01'],
        ['01','01','02','03'],
        ['03','01','01','02'],]

index = 1

column = [row[index] for row in pol]

cols = ''.join(str(item) for item in column)

