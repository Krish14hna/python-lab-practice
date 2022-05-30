count = 0
f =open("sample.txt")
n= int(input())
for i in range(n):
    print(f.readline())
f.close()     