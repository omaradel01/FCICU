print("Welcome to Kayles game\nThe rules of this game is as following:\nTwo players alternate turns. Every player have to remove either one or two adjacent tokens. The player who removes the last token wins.")
a=[]
x=0
i=0
y=0
while i<=10 and x<10:
    a.insert(i,x)
    i=i+1
    x=x+1
while i<=20 and  y<10:
    a.insert(i,y)
    i=i+1
    y=y+1
print()    
print(a)


while a[0] != '-' or a[1] !='-' or a[2] != '-' or a[3] != '-' or a[4] != '-' or a[5] != '-' or a[6] != '-' or a[7] != '-' or a[8] != '-' or a[9] != '-' or a[10] != '-' or a[11] != '-' or a[12] != '-' or a[13] != '-' or a[14] != '-' or a[15] != '-' or a[16] != '-' or a[17] != '-' or a[18] != '-' or a[19] != '-':
    tokens = int(input("Player 1, Enter number of tokens either 1 or 2: "))
    index = int(input("Player 1, Enter token's number: "))
    if tokens == 1:
        a.pop(index)
        a.insert(index,'-')
        print()
        print(a)
    elif tokens == 2:
        a.pop(index)
        a.pop(index)
        a.insert(index,'-')
        a.insert(index,'-')
        print()
        print(a)
    if a[0] =='-' and a[1] =='-' and a[2] =='-' and a[3] =='-' and a[4] =='-' and a[5] =='-' and a[6] =='-' and a[7] =='-' and a[8] =='-' and a[9] =='-' and a[10] =='-' and a[11] =='-' and a[12] =='-' and a[13] =='-' and a[14] =='-' and a[15] =='-' and a[16] =='-' and a[17] =='-' and a[18] =='-' and a[19] =='-':
        print("player 1 won")
        break

        
    tokens = int(input("Player 2, Enter number of tokens either 1 or 2: "))
    index = int(input("Player 2, Enter token's number: "))
    if tokens == 1:
        a.pop(index)
        a.insert(index,'-')
        print()
        print(a)
    elif tokens == 2:
        a.pop(index)
        a.pop(index)
        a.insert(index,'-')
        a.insert(index,'-')
        print()
        print(a)
    if a[0] =='-' and a[1] =='-' and a[2] =='-' and a[3] =='-' and a[4] =='-' and a[5] =='-' and a[6] =='-' and a[7] =='-' and a[8] =='-' and a[9] =='-' and a[10] =='-' and a[11] =='-' and a[12] =='-' and a[13] =='-' and a[14] =='-' and a[15] =='-' and a[16] =='-' and a[17] =='-' and a[18] =='-' and a[19] =='-':
        print("player 2 won")
        break  
    
