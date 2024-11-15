#!/usr/bin/python3

__author__      = "Tomas Zvara, Tomas Fornusek, Robert Lorencz, Jiri Bucek"

from random import randint
from binascii import unhexlify
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("count", type=int, help="Number of blocks to generate")
    parser.add_argument("output", help="output file")
    args = vars(parser.parse_args())

    k = 0
    with open(args['output'], 'w') as fid_out:
        for i in range(args['count']):
            a = randint(1, 65535)
            fid_out.write((f"{a:04x} "))
            k+=1
    print(f"Processed {k} blocks.")

if __name__ == "__main__":
    main()