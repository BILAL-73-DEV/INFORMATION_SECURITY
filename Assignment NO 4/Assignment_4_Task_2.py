import hashlib
# -------- RSA KEY GENERATION --------
p = 11
q = 13
n = p * q
phi = (p - 1) * (q - 1)
e = 7  # public exponent
# Find modular inverse
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
d = mod_inverse(e, phi)
print("Public Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))
# -------- HASH FUNCTION --------
def hash_message(message):
    # SHA256 hashing
    hash_obj = hashlib.sha256(message.encode())
    return int(hash_obj.hexdigest(), 16)
# -------- SIGN FUNCTION --------
def sign(message, d, n):
    h = hash_message(message)
    signature = pow(h, d, n)   # sign using private key
    return signature
# -------- VERIFY FUNCTION --------
def verify(message, signature, e, n):
    h = hash_message(message)
    h_from_signature = pow(signature, e, n)  # decrypt signature
    # Compare both hashes
    return h % n == h_from_signature
# -------- TEST --------
message = "Hello"
print("\nOriginal Message:", message)
signature = sign(message, d, n)
print("Signature:", signature)
# Verify correct message
is_valid = verify(message, signature, e, n)
print("Verification (Original):", is_valid)
# -------- MODIFY MESSAGE --------
fake_message = "Hella"   # slight change
print("\nModified Message:", fake_message)
is_valid_fake = verify(fake_message, signature, e, n)
print("Verification (Modified):", is_valid_fake)