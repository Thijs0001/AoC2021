inputs=[]
i=""
while i!="0":
	i=input()
	inputs.append(i)

inputs.pop()

i=0
gamma=[0,0,0,0,0,0,0,0,0,0,0,0]
while i in range(0,len(inputs)):
	x=0
	while x in range(0,12):
		if inputs[i][x]=="1":
			gamma[x]+=1
		elif inputs[i][x]=="0":
			gamma[x]-=1
		x+=1
	i+=1

grate=0
erate=0
i=0
while i in range(0,12):
	if gamma[i]>0:
		gamma[i]=1
		grate+=2**(11-i)
	elif gamma[i]<0:
		gamma[i]=0
		erate+=2**(11-i)
	i+=1

print(grate)
print(erate)
print(grate*erate)

oxygen=inputs.copy()
x=0
while len(oxygen)>1:
	i=0
	n=0
	while i in range(0,len(oxygen)):
		if oxygen[i][x]=="1":
			n+=1
		else:
			n-=1
		i+=1
	i=0
	while i in range(0,len(oxygen)):
		if n>=0:
			if oxygen[i][x]=="0":
				oxygen.pop(i)
			else:
				i+=1
		elif n<0:
			if oxygen[i][x]=="1":
				oxygen.pop(i)
			else:
				i+=1

	x+=1

oxygenRate=oxygen[0]

scrubber=inputs.copy()
x=0
while len(scrubber)>1:
	i=0
	n=0
	while i in range(0,len(scrubber)):
		if scrubber[i][x]=="1":
			n+=1
		else:
			n-=1
		i+=1
	i=0
	while i in range(0,len(scrubber)):
		if n>=0:
			if scrubber[i][x]=="1":
				scrubber.pop(i)
			else:
				i+=1
		elif n<0:
			if scrubber[i][x]=="0":
				scrubber.pop(i)
			else:
				i+=1
	x+=1

scrubberRate=scrubber[0]

orate=0
i=0
while i in range(0,12):
	if oxygenRate[i]=="1":
		orate+=2**(11-i)
	i+=1

srate=0
i=0
while i in range(0,12):
	if scrubberRate[i]=="1":
		srate+=2**(11-i)
	i+=1

print(orate)
print(srate)
print(orate*srate)

