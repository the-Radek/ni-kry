#!/usr/bin/env python3

# This is a fake vulnerable server for the padding oracle attack.
# You can use it to debug your attack before trying it over the network.

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import sys

# intercepted message:
correct_ct = bytes.fromhex(
    "2e9f47e4969aec3bb655ee2c168a5feff4e51831191cbf59303602a371ff769e321842dfb1f5d68e936ec3c63a26d7a3bdf88b03369efd565aa9f90d7d267192b84d88e47f2176015a451920cc71033e65da77428139221aa60a458e045f84c3"
)

# secret plaintext message with removed padding:
correct_pt = bytes.fromhex(
    "54686973206d757374206d6174636820776861746576657220776173206465637279707465642c206f74686572776973652049207468726f7720616e206572726f722e"
)


def decrypt_and_check(msg: bytes):
    """
    Decrypts and checks a ciphertext message

    Parameters
    ----------
    msg: bytes
        raw binary message including IV

    Returns
    -------
    code
        200 = OK, 404 = message integrity error, 400 = padding error
    """
    # secret key:
    key = bytes.fromhex("16beb74795960b2245f8f0117db930a8")
    # iv is the first block of encrypted message:
    iv = msg[0:16]
    # the remaining ciphertext:
    ct = msg[16:]
    # first decrypt the ct:
    aes = AES.new(key, AES.MODE_CBC, iv)
    dt = aes.decrypt(ct)
    # remove and check the padding:
    try:
        dt_unpad = unpad(dt, 16)
    except:
        # padding is wrong, report padding error:
        return 400  # Padding oracle here!
    # check if the decrypted message is correct:
    if dt_unpad == correct_pt:
        return 200
    # else return message integrity error:
    return 404


# you can run this as a standalone script, then pass the hex string of the message as the first argument.
if __name__ == "__main__":
    if len(sys.argv) < 2:
        # no argument, do a check on the correct message
        ret = decrypt_and_check(correct_ct)  # should return 200
    else:
        # argument passsed, check the supplied message
        ret = decrypt_and_check(bytes.fromhex(sys.argv[1]))
    # print the error code
    print(ret)
    # also return it as exit status
    sys.exit(ret)
