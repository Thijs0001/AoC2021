commands=[]
i=""
while i!="0":
    i=input()
    x=i.split()
    print(x)
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