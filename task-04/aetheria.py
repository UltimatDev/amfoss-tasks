city_num=int(input())
dist=input().split()
dist=list(dist)

for x in range(city_num):
    dist[x]=int(dist[x])

minimum_dist=min(dist)

if dist.count(minimum_dist)>1:
    print("Still Aetheria")
else:
    print(dist.index(minimum_dist)+1)