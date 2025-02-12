# encryption/homomorphic/encrypt.py
import syft as sy
from syft import he

def encrypt_data(data):
    # Create public/private keys
    context = he.context(he.scheme.CKKS, 16384, coeff_mod_bit_sizes=[60, 40, 40, 60])
    
    # Encrypt tensor
    encrypted_data = data.encrypt(context=context)
    return encrypted_data