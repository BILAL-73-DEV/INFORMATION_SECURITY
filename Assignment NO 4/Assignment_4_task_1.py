# Simple RSA implementation (for learning only)
# Step 1: Choose two small prime numbers
p = 11
q = 13
# Step 2: Calculate n = p * q
n = p * q
# Step 3: Calculate Euler's Totient function
phi = (p - 1) * (q - 1)
# Step 4: Choose e (public key exponent)
e = 7   # must be coprime with phi
# Step 5: Find d (private key exponent)
# d is modular inverse of e mod phi
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
d = mod_inverse(e, phi)
print("Public Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))
# -------- ENCRYPTION FUNCTION --------
def encrypt(message, e, n):
    cipher = []
    for char in message:
        # Convert character to number (ASCII)
        m = ord(char)
        # RSA formula: c = m^e mod n
        c = pow(m, e, n)
        cipher.append(c)
    return cipher
# -------- DECRYPTION FUNCTION --------
def decrypt(cipher, d, n):
    message = ""
    for c in cipher:
        # RSA formula: m = c^d mod n
        m = pow(c, d, n)
        message += chr(m)
    return message
# -------- TEST --------
text = "ALI"   # your name or short string
print("\nOriginal Message:", text)
encrypted = encrypt(text, e, n)
print("Encrypted:", encrypted)
decrypted = decrypt(encrypted, d, n)
print("Decrypted:", decrypted)