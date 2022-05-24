st = input("enter the string").split()
e=[]
for i in st:
    if (st.count(i)>=1 and (i not in e)):
        e.append(i)
print(' '.join(e))