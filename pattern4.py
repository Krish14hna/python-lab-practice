row= int(input())
for i in range (1,row+1):
    for j in range (row+1-i):
        print("",end="")
    for j in range (i):
        print("*",end="")
    for j in range (row-i):
        print("",end="")
    for j in range (i):
        print("*",end="")
    print()        

#output
'''
    *    *
   **   **
  ***  ***
 **** ****
**********'''