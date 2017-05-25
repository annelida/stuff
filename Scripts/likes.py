def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "%s likes this" % names[0] 
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
    elif len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    else:
        return "%s, %s and %sothers like this" % (names[0], names[1], len(names)-2)
print likes(['Ann', 'Alex', 'Mark', 'Max'])
# assert likes([]), 'no one likes this'
# assert likes(['Peter']), 'Peter likes this'
# assert likes(['Jacob', 'Alex']), 'Jacob and Alex like this'
# assert likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this'
# assert likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2others like this'
