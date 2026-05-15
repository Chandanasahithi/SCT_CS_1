#task 1
def encrypt(text, shift):
    result = ""

    for char in text:

        if char.isalpha():

            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char

        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


print("===== Caesar Cipher Tool =====")

choice = input("Type 'e' for Encrypt or 'd' for Decrypt: ")

message = input("Enter your message: ")

shift = int(input("Enter shift value: "))

if choice.lower() == 'e':

    encrypted = encrypt(message, shift)

    print("\nEncrypted Message:")
    print(encrypted)

elif choice.lower() == 'd':

    decrypted = decrypt(message, shift)

    print("\nDecrypted Message:")
    print(decrypted)

else:
    print("Invalid Choice")