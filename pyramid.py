
start=int(11/2)
end=int(11/2 -1)
for i in range (1, 7):

    for j in range(0,9):
        if j in range(start, end):
            print("*",end='')
        else:
            print(" ",end="" )
    start-=1
    end+=1
    print("\n")