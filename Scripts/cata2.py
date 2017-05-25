def find_short(s):
    l = min([len(str) for str in s.split(" ")])
    return l
print find_short("Python is great")      
