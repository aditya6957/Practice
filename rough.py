A = a = 1
B = b = 2
C = c = 3
D = d = 4
E = e = 5
F = f = 6
G = g = 7
H = h = 8
I = i = 9
J = j = 10
K = k = 11
L = l = 12
M = m = 13
N = n = 14
O = o = 15
P = p = 16
Q = q = 17
R = r = 18
S = s = 19
T = t = 20
U = u = 21
V = v = 22
W = w = 23
X = x = 24
Y = y = 25
Z = z = 26

test_list = ['a1b', 'a1a']
for i in range(len(test_list)-1,0,-1):
    for j in range(i):
        if test_list[j]>test_list[j+1]:
            temp = test_list[j]
            test_list[j] = test_list[j+1]
            test_list[j+1] = temp
print("Your sorted list is: ")
print(test_list)