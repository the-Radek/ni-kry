## Generate input
To generate random inputs run
```
random_gen.py number_of_inputs output_file
```

To generate random inputs from plaintext run
```
random_input.py input_file output_file
```
## SPN
`spn.py` contains the implementation of SPN cipher. To encrypt some input run
```
spn.py [-k KEY] input_file output_file
```
To decrypt use option `-d`
```
spn.py [-k KEY] -d input_file output_file
```

## Linear cryptoanalysis

To start linear cryptoanalysis with default arguments run
```
linear.py plaintext ciphertext
```

To set your own masks change the values in the source code (find comment "DEFAULT ARGS"). The default setup is:
```
P_mask =  0b101100000000 #Plaintext bitmask
U_mask = 0b010100000101 #U mask
key_mask = 0b0101 #Sbox mask
bias = 1/32
```
## Differential cryptoanalysis

To start differential cryptoanalysis with default arguments run
```
differential.py
```

To set your own masks change the values in the source code (find comment "DEFAULT ARGS"). The default setup is:
```
enc_key=0x1345 #key for encryption - normally, this is unknown, and not used later
size = 5000 #number of plaintext block generated
deltaP = 0b0000101100000000 #what bits differ at P
expected_deltaU4 = 0b0000011000000110 #what bits must differ at U4
key_mask = 0b0101 #Sbox mask
bias = 27/1024
```