n=int(input("Enter Number U want to find Prime Numbers till:-"))
print("Prime Numbers Are:-")

for x in range(2,n):
    
    for i in range(2,x//2+1):#we need to only check till half the number to find if it has a factor or not 
        if x%i==0:
    
            break
    else:
        print(x)

   
