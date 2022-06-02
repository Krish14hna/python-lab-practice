def lacky_name(n):
    a="aeiou"
    for i in a:
        if i in n:
            return True
        else:
            return False    

name= input()
print((lacky_name(name)))