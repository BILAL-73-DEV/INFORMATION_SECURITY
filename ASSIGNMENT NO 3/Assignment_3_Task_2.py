# Simple ECC implementation (for learning only, not secure)
# Curve parameters: y^2 = x^3 + ax + b (mod p)
a = 2
b = 3
p = 97   # prime number (small for simplicity)
# Base point (generator)
G = (3, 6)
# Function to find modular inverse
def mod_inverse(k, p):
    # Fermat's Little Theorem
    return pow(k, p - 2, p)
# Function for point addition
def point_add(P, Q):
    if P == "O":  # Identity point
        return Q
    if Q == "O":
        return P
    x1, y1 = P
    x2, y2 = Q
    # If points are same → point doubling
    if P == Q:
        return point_double(P)
    # Calculate slope (lambda)
    m = ((y2 - y1) * mod_inverse(x2 - x1, p)) % p
    # Calculate new point
    x3 = (m*m - x1 - x2) % p
    y3 = (m*(x1 - x3) - y1) % p
    return (x3, y3)
# Function for point doubling
def point_double(P):
    if P == "O":
        return "O"
    x, y = P
    # slope formula
    m = ((3*x*x + a) * mod_inverse(2*y, p)) % p
    x3 = (m*m - 2*x) % p
    y3 = (m*(x - x3) - y) % p
    return (x3, y3)
# Scalar multiplication (k * P)
def scalar_multiply(k, P):
    result = "O"   # Identity
    temp = P
    while k > 0:
        if k % 2 == 1:
            result = point_add(result, temp)
        temp = point_double(temp)
        k = k // 2
    return result
# -------- KEY GENERATION --------
private_key = 5   # small integer
public_key = scalar_multiply(private_key, G)
print("Private Key:", private_key)
print("Public Key:", public_key)
# -------- ENCRYPTION (EC-ElGamal simplified) --------
def encrypt(message_point, public_key):
    k = 3  # random small number
    C1 = scalar_multiply(k, G)
    C2 = point_add(message_point, scalar_multiply(k, public_key))
    return (C1, C2)
# -------- DECRYPTION --------
def decrypt(cipher, private_key):
    C1, C2 = cipher
    shared = scalar_multiply(private_key, C1)
    # Inverse of shared point
    x, y = shared
    inverse_shared = (x, (-y) % p)
    message = point_add(C2, inverse_shared)
    return message
# -------- TEST MESSAGE --------
# Represent message as a point (example)
message = (10, 7)
print("\nOriginal Message:", message)
cipher = encrypt(message, public_key)
print("Encrypted:", cipher)
decrypted = decrypt(cipher, private_key)
print("Decrypted:", decrypted)