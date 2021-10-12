# cook your dish here
# cook your dish here
import io, os, sys
reader = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
def fast_input():
    return reader().decode()
def fast_print(x):
    sys.stdout.write(x + "\n")
    

def precompute(n,m,matrix):
    t=[[0 for i in range(m)] for j in range(n)]
    t[0][0]=matrix[0][0]
    for i in range(m):
        t[0][i]=t[0][i-1]+matrix[0][i]
    for i in range(n):
        t[i][0]=t[i-1][0]+matrix[i][0]
    for i in range(1,n):
        for j in range(1,m):
            t[i][j]=t[i-1][j]+t[i][j-1]+matrix[i][j]-t[i-1][j-1]
    return t




def solve(sum,n,m,key):
    c=0
    for k in range(1,n+1):
        for i in range(k - 1, n):
            low,high,j,total=k-1,m-1,0,0;
            while(low<=high):
                j=(low+high)//2
                total = sum[i][j]
                if i - k >= 0:
                    total = total - sum[i - k][j]
                if j - k >= 0:
                    total = total - sum[i][j - k]
                if i - k >= 0 and j - k >= 0:
                    total = total + sum[i - k][j - k]
                if total/(k*k)>=key:
                    high=j-1
                else:
                    low=j+1
            if total/(k*k)>=key:
                c+=(m-j)
            else:
                c+=(m-j-1)
            #print(c,k,total)
    return c
for _ in range(int(fast_input())):
    n,m,key=map(int,fast_input().split())
    matrix=[list(map(int,fast_input().split())) for j in range(n)]
    t=precompute(n,m,matrix)
    #print(t)
    print(solve(t,n,m,key))
    
