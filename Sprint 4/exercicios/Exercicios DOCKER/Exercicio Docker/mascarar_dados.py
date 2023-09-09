import hashlib

def calcular_hash():
    input_string = input()
    
    if input_string.lower() == 'sair':
        return

    sha1_hash = hashlib.sha1(input_string.encode()).hexdigest()
    print("Hash SHA-1:", sha1_hash)

    calcular_hash()

calcular_hash()
