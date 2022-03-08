import random
file = open('data1.txt', 'w')
file2 = open('data.txt', 'w')
s = 'f(a,b,c,d,e,f) a b c d e f\n'
file.write(s)
for i in range(100000):
    s = ''
    a = random.randint(1,1000)
    file2.write(str(a) + '\n')
    s = s + str(a) + ' '
    b = random.randint(1,1000)
    file2.write(str(b) + '\n')
    s = s + str(b) + ' '
    c = random.randint(1,1000)
    file2.write(str(c) + '\n')
    s = s + str(c) + ' '
    d = random.randint(1,1000)
    file2.write(str(d) + '\n')
    s = s + str(d) + ' '
    e = random.randint(1,1000)
    file2.write(str(e) + '\n')
    s = s + str(e) + ' '
    f = random.randint(1,1000)
    file2.write(str(f) + '\n')
    s = s + str(f)
    myfun = a ** 5 + b ** 4 - c ** 3 + d + e + f
    file2.write(str(myfun) + '\n')
    s = str(myfun) + ' ' + s + '\n'
    file.write(s)
file.close()
file2.write('1000000001')
file2.close()
print('done')
