t = int(input())
for t in range(t):
    s = input()
    p = input()
    pList = list(p)
    temp = list(s)
    ans = 'N'
    for c,i in enumerate(pList):
        temp.remove(i)
        if pList[0] > pList[c]: 
            if c == 0:
                continue    
            ans = 'Y'
    if ans =='Y':
        temp.append(pList[0])
        temp = ('').join(sorted(temp))
        index = temp.index(pList[0])
        print(str(temp[0:index])+p+str(temp[index+1:]),end='')      
    else:
        temp.append(p)
        temp = ('').join(sorted(temp))
        print(temp,end='')