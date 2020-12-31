import string

alphabet = list(string.ascii_lowercase)

code = input("Enter code: ")

decoded = ""

for c in code:
    for v in alphabet:
        if c == 'y':
            c = 'a'
            continue
        elif c == 'z':
            c = 'b'
            continue
        if c == v:
            c = alphabet[alphabet.index(v) + 2]
            break
    decoded = decoded + c
print(decoded)