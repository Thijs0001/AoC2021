inputs=input("Please input your input:\n").split(",")

fishes=[0,0,0,0,0,0,0,0,0]

i=0
while i in range(0,len(inputs)):
	fishes[int(inputs[i])]+=1
	i+=1

days=int(input("\nHow many days do you want to simulate?\n"))

i=0
while i in range(0,days):
	z=fishes[7]
	fishes[7]=fishes[8]
	fishes[8]=fishes[i%7]
	fishes[i%7]+=z
	i+=1

print(sum(fishes))