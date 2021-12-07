depths=[]
i=1
while i!=0:
    i = int(input())
    depths.append(i)
    
depths.pop()

increase=[]
i=0
while i in range (0,len(depths)):
	if i != 0:
		increase.append(depths[i]>depths[i-1])
	else:
		increase.append("")
	i+=1

print(increase.count(True))