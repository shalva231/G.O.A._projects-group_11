def pig_it(text):
    words = text.split()
    pig_latin_words = []
    
    for word in words:
        if word.isalpha():
            pig_latin_word = word[1:] + word[0] + 'ay'
            pig_latin_words.append(pig_latin_word)
        else:
            pig_latin_words.append(word)
    
    return ' '.join(pig_latin_words)