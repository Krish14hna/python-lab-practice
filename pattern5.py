r=int(input())
k=1
for i in range (1,r+1):
    for j in range (i):
        print(k,end="")
        k+=1
        if k>10:
            k=1
    print()        
'''
5
1
23
456
78910
12345
'''