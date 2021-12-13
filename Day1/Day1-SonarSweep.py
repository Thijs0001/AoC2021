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

windows=[]
i=0
while i in range(0,len(depths)-2):
	windowtotal=depths[i]+depths[i+1]+depths[i+2]
	windows.append(windowtotal)
	i+=1

windowincrease=[]
i=0
while i in range(0,len(windows)):
	if i!=0:
		windowincrease.append(windows[i]>windows[i-1])
	else:
		windowincrease.append("")
	i+=1

print(windowincrease.count(True))