display=[]
i="1"
i=input().split(" | ")
while i[0]!="0":
	display.append(i[1].split(" "))
	i=input().split(" | ")

i=0
counter=0
while i in range(0,len(display)):
	n=0
	while n in range(0,4):
		if len(display[i][n]) in [2,3,4,7]:
			counter+=1
		n+=1
	i+=1

print(counter)