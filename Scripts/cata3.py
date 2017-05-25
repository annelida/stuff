def longest(s1, s2):
    s3 = s1 + s2
    result = []
    for c in s3:
        if c not in result:
            result.append(c)
            result.sort()
    print ''.join(result)
longest("xyaabbbcccdefww", "xxxxyyyabklmopq")
