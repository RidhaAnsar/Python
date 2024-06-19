start = 11 // 2
end = start + 1
for i in range (1, 7):

    for j in range(1,12):
        if j in range(start, end):
            print(i,end='')
        else:
            print(" ",end="" )
    start-=1
    end+=1
    print("\n")
