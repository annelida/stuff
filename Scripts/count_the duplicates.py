def duplicate_count(text):
    d = {}
    count = 0
    text = text.lower()
    for letter in text:
        if letter in d:
            d[letter] = d[letter] + 1 
        else:
            d[letter] = 1                                                                                                                                     

    for k in d.keys():
        # print "%s: %d" % (k, d[k])
        if d[k] > 1:
            count = count + 1                                                                                                                                  
    print count           
duplicate_count("aabBcde")
