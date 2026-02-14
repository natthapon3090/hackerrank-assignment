def caesar_cipher(s: str, k: int) -> str:
    result = ""
    k = k % 26

    for char in s:
        if char.isupper():
            result += chr((ord(char) - ord('A') + k) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        else:
            result += char

    return result

