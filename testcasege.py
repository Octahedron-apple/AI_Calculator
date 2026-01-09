import random
with open("test.txt","w") as f:
    for i in range(40):
        for j in range(40):
            if random.randint(1,2)==1:
                f.write(f"{i}+{j}={i+j}\n")
with open("dat.txt","w") as f:
    for i in range(40):
        for j in range(40):
            if random.randint(1,2)==1:
                f.write(f"{i}+{j}={i+j}\n")
