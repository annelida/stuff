def vowel_indices(word):
    res = []
    index = 0

    for vowel in word:
        index += 1

        if vowel.lower() in 'aeiouy':
            res.append(index)
    print res
vowel_indices("bialy")
