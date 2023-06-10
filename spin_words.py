def spin_words(sentence):
    words = sentence.split()

    for count, word in enumerate(words):
        if len(word)>=5:
            lw = list(word)
            lw.reverse()
            words[count] = ''.join(lw)

    return ' '.join(words)


print (spin_words("hello hi goodbye"))