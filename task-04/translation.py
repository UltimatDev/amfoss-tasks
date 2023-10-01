def remove_occ(s):
    l=[]
    for x in s:
        l.append(x)
    l.pop(s.find("l"))
    s=""
    for x in l:
          s+=x
    return s
def check(s):
    if s.count('l')<2:
        return False
    check=0     
    if s.find('h')<s.find('e'):
            check+=1;
    if s.find('e')<s.find('l'):
            check+=1
            s=remove_occ(s)
    if s.find('e')<s.find('l'):
            check+=1
    if s.find('l')<s.find('o'):
            check+=1
    if check==4:
        return True
    else:
        return False


        
s=input().lower()


if check(s):
      print("YES")
else:
      print("NO")

