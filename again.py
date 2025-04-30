from cryptography.fernet import Fernet
import os

# Generate and save a key if not already present
KEY_FILE = "secret.key"
PASSWORD_FILE = "password.txt"

def load_key():
    """Loads the encryption key from a file or generates a new one."""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
    else:
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
    return key

# Load the encryption key
key = load_key()
cipher = Fernet(key)

def save_password(password):
    """Encrypts and saves the password to a file."""
    encrypted_password = cipher.encrypt(password.encode())
    with open(PASSWORD_FILE, "wb") as file:
        file.write(encrypted_password)
    print("🔒 Password successfully encrypted and saved!")

def retrieve_password():
    """Decrypts and retrieves the password from a file."""
    if not os.path.exists(PASSWORD_FILE):
        print("❌ No password found!")
        return
    with open(PASSWORD_FILE, "rb") as file:
        encrypted_password = file.read()
    decrypted_password = cipher.decrypt(encrypted_password).decode()
    print(f"🔓 Your admin password is: {decrypted_password}")

# Example usage
action = input("Enter 'change' to update admin password or 'unlock' to reveal the password: ").strip().lower()

if action == "change":
    new_password = input("Enter new password: ")
    save_password(new_password)
elif action == "unlock":
    retrieve_password()
else:
    print("❌ Invalid option!")
