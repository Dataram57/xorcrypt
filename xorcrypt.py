import random
import string
import importlib.util
import sys

spec = importlib.util.spec_from_file_location("module_name", "ikg_sha256.py")
ikg = importlib.util.module_from_spec(spec)
sys.modules["module_name"] = ikg
spec.loader.exec_module(ikg)



#================================================================
#
#                    Infinite Key Managment                    
#
#----------------------------------------------------------------

indexo = 0

def GetKeyChunk():
    global indexo
    key_size = random.randint(1, 10)  # Key size will be random between 1 and 10 bytes
    key = ""
    while key_size > 0:
        key_size -= 1
        indexo += 1
        key += str(indexo)
    return bytearray(key, 'utf-8')


#================================================================
#
#                       Basic Operations                       
#
#----------------------------------------------------------------

# Function to XOR encrypt/decrypt a file using the key generator
def XOREncryptDecrypt(input_file, output_file):
    with open(input_file, 'rb') as f_in:
        data = f_in.read()

    encrypted_data = bytearray()
    data_len = len(data)
    i = 0

    while i < data_len:
        # Generate a new key for each byte
        key = ikg.GetKeyChunk()

        # The number of bytes from the key to use
        key_len = len(key)

        # XOR the data using the current key
        j = 0
        while j < key_len:
            if i < data_len:
                encrypted_data.append(data[i] ^ key[j])
                i += 1
            else:
                break
            j += 1

    # Write the encrypted/decrypted data to the output file
    with open(output_file, 'wb') as f_out:
        f_out.write(encrypted_data)

    print(f"Operation completed. File saved as: {output_file}")

#================================================================
#
#                             Main                             
#
#----------------------------------------------------------------


# Main execution
if __name__ == "__main__":
    input_file = "input.txt"  # Replace with your file path
    key = "VERYLONGKEYAAAAAAAAAAAAAAAAAAAAAAAAAA###############***F*FHR*$@#)"
    encrypted_file = "encrypted.txt"
    decrypted_file = "decrypted.txt"

    # Encrypt the file
    ikg.SetKey(key)
    XOREncryptDecrypt(input_file, encrypted_file)
    # Decrypt the file (using the same function)
    ikg.SetKey(key)
    XOREncryptDecrypt(encrypted_file, decrypted_file)