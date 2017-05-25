def unique_in_order(iterable):
    result = []
    for c in iterable:
        if not result or c != result[-1]:
            result.append(c)
    return result
print unique_in_order('AAAABBBCCDAABBB')
      
