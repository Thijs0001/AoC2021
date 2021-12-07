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