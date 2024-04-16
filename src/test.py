from dna_functions import *
from aes_functions import *

DNA = "ACTG"
bin = dna_to_binary(DNA)

output = binary_to_dna(bin)

print(output)