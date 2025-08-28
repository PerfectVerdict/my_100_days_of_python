alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    original_text = list(original_text)
    shifted_text = []

    for letter in original_text:
        idx = alphabet.index(letter)
        # shifted_idx = idx + shift
        shifted_idx = (idx + shift) % 26
        shifted_text.append(alphabet[shifted_idx])

    print(shifted_text)

encrypt(text, shift)

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?


