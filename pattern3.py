row= int(input())
count=1
for i in range (1,row+1):
    for j in range(i):
        print(count,end="")
        count+=1
    print()     

# output
'''
1
23
456
78910
1112131415'''