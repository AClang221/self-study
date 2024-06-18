import random
file = open("text.txt", "w+")
for i in range(100):
    file.write(str(random.randint(1,100))+"\n")
file.close()