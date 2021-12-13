grid=[]
x=0
while x in range(0,999):
	y=0
	grid.append([])
	while y in range(0,999):
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
	if lines[i][0][0]==lines[i][1][0]:
		n=min(int(lines[i][0][1]),int(lines[i][1][1]))
		while n in range(min(int(lines[i][0][1]),int(lines[i][1][1])),max(int(lines[i][0][1]),int(lines[i][1][1]))+1):
			grid[n][int(lines[i][0][0])]+=1
			n+=1
	elif lines[i][0][1]==lines[i][1][1]:
		n=min(int(lines[i][0][0]),int(lines[i][1][0]))
		while n in range(min(int(lines[i][0][0]),int(lines[i][1][0])),max(int(lines[i][0][0]),int(lines[i][1][0]))+1):
			grid[int(lines[i][0][1])][n]+=1
			n+=1
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