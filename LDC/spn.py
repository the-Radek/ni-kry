#!/usr/bin/python3

__author__      = "Tomas Zvara, Tomas Fornusek, Robert Lorencz, Jiri Bucek"

import argparse

def permutation(p_in):
    TRAN =[1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]
    out = 0
    for i in range(0,16):
        bit = (p_in >> i) & 1
        out |= bit << (16 - TRAN[15-i])
    return out

def do_subs(r,SBOX):
    S1i = (r & 0xF000) >> 12
    S2i = (r & 0x0F00) >> 8
    S3i = (r & 0x00F0) >> 4
    S4i = (r & 0x000F)

    S1o = SBOX[S1i]
    S2o = SBOX[S2i]
    S3o = SBOX[S3i]
    S4o = SBOX[S4i]

    out  = S1o << 12
    out |= S2o << 8
    out |= S3o << 4
    out |= S4o
    return out

def substitution_enc(r):
    SBOX = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]
    return do_subs(r, SBOX)

def substitution_dec(r):
    SBOX = [14, 3, 4, 8, 1, 12, 10, 15, 7, 13, 9, 6, 11, 2, 0, 5]
    return do_subs(r, SBOX)

def round_enc(block_in, subkey, enc_round):
    r = block_in ^ subkey
    subst = substitution_enc(r);
    if enc_round < 3:
        perm = permutation(subst)
        return perm
    return subst

def round_dec(block_in, subkey, enc_round):
    perm = block_in
    if enc_round < 3:
        perm = permutation(perm)
    subst = substitution_dec(perm);
    block_out = subst ^ subkey
    return block_out

def get_subkey(key, enc_round):
    places=4*enc_round
    f1 = (key << places) & 0xFFFF
    f2 = (key >> (16 - places)) & 0xFFFF
    res = f1 | f2
    return res

def encrypt(block_in, key):
    block_out = block_in
    for i in range(0,4):
        subkey = get_subkey(key,i)
        block_out = round_enc(block_out,subkey,i)
    block_out = block_out ^ key
    return block_out

def decrypt(block_in, key):
    block_out = block_in ^ key
    for i in range(3,-1, -1):
        subkey = get_subkey(key,i)
        block_out = round_dec(block_out,subkey,i)
    return block_out

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    parser.add_argument("output", help="output file")
    # %%%%%% DEFAULT ARGS %%%%%% #
    parser.add_argument("-k", "--key", type=lambda x: int(x,0), default=0x1515, help="key")
    parser.add_argument("-d", "--decrypt", action="store_true", help="decrypt")
    args = vars(parser.parse_args())

    k = 0
    work_function = decrypt if args['decrypt'] else encrypt

    with open(args['input'], 'r') as fid_in, open(args['output'], 'w') as fid_out:
        for in_block in fid_in.read().split():
            in_block = int(in_block, 16)
            out_block = work_function(in_block, args['key'])
            fid_out.write((f"{out_block:04x} "))
            k+=1
    print(f"Processed {k} blocks.")

if __name__ == "__main__":
    main()