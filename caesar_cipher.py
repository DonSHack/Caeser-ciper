import sys

capital_alphabet = dict()
simple_alphabet = dict()
int_A = 65
int_a = 97
space = 32
for i in range(0,26):
    capital_alphabet[i] = chr(int_A)
    simple_alphabet[i] = chr(int_a)
    int_A += 1
    int_a +=1
def encrypt(raw_text, key):
    char_raw_text = list(raw_text)
    encrypted_text = ""
    for char in char_raw_text:
        if char in capital_alphabet.values():
            char_position = list(capital_alphabet.keys())[list(capital_alphabet.values()).index(char)]
            new_char_int = (char_position + key)%26
            encrypted_text += capital_alphabet[new_char_int]
        elif char in simple_alphabet.values():
            char_position = list(simple_alphabet.keys())[list(simple_alphabet.values()).index(char)]
            new_char_int = (char_position + key) % 26
            encrypted_text += simple_alphabet[new_char_int]
        elif char == chr(space):
            encrypted_text += chr(space)
        else:
            encrypted_text += char
    return encrypted_text
def decrypt(encrypted_text, key):
    char_raw_text = list(encrypted_text)
    decrypted_text = ""
    for char in char_raw_text:
        if char in capital_alphabet.values():
            char_position = list(capital_alphabet.keys())[list(capital_alphabet.values()).index(char)]
            new_char_int = (char_position - key) % 26
            decrypted_text += capital_alphabet[new_char_int]
        elif char in simple_alphabet.values():
            char_position = list(simple_alphabet.keys())[list(simple_alphabet.values()).index(char)]
            new_char_int = (char_position - key) % 26
            decrypted_text += simple_alphabet[new_char_int]
        elif char == chr(space):
            decrypted_text += chr(space)
        else:
            decrypted_text += char
    return decrypted_text


if __name__ == "__main__":
    try:
        key = int(input("Enter the key first: "),8)
        if key in range(0,27):
            raw_text = input("Enter the text do you want to encrypt: ")
            encrypted_text = encrypt(raw_text, key)
            print("Encrypted text: " + encrypted_text)
            print("********************************************************")
            decrypted_text = decrypt(encrypted_text,key)
            print("Decrypted text: " + decrypted_text)
        else:
            print("Key should be an Integer range in 0 to 25")
    except:
        print("Key should be an Integer")