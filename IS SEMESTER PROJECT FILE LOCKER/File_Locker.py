import hashlib
import getpass
import os

# -------------------------------
#  Vigenère Cipher (Text-based)
# -------------------------------
def vigenere_encrypt_text(text, key):
    result = []
    key = key.upper()
    k_len = len(key)
    for i, ch in enumerate(text):
        if ch.isalpha():
            shift = ord(key[i % k_len]) - ord('A')
            if ch.isupper():
                result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
            else:
                result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        else:
            result.append(ch)
    return ''.join(result)

def vigenere_decrypt_text(text, key):
    result = []
    key = key.upper()
    k_len = len(key)
    for i, ch in enumerate(text):
        if ch.isalpha():
            shift = ord(key[i % k_len]) - ord('A')
            if ch.isupper():
                result.append(chr((ord(ch) - ord('A') - shift) % 26 + ord('A')))
            else:
                result.append(chr((ord(ch) - ord('a') - shift) % 26 + ord('a')))
        else:
            result.append(ch)
    return ''.join(result)

# -------------------------------
#  Vigenère Cipher (Byte-based for PDFs/DOCX)
# -------------------------------
def vigenere_encrypt_bytes(data, key):
    key_bytes = key.encode()
    k_len = len(key_bytes)
    result = bytearray()
    for i, b in enumerate(data):
        shift = key_bytes[i % k_len]
        result.append((b + shift) % 256)
    return bytes(result)

def vigenere_decrypt_bytes(data, key):
    key_bytes = key.encode()
    k_len = len(key_bytes)
    result = bytearray()
    for i, b in enumerate(data):
        shift = key_bytes[i % k_len]
        result.append((b - shift) % 256)
    return bytes(result)

# -------------------------------
#  Password Hashing (SHA256)
# -------------------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# -------------------------------
#  Encryption (Hybrid)
# -------------------------------
def encrypt_file(file_path, key):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".txt":
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read()
        encrypted = vigenere_encrypt_text(data, key)
        new_file = file_path + ".enc"
        with open(new_file, 'w', encoding='utf-8') as f:
            f.write(encrypted)
    else:
        with open(file_path, 'rb') as f:
            data = f.read()
        encrypted = vigenere_encrypt_bytes(data, key)
        new_file = file_path + ".enc"
        with open(new_file, 'wb') as f:
            f.write(encrypted)

    print("✅ File encrypted and saved as:", new_file)

# -------------------------------
#  Decryption Functions
# -------------------------------
def decrypt_text_file(file_path, key):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
    decrypted = vigenere_decrypt_text(data, key)
    new_file = file_path.replace(".enc", "_decrypted.txt")
    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(decrypted)
    print("✅ Text file decrypted and saved as:", new_file)

def decrypt_pdf_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    decrypted = vigenere_decrypt_bytes(data, key)
    new_file = file_path.replace(".enc", "_decrypted.pdf")
    with open(new_file, 'wb') as f:
        f.write(decrypted)
    print("✅ PDF file decrypted and saved as:", new_file)

def decrypt_docx_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    decrypted = vigenere_decrypt_bytes(data, key)
    new_file = file_path.replace(".enc", "_decrypted.docx")
    with open(new_file, 'wb') as f:
        f.write(decrypted)
    print("✅ DOCX file decrypted and saved as:", new_file)

# -------------------------------
#  Dispatcher
# -------------------------------
def decrypt_file(file_path, key):
    if file_path.endswith(".txt.enc"):
        decrypt_text_file(file_path, key)
    elif file_path.endswith(".pdf.enc"):
        decrypt_pdf_file(file_path, key)
    elif file_path.endswith(".docx.enc"):
        decrypt_docx_file(file_path, key)
    else:
        print("⚠️ Unsupported file type for decryption.")

# -------------------------------
#  Main Menu
# -------------------------------
def main():
    # Stage 1: Set password
    password = getpass.getpass("Set your locker password (hidden): ")
    stored_hash = hash_password(password)
    print("🔐 Password saved securely (SHA256 hash).")

    # Stage 2: Unlock locker
    pwd = getpass.getpass("Enter password to unlock locker: ")
    if hash_password(pwd) != stored_hash:
        print("❌ Wrong password! Exiting...")
        return

    print("✅ Locker unlocked. You can now access the menu.")

    while True:
        print("\n--- File Locker Menu ---")
        print("1. Encrypt a file (requires password)")
        print("2. Decrypt a file (requires password)")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ")

        if choice in ['1', '2']:
            # Stage 3: Confirm password before action
            pwd = getpass.getpass("Enter locker password again: ")
            if hash_password(pwd) != stored_hash:
                print("❌ Wrong password! Action denied.")
                continue

            if choice == '1':
                file_path = input("Enter file path to encrypt: ")
                key = input("Enter Vigenere key: ")
                encrypt_file(file_path, key)

            elif choice == '2':
                file_path = input("Enter file path to decrypt (.enc file): ")
                key = input("Enter Vigenere key: ")
                decrypt_file(file_path, key)

        elif choice == '3':
            print("👋 Exiting File Locker. Stay safe!")
            break
        else:
            print("⚠️ Invalid choice, try again.")

# -------------------------------
#  Run Program
# -------------------------------
if __name__ == "__main__":
    main()
