import binascii

def string_to_big_number(s):
    hex_string = s.encode("utf-8").hex()
    return int(hex_string, 16)

def big_number_to_string(n):
    hex_string = hex(int(n))[2:]  # Remove '0x' prefix
    if len(hex_string) % 2 != 0:
        hex_string = "0" + hex_string  # Ensure even length
    byte_string = binascii.unhexlify(hex_string)
    return byte_string.decode("utf-8")

# textbook RSA encryption
# e and n are the public key of the RSA encryption
# plaintext is a number representing a string, probably generated by the usage of `string_to_big_number(s)`
def encrypt(e, n, plaintext):
    cipher = pow(plaintext, e, n)
    return cipher

if __name__ == "__main__":
    n = 27079057133799412050574271437008052479608241223378451645921828586987123275384389661190553748448131519947241422660530887207052569407854395838748787042401384171004075065289693865326335229373180653322729951129863580393632355060254900268199341538759231436658420086612699118387712385798095800079241523407995250557541194616409131909211593714204924250020714684886257490233315018260104680317027639085285801307224595400670158526070066366240039167026375801898715172465640224571404900157050983353328416661007442709676702248323670028687937388451334051028292837462090344713796045666811858601266699076083800170158980716593299585259
    e = 3
    print("Public keys:", e, n)
  
    content = "???????????????????????????????????????????????????????????"
    flag = "INS{" + content + "}"
    assert(len(flag) == 64)

    # perform the encryption
    flag_num = string_to_big_number(flag)
    encrypted_msg = encrypt(e, n, string_to_big_number(flag))
    print("Encrypted message:", encrypted_msg)