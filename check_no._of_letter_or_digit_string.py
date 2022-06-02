str=(input())
countletter= 0
countdigit=0
str.lower()
for i in str:
    if i.isnumeric():
        countdigit+=1
    else:
        countletter+=1    

print(f"leter={countletter}")    
print(f"digit={countdigit}")    