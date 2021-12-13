grid=[]
x=0
while x in range(0,10):
	y=0
	grid.append([])
	while y in range(0,10):
		grid[x].append(0)
		y+=1
	x+=1 

lines=[]
x=0
i=input()
while i!="0":
	q=i.split(" -> ") 
	lines.append([])
	n=0
	while n in range(0,2):
		y=q[n].split(",")
		lines[x].append(y)
		n+=1
	i=input()
	x+=1

i=0
while i in range(0,len(lines)):
	#x1=min(int(lines[i][0][0]),int(lines[i][1][0]))
	#x2=max(int(lines[i][0][0]),int(lines[i][1][0]))
	#y1=min(int(lines[i][0][1]),int(lines[i][1][1]))
	#y2=max(int(lines[i][0][1]),int(lines[i][1][1]))
	(x1,y1)=min((int(lines[i][0][0]),int(lines[i][0][1])),(int(lines[i][1][0]),int(lines[i][1][1])))
	(x2,y2)=max((int(lines[i][0][0]),int(lines[i][0][1])),(int(lines[i][1][0]),int(lines[i][1][1])))
	print((x1,y1),(x2,y2))
	if x1==x2:
		n=y1
		while n in range(y1,y2+1):
			print(str(x1)+" "+str(n))
			grid[n][x1]+=1
			print(grid)
			n+=1
	elif y1==y2:
		n=x1
		while n in range(x1,x2+1):
			print(str(n)+" "+str(y1))
			grid[y1][n]+=1
			print(grid)
			n+=1
	else:
		print(str(x1)+" "+str(y1)+" "+str(x2)+" "+str(y2))
		if y2>y1:
			p=x1
			q=y1
			while (p in range(x1,x2+1)) and (q in range(y1,y2+1)):
				print(str(p)+" "+str(q))
				grid[q][p]+=1
				p+=1
				q+=1
				print(grid)
		else:
			p=x1
			q=y1
			while (p in range(x1,x2+1)) and (q in range(y2,y1+1)):
				print(str(p)+" "+str(q))
				grid[q][p]+=1
				p+=1
				q-=1
				print(grid)
	i+=1

n=0
row=0
while row in range(0,len(grid)):
	column=0
	while column in range(0,len(grid[row])):
		if grid[row][column]>1:
			n+=1
		column+=1
	row+=1

print(n)