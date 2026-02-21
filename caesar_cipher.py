def caesar_cipher(s:str,k:int)->str:

    result=""

    k=k%26

    for c in s:

        if c.islower():
            result+=chr((ord(c)-97+k)%26+97)

        elif c.isupper():
            result+=chr((ord(c)-65+k)%26+65)

        else:
            result+=c

    return result
