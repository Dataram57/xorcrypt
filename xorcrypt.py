import random
import string
import importlib.util
import sys

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
    data = bytearray()
    encrypted_data = bytearray()
    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        while True:
            #Generate Key
            key = ikg.GetKeyChunk()
            key_len = len(key)
            #Read chunk to xor
            data = f_in.read(key_len)
            #check EOF
            if not data:
                break
            #more info
            data_len = len(data)
            #XOR the data
            i = 0
            f = min(data_len, key_len)
            encrypted_data = bytearray()
            while i < f:
                encrypted_data.append(data[i] ^ key[i])
                i += 1
            #Write the encrypted/decrypted data to the output file
            f_out.write(encrypted_data)
    #shred
    i = len(data)
    while i > 0:
        i -= 1
        data[i] = 0x00

    print(f"Operation completed. File saved as: {output_file}")

#================================================================
#
#                             Main                             
#
#----------------------------------------------------------------

# Main execution
if __name__ == "__main__":
    if len(sys.argv) >= 4:
        #load module
        ikg_name = "ikg_sha256.py"
        if len(sys.argv) > 4:
            ikg_name = sys.argv[4]
        spec = importlib.util.spec_from_file_location("module_name", ikg_name)
        ikg = importlib.util.module_from_spec(spec)
        sys.modules["module_name"] = ikg
        spec.loader.exec_module(ikg)
        #Encrypt/Decrypt
        ikg.SetKey(sys.argv[3])
        XOREncryptDecrypt(sys.argv[1], sys.argv[2])
        #shred
        ikg.Shred()
    else:
        print("xorcrypt.py <INPUT_FILE> <OUTPUT_FILE> <KEY>")