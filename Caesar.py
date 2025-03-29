def encrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabetic characters are unchanged

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    print("Welcome to the Caesar Cipher program!")
    choice = input("Do you want to Encrypt or Decrypt? (e/d): ").lower()
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        encrypted_text = encrypt(text, shift)
        print(f"Encrypted Text: {encrypted_text}")
    elif choice == 'd':
        decrypted_text = decrypt(text, shift)
        print(f"Decrypted Text: {decrypted_text}")
    else:
        print("Invalid choice!")


# Corrected the following line
if __name__ == "__main__":
    main()