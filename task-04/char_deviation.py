
def check(s):
    
    ref="amfoss"
    if s==ref:
        print(0)
        return
    else:
        dif_ind=0
        
        for i in range(len(s)):
            if s[i]!=ref[i]:
                dif_ind+=1
        print(dif_ind)
        return
n=int(input())
for x in range(n):
    check(raw_input().strip())