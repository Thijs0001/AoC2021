commands=[]
i=""
while i!="0":
    i=input()
    x=i.split()
    commands.append(x)
    
commands.pop()

x=0
depth=0
i=0
while i in range(0,len(commands)):
    if commands[i][0]=="forward":
        x+=int(commands[i][1])
    elif commands[i][0]=="down":
        depth+=int(commands[i][1])
    elif commands[i][0]=="up":
        depth-=int(commands[i][1])
    i+=1

print(x)
print(depth)
print(x*depth)

i=0
aim=0
depth=0
x=0
while i in range(0,len(commands)):
    if commands[i][0]=="forward":
        x+=int(commands[i][1])
        depth+=aim*int(commands[i][1])
    elif commands[i][0]=="down":
        aim+=int(commands[i][1])
    elif commands[i][0]=="up":
        aim-=int(commands[i][1])
    i+=1

print(x)
print(depth)
print(x*depth)