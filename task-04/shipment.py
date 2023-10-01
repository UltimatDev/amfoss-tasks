def makelist(s):
    l=[]
    for x in s:
        l.append(int(x))
    print(l)
    return l
    

def givemax(li):
    a=max(li)

    for x in range(len(li)):
        if li[x]==a:
            li.pop(x)
    b=max(li)
    return a,b
def splitlist(lis,a,b):
    l1=[]
    l2=[]
    x=len(lis)-1
    while x>=0:
        if lis[x]==a:
            l1.append(a)
            
            
        elif lis[x]==b:
            l2.append(b)
            
        else:
            if len(l1)>len(l2):
                l2.append(lis[x])
                
            else:
                l1.append(lis[x])
                
                
        x-=1
    print(l1,l2)
    return l1,l2
t=int(input())

for x in range(t):
    length=int(input())
    s=input()
    l=makelist(s.split())
    temp=sorted(l).copy()
    a,b=givemax(temp)    
    l1,l2=splitlist(temp,a,b)
    print(a+b)