# cook your dish here
T = int(input())
for i in range(T):
    
    N,X = map(int, input().split())
    M = 0
    for j in range(N):
        S , R = map(int, input().split())
        if S<= X and R >M:
            M = R
    print(M)
