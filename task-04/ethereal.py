def make_int(vector):
    temp_vector=[]
    for x in vector:
        row=[]
        for i in x:
            row.append(int(i))
        temp_vector.append(row)
    return temp_vector
n=int(input())
vector=[]
for i in range(n):
    x=raw_input()
    vector.append(x.split())
vector=make_int(vector)

l=[0,0,0]
for x in range(3):
    for i in vector:
        l=[l[0]+i[0],l[1]+i[1],l[2]+i[2]]

if l==[0,0,0]:
    print("YES")
else:
    print("NO")