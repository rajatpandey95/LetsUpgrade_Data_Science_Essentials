x=0
y=0


for i in range(int(input())):
    l=input().upper().split()
    if l[0] == 'RIGHT':
        x+=int(l[1])
    elif l[0] == 'LEFT':
        x-=int(l[1])
    elif l[0] == 'UP':
        y+=int(l[1])
    elif l[0] == 'DOWN':
        y-=int(l[1])

dis = (((x**2) + (y**2)) ** 0.5)
print(round(dis))
        
