


row = int(input())
for i in range (1, row+1):
    count=65
    for j in range(i):
        print(chr(count),end="")
        count +=1
    print()

#output
# A
# AB
# ABC
# ABCD
# ABCDE    
    