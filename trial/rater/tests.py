from sys import stdin

N, M=stdin.readline().split()
N=int(N)
M=int(M)

b=[]
b=list(map(int, stdin.readline().split()))

def binary(array,target,start, end):
    sum=0
    mid=(start+end)//2
    for j in range(N):
        if(b[j]>mid):
            sum=sum+b[j]-mid

    if(start>mid):
        return None
    elif (start==mid):
        return mid
    elif (target>sum):
        binary(array,  target,start, mid-1)
    else:
        binary(array, target, mid+1, end)

print(binary(b, M, 0, max(b)))
