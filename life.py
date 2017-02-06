from random import randint
def print2D(A):
    string = ''
    for i in range(len(A)+2):
        string += '-'
    print string
    for i in A:
        string = '|'
        for j in i:
            string += j
        print string+'|'
    string = ''
    for i in range(len(A)+2):
        string += '-'
    print string
        
def neighbours(A,x,y):
    new = []
    n = len(A)
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i<0 or i>=n or j<0 or j>=n or (i==x and j==y):
                continue
            new.append(A[i][j])
    return new
def get(A,i,j):
    x = i%len(A)
    y = j%len(A[x])
    return A[x][y]

def neighbours2(A,x,y):
    new = []
    n = len(A)
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i==x and j==y:
                continue
            new.append(get(A,i,j))
    return new

def mu(c,n):
    if c==' ':
        if n==3:
            return '*'
        return ' '
    if n<2 or n>3:
        return ' '
    return '*'
        
def nextIt(A):
    n = len(A)
    B = []
    total = 0
    for i in range(n):
        B.append([])
        for j in range(n):
            for k in neighbours2(A,i,j):
                if k=='*':
                    total+=1
            B[i].append(mu(A[i][j],total))
            total = 0
    return B
def main(A):
    s = ''
    while s!='e':
        print2D(A)
        A=nextIt(A)
        s = raw_input()

A = []
N = 15
for i in range(N):
    A.append([])
    for j in range(N):
        if randint(1,10)<5:
            A[i].append('*')
        else:
            A[i].append(' ')
main(A)
