#!/usr/bin/python3

__author__      = "Tomas Zvara, Tomas Fornusek, Robert Lorencz, Jiri Bucek"

from random import randint
from binascii import unhexlify
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    parser.add_argument("output", help="output file")
    args = vars(parser.parse_args())

    k = 0
    with open(args['input'], 'r') as fid_in, open(args['output'], 'w') as fid_out:
        while True:
            word = fid_in.read(2)
            if not word or len(word) != 2: #EOF
                break
            a = ord(word[0])*256 + ord(word[1])
            a += randint(1, 255)
            fid_out.write((f"{a:04x} "))
            k+=1
    print(f"Processed {k} blocks.")

if __name__ == "__main__":
    main()