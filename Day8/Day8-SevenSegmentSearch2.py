display=[]
i="1"
i=input().split(" | ")
while i[0]!="0":
	display.append(i[1].split(" "))
	i=input().split(" | ")

five=["2","3","5"]
six=["6","9"]

i=0
numbers=[]
while i in range(0,len(display)):
	numbers.append([])
	n=0
	while n in range(0,4):
		if len(display[i][n])==2:
			numbers[i].append("1")
		elif len(display[i][n])==3:
			numbers[i].append("7")
		elif len(display[i][n])==4:
			numbers[i].append("4")
		elif len(display[i][n])==7:
			numbers[i].append("8")
		elif len(display[i][n])==5:
			numbers[i].append(five)
		elif len(display[i][n])==6:
			numbers[i].append(six)
		n+=1
	i+=1

print(numbers)