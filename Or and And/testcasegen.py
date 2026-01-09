import random
with open("test.txt","w") as f:
    for i in range(40):
        a=random.randint(0,1)
        b=random.randint(0,1)
        f.write(f"{a}and{b}={a and b}\n")
    for i in range(40):
        a=random.randint(0,1)
        b=random.randint(0,1)
        f.write(f"{a}or{b}={a or b}\n")
    
with open("dat.txt","w") as f:
    for i in range(40):
        a=random.randint(0,1)
        b=random.randint(0,1)
        f.write(f"{a}and{b}={a and b}\n")
    for i in range(40):
        a=random.randint(0,1)
        b=random.randint(0,1)
        f.write(f"{a}or{b}={a or b}\n")
