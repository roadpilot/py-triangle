# You are given a positive integer N. Print a numerical triangle of height N-1 like the one below:
# 1
# 22
# 333
# 4444

for i in range(1,int(input())):
    print((10**(i)//9)*i)