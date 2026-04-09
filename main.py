# Programming Problem 3.4 - Monoalphabetic Substitution Cipher

import random
import string

ALPHA = string.ascii_uppercase
ENG_FREQ_ORDER = "ETAOINSHRDLCUMWFGYPBVKJXQZ"


# ── Key generation ────────────────────────────────────────────────────────────

def generate_random_key():
    key = list(ALPHA)
    random.shuffle(key)
    return ''.join(key)


def generate_keyword_key(keyword):
    keyword = keyword.upper()
    seen = []
    for ch in keyword:
        if ch in ALPHA and ch not in seen:
            seen.append(ch)
    for ch in ALPHA:
        if ch not in seen:
            seen.append(ch)
    return ''.join(seen)


def validate_key(key):
    key = key.upper()
    if len(key) != 26:
        return False, "Key must be exactly 26 letters."
    if not all(c in ALPHA for c in key):
        return False, "Key must contain only letters A-Z."
    if len(set(key)) != 26:
        return False, "Key must be a permutation with no duplicate letters."
    return True, "Valid."


# ── Cipher ────────────────────────────────────────────────────────────────────

def encrypt(plaintext, key):
    result = []
    for ch in plaintext:
        if ch.isalpha():
            idx = ord(ch.upper()) - ord('A')
            enc = key[idx]
            result.append(enc if ch.isupper() else enc.lower())
        else:
            result.append(ch)
    return ''.join(result)


def decrypt(ciphertext, key):
    reverse_key = ['?'] * 26
    for i, ch in enumerate(key):
        reverse_key[ord(ch) - ord('A')] = ALPHA[i]
    result = []
    for ch in ciphertext:
        if ch.isalpha():
            idx = ord(ch.upper()) - ord('A')
            dec = reverse_key[idx]
            result.append(dec if ch.isupper() else dec.lower())
        else:
            result.append(ch)
    return ''.join(result)


# ── Frequency analysis ────────────────────────────────────────────────────────

def frequency_analysis(text):
    text = text.upper()
    counts = {ch: 0 for ch in ALPHA}
    total = 0
    for ch in text:
        if ch in ALPHA:
            counts[ch] += 1
            total += 1

    if total == 0:
        print("  No alphabetic characters found.")
        return

    sorted_chars = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    present = [(ch, n) for ch, n in sorted_chars if n > 0]

    print()
    print("  FREQUENCY ANALYSIS")
    print(f"  Total letters: {total}")
    print()
    print(f"  {'#':<4} {'Letter':<8} {'Count':<8} {'Percent':<10} {'Bar'}")
    print("  " + "-" * 52)
    for rank, (ch, count) in enumerate(present, start=1):
        pct = count / total * 100
        bar = '|' * int(pct * 2)
        print(f"  {rank:<4} {ch:<8} {count:<8} {pct:<9.1f}%  {bar}")

    print()
    cipher_order = ''.join(ch for ch, _ in present)
    print(f"  Cipher frequency order  : {cipher_order}")
    print(f"  English frequency order : {ENG_FREQ_ORDER}")
    print()
    print("  Suggested mapping (cipher -> plain):")
    print("  " + "-" * 52)
    for i, c_ch in enumerate(cipher_order):
        if i >= len(ENG_FREQ_ORDER):
            break
        print(f"  Rank {i+1:>2}:  {c_ch}  ->  {ENG_FREQ_ORDER[i]}")
    print()


# ── Display helpers ───────────────────────────────────────────────────────────

def print_header():
    print()
    print("=" * 52)
    print("  MONOALPHABETIC SUBSTITUTION CIPHER  |  Prob 3.4")
    print("=" * 52)


def print_key(key):
    print()
    print("  Current Key")
    print("  " + "-" * 52)
    print("  Plain  : " + ' '.join(ALPHA))
    print("  Cipher : " + ' '.join(key))
    print()


def print_menu():
    print("  Options")
    print("  " + "-" * 52)
    print("  1  Encrypt text")
    print("  2  Decrypt text")
    print("  3  Generate random key")
    print("  4  Enter key manually")
    print("  5  Generate key from keyword")
    print("  6  Frequency analysis")
    print("  7  Exit")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print_header()
    key = ALPHA  # default: identity mapping

    while True:
        print_key(key)
        print_menu()
        choice = input("  Choose (1-7): ").strip()
        print()

        if choice == '1':
            text = input("  Plaintext  : ")
            result = encrypt(text, key)
            print()
            print("  " + "-" * 52)
            print(f"  Plaintext  : {text}")
            print(f"  Key used   : {key}")
            print(f"  Ciphertext : {result}")
            print("  " + "-" * 52)

        elif choice == '2':
            text = input("  Ciphertext : ")
            result = decrypt(text, key)
            print()
            print("  " + "-" * 52)
            print(f"  Ciphertext : {text}")
            print(f"  Key used   : {key}")
            print(f"  Plaintext  : {result}")
            print("  " + "-" * 52)

        elif choice == '3':
            key = generate_random_key()
            print("  New random key generated.")

        elif choice == '4':
            new_key = input("  Enter 26-letter key: ").strip().upper()
            valid, msg = validate_key(new_key)
            if valid:
                key = new_key
                print("  Key accepted.")
            else:
                print(f"  Error: {msg}")

        elif choice == '5':
            kw = input("  Enter keyword: ").strip()
            key = generate_keyword_key(kw)
            print(f"  Key generated from keyword '{kw}'.")

        elif choice == '6':
            text = input("  Text to analyse: ")
            frequency_analysis(text)

        elif choice == '7':
            print("  Goodbye.")
            break

        else:
            print("  Invalid choice. Please enter a number from 1 to 7.")

        print()


if __name__ == "__main__":
    main()
