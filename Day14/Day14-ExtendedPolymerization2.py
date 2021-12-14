import time

template="FSHBKOOPCFSFKONFNFBB"

pairs=[]
insertions=[]
i=input()
while i!="0":
	x=i.split(" -> ")
	pairs.append(x[0])
	insertions.append(x[0][0]+x[1]+x[0][1])
	i=input()

iterations=int(input("How many times would you like to insert?\n"))

class Wildcard:
    def __eq__(self, anything):
        return True

wc = Wildcard()
i=0
for i in range(0,iterations):
	start=time.time()
	print(i)
	templates=[]
	y=0
	starttemp=time.time()
	for y in range(0,len(template)-1):
		templates.append(template[y]+template[y+1])
		y+=1
	print("creating templates "+str(time.time()-starttemp))
	n=0
	findtime=0
	inserttime=0
	startinsert=time.time()
	for n in range(0,len(templates)-1):
		s=time.time()
		x=pairs.index(templates[n])
		findtime+=time.time()-s
		s=time.time()
		templates[n]=insertions[x]
		inserttime+=time.time()-s
		n+=1
	print("inserting letters "+str(time.time()-startinsert)+" of which finding "+str(findtime)+" and inserting "+str(inserttime))
	n=0
	template=""
	startdup=time.time()
	for n in range(0,len(templates)-1):
		templates[n]=templates[n][0]+templates[n][1]
		template+=templates[n]
		n+=1
	print("removing duplicates "+str(time.time()-startdup))
	template+=templates[len(templates)-1]
	print(time.time()-start)
	i+=1

i=0
amounts=[["F",0],["S",0],["H",0],["B",0],["K",0],["O",0],["P",0],["C",0]]
while i in range(0,len(template)):
	n=0
	while n in range(0,len(amounts)):
		if template[i]==amounts[n][0]:
			amounts[n][1]+=1
		n+=1
	i+=1

i=1
maximum=amounts[0]
minimum=amounts[0]
while i in range(1,len(amounts)):
	if amounts[i][1]>maximum[1]:
		maximum=amounts[i]
	if amounts[i][1]<minimum[1]:
		minimum=amounts[i]
	i+=1

print(maximum)
print(minimum)
print(maximum[1]-minimum[1])
