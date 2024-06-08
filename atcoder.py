a=[]
while True:
    b=input()
    if b==0:
        a.append(b)
    if b:
        a.append(b)
    else:
        break
for i in reversed(a):
    print(i)