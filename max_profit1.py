N = 6
A = [10, 20, 30, 40, 50, 60]
K = 3

def solve (N, A, K):
    buf=[]
    s=[0,A[0]]
    print('s=[0,A[0]] --- ',s)
    for i in A[1:]:
        print('A[1:]----', A[1:])
        s.append(s[-1]+i)
        print('s.append(s[-1]+i) -----', s)
    b2=[A[1]-A[0]]
    print('b2=[A[1]-A[0]]--------', b2)
    for i in range(2,len(A)):
        print('max(b2[-1]+A[i],-s[i]+A[i])----', b2[-1]+A[i], -s[i]+A[i])
        b2.append(max(b2[-1]+A[i],-s[i]+A[i]))
    buf.append(b2)
    f=-1
    for k in range(2,K):
        print('[buf[-1][0]-A[k]]------', [buf[-1][0]-A[k]])
        b2=[buf[-1][0]-A[k]]
        for i in range(k+1,len(A)):
            print('b2[-1]+f*A[i],buf[-1][i-k]+f*A[i]------', b2[-1]+f*A[i], buf[-1][i-k]+f*A[i])
            b2.append(max(b2[-1]+f*A[i],buf[-1][i-k]+f*A[i]))
        buf.append(b2)
        f=-f
        print('buf-------------',buf)
    return buf[-1][-1]


print(solve(N, A, K))


