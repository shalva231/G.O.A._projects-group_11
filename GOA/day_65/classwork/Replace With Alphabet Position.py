def alphabet_position(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    new = ""
    
    for i in text.lower():
        if i.isalpha():
            ind = alphabet.index(i)
            new += str(ind + 1) + " "
    return new.strip()