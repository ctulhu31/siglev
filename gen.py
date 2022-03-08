import random
file = open('data.txt', 'w')
s = 'f(a,b,c,d,e,f) a b c d e f\n'
file.write(s)
for i in range(100000):
    s = ''
    a = random.randint(1,1000)
    s = s + str(a) + ' '
    b = random.randint(1,1000)
    s = s + str(b) + ' '
    c = random.randint(1,1000)
    s = s + str(c) + ' '
    d = random.randint(1,1000)
    s = s + str(d) + ' '
    e = random.randint(1,1000)
    s = s + str(e) + ' '
    f = random.randint(1,1000)
    s = s + str(f)
    myfun = a ** 5 + b ** 4 - c ** 3 + d + e + f
    s = str(myfun) + ' ' + s + '\n'
    file.write(s)
file.close()
print('done')
