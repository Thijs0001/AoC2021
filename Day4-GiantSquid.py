numbers=[72,99,88,8,59,61,96,92,2,70,1,32,18,10,95,33,20,31,66,43,26,24,91,44,11,15,48,90,27,29,14,68,3,50,69,74,54,4,16,55,64,12,73,80,58,83,6,87,30,41,25,39,93,60,9,81,63,75,46,19,78,51,21,28,94,7,17,42,53,13,97,98,34,76,89,23,86,52,79,85,67,84,47,22,37,65,71,49,82,40,77,36,62,0,56,45,57,38,35,5]
boards=[]

i=1
x=0
while i!="0":
	n=0
	boards.append([])
	while n in range(0,5):
		i=input().split("""

""")
		boards[x].append(i[0].split())
		n+=1
	x+=1
	i=input()

i=0
while i in range(0,len(numbers)):
	board=0
	while board in range(0,len(boards)):
		row=0
		while row in range(0,5):
			column=0
			while column in range(0,5):
				if int(boards[board][row][column])==numbers[i]:
					boards[board][row][column]=-1
					r=0
					rowtotal=0
					columntotal=0
					while r in range(0,5):
						rowtotal+=int(boards[board][row][r])
						columntotal+=int(boards[board][r][column])
						r+=1
					if columntotal==-5 or rowtotal==-5:
						win=boards[board]
						last=numbers[i]
						column=5
						row=5
						board=len(boards)
						i=len(numbers)
				column+=1
			row+=1
		board+=1
	i+=1

total=0
row=0
while row in range(0,5):
	column=0
	while column in range(0,5):
		if win[row][column]!=-1:
			total+=int(win[row][column])
		column+=1
	row+=1

score=total*last
print(score)
