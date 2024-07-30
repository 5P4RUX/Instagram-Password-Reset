import requests
import uuid
import random
import string
import os
import pyfiglet

# Colors for terminal output
RESET = '\033[0m'
GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
GREY = '\033[90m'

# Function to clear the terminal and print a banner
def print_banner(title):
    os.system('clear')  # Use 'cls' on Windows
    banner = pyfiglet.figlet_format(title, font='smslant')
    print(f"{GREY}{banner}{GREEN}                       Github: SPARUX-666 </>\n{RESET}")
    print(f"{GREEN}{'━'*67}{RESET}")

# Function to perform the password reset request
def send_reset_link(target):
    url = "https://i.instagram.com/api/v1/accounts/send_password_reset/"
    data = {
        "_csrftoken": "".join(random.choices(string.ascii_letters + string.digits, k=32)),
        "username": target,
        "guid": str(uuid.uuid4()),
        "device_id": str(uuid.uuid4())
    }
    headers = {
        "user-agent": f"Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440; {''.join(random.choices(string.ascii_letters + string.digits, k=16))}/{''.join(random.choices(string.ascii_letters + string.digits, k=16))}; {''.join(random.choices(string.ascii_letters + string.digits, k=16))}; {''.join(random.choices(string.ascii_letters + string.digits, k=16))}; {''.join(random.choices(string.ascii_letters + string.digits, k=16))}; en_GB;)"
    }

    response = requests.post(url, headers=headers, data=data)

    if "obfuscated_email" in response.text:
        print(f"{GREEN}[ > ] {response.text} {RESET}", end="")
    elif response.status_code == 404:
        print(f"{RED}Username is Not Found{RESET}", end="")
    else:
        print(f"{response.text} {RESET}", end="")

    input()

# Main function to interact with the user
def main():
    print_banner('instaResetPass')
    print(f'{BLUE}— ENTER USERNAME:{RESET} ', end="")
    target = input().strip()
    send_reset_link(target)

if __name__ == "__main__":
    main()
