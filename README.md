# Monoalphabetic Substitution Cipher — Problem 3.4

A Python implementation of the monoalphabetic substitution cipher with an interactive terminal menu. Supports encryption, decryption, three key generation methods, key validation, and letter frequency analysis.

---

## Requirements

| Tool   | Version      | Notes                        |
|--------|--------------|------------------------------|
| Python | 3.11 or later | Required to run the program  |
| pip    | 23.x or later | Comes with Python            |

No third-party libraries are required. The program uses Python's standard library only.

---

## Project Structure

```
src/
└── main.py   # All cipher logic and interactive menu
```

---

## How to Run

### Interactive Menu

```bash
python main.py
```

A terminal window will open and the menu will appear automatically.

### Menu Options

| Option | Name               | Description                                          |
|--------|--------------------|------------------------------------------------------|
| 1      | Encrypt            | Encrypts a plaintext message using the current key   |
| 2      | Decrypt            | Decrypts a ciphertext message using the current key  |
| 3      | Random key         | Generates a new random 26-letter substitution key    |
| 4      | Manual key         | Lets you type in your own 26-letter key              |
| 5      | Keyword key        | Builds a key derived from a keyword you provide      |
| 6      | Frequency analysis | Shows letter frequency statistics for any text       |
| 7      | Exit               | Closes the program                                   |

---

## Example Usage

**Generate a key from a keyword:**
```
Choose (1-7): 5
Enter keyword: CRYPTO
Key generated from keyword 'CRYPTO'.
```

**Encrypt a message:**
```
Choose (1-7): 1
Plaintext  : Hello World
Ciphertext : Btggj Cjkga
```

**Decrypt it back:**
```
Choose (1-7): 2
Ciphertext : Btggj Cjkga
Plaintext  : Hello World
```

---

## How the Cipher Works

The key is a 26-letter string where position `i` gives the cipher letter for plain letter `i`. For example, if position 0 is `Z`, then `A` encrypts to `Z`.

To decrypt, the program builds a reverse key: for each position `i` in the key, it records that cipher letter `i` maps back to plain letter `i`.

Non-letter characters (spaces, digits, punctuation) are passed through unchanged. The original case of each letter is preserved.

### Keyword Key Generation

Keyword letters are placed first in the key in the order they appear, skipping duplicates. The remaining letters of the alphabet are appended in order. This produces a key that is reproducible from the keyword.

---

## Key Validation Rules

A key entered manually must:
- Be exactly 26 letters long
- Contain only letters A–Z
- Use each letter exactly once (no duplicates)

Any violation is rejected with a descriptive error message.

---

## Troubleshooting

**Program does not start on double-click**
Right-click the file and choose *Open with > Python*. If Python is not listed, install it from [https://python.org](https://python.org) and tick *Add Python to PATH* during installation.

**Invalid key error**
The key must be exactly 26 letters, contain only A–Z, and use each letter exactly once.
