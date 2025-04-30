import os
import datetime
import random
import socket
import struct
import datetime
import string
from datetime import datetime, timezone

EXAM_END_DATE = datetime(2025, 1, 18, tzinfo=timezone.utc) 
PASSWORD_FILE = "C:\\IMPP!\\admin_password.lock" 
ADMIN_USERNAME = "undefeatable"

def generate_random_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))


def get_real_date():
    try:
        print("🌐 Connecting to Google NTP server...")
        
        NTP_SERVER = "time.google.com"
        port = 123
        msg = b'\x1b' + 47 * b'\0'

        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.settimeout(5)
        client.sendto(msg, (NTP_SERVER, port))
        data, _ = client.recvfrom(1024)

        timestamp = struct.unpack("!12I", data)[10]
        timestamp -= 2208988800 
        
        from datetime import datetime, timezone

        real_time = datetime.fromtimestamp(timestamp, timezone.utc)

        return real_time
    
    except socket.timeout:
        print("🔴 Timeout: Could not reach Google NTP server!")
        exit()
    except Exception as e:
        print(f"🔴 Error fetching real time: {e}")
        exit()


def reveal_password():
    if not os.path.exists(PASSWORD_FILE):
        print("🔴 Password file not found! Was it deleted?")
        exit()
    
    current_date = get_real_date()
    
    if current_date < EXAM_END_DATE:
        print(f"❌ You cannot retrieve the password before {EXAM_END_DATE.strftime('%Y-%m-%d')}.")
        exit()

    with open(PASSWORD_FILE, "r") as file:
        password = file.read().strip()
    
    print(f"🔓 Your admin password is: {password}")


if __name__ == "__main__":
    action = input("Enter 'change' to update admin password or 'unlock' to reveal the password: ").strip().lower()
    
    if action == "change":
        change_admin_password()
    elif action == "unlock":
        reveal_password()
    else:
        print("❌ Invalid option! Choose 'change' or 'unlock'.")
