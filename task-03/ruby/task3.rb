puts "Enter the number:"
num=gets.chomp.to_i
count=0
arry=Array.new
while num>1
	count=0
	i=2
	while(i<num)
		if (num%i==0)
			count+=1
		end
		i+=1
	end
	
    if count==0
	    arry.append(num)
    end
    num-=1
end
arry=arry.reverse()
puts arry
