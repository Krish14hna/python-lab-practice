count = 0
f =open("sample.txt")
n= int(input())
for i in range(n-1):
    print(f.readline())
data =f.readline()
print(data)    
f.close()     