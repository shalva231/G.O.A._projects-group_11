def smash(words):
    word = ""
    count = 0
    if count < len(words):
        for i in words:
            word += i
            if i != words[-1]:
                word += " "
    return word