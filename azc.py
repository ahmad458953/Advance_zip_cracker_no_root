import zipfile
import itertools
import string

charset = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation

zip_path = input("Enter zip file path: ")

def try_password(zf, name, password):
    try:
        zf.read(name, pwd=password.encode())
        return True
    except:
        return False

with zipfile.ZipFile(zip_path) as zf:
    first_file = zf.namelist()[0]
    found = False
    length = 1
    attempt = 0

    try:
        while not found:
            for combo in itertools.product(charset, repeat=length):
                guess = ''.join(combo)
                attempt += 1
                if attempt % 10000 == 0:
                    print(f"[~] Tried {attempt} passwords... (last: {guess})")
                if try_password(zf, first_file, guess):
                    print(f"[+] Password found: {guess}")
                    found = True
                    break
            length += 1
    except KeyboardInterrupt:
        print("\n[!] Stopped by user.")
