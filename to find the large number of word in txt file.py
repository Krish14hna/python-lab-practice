f= open("sample.txt")
data=f.read().split()
out=max(f,key=len)
print(out)