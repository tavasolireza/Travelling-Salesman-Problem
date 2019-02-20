import random

a = random.randint(2, 12)
b = random.randint(2, 12)
c = random.randint(2, 12)
d = random.randint(10, 20)
print(a, b, c, d)

a_list = []
b_list = []
c_list = []
d_list = []

for i in range(a):
    a_list.append((random.randint(-15, 15), random.randint(-15, 15)))

for i in range(b):
    b_list.append((random.randint(-100, 100), random.randint(-100, 100)))

for i in range(c):
    c_list.append((random.randint(-10, 10), random.randint(-10, 10)))

for i in range(d):
    d_list.append((random.randint(-9, 9), random.randint(-9, 9)))

print('n= {}\npoints= {}'.format(a, a_list))
print('n= {}\npoints= {}'.format(b, b_list))
print('n= {}\npoints= {}'.format(c, c_list))
print('n= {}\npoints= {}'.format(d, d_list))
