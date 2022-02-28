import random
i = 1
file = open('data.txt', 'w')
while i<100000:
    a = random.randint(1,1000)
    file.write(str(a) + '\n')
    b = random.randint(1,1000)
    file.write(str(b) + '\n')
    c = random.randint(1,1000)
    file.write(str(c) + '\n')
    d = random.randint(1,1000)
    file.write(str(d) + '\n')
    e = random.randint(1,1000)
    file.write(str(e) + '\n')
    f = random.randint(1,1000)
    file.write(str(f) + '\n')
    myfun = a * a * a + b * b - c 
    file.write(str(myfun) + '\n')
    i = i + 1
file.write('1000000001')
file.close()
print('done')
