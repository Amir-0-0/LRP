u = [0 , 0 ]
k = [[]]
N = 2
M = 11
count = 0
summ = 0
def nex(u):
    for i in range(N) :
        if u[N-1-i] < M-1  :
            u[N-1-i] += 1
            break
        else :
            u[N-1-i] = 0

def lrp(u):
    d = True
    i = 0
    while d :
        u.append( ( 2*u[i+1] + 3*u[i] )%M )
        k.append(u[i:i+N])
        i+= 1
        if u[0:N] == u[-N:] : 
            d=False
    print("[u] = ", u , "  ", i)
    del u[N:]
    return i
    
for a in range(M**N):
    f = False
    for kl in k :
        if kl == u :
            f = True
            break
    if f==False:
        i = lrp(u)
        count+=1
        summ += i
    nex(u)
   
   
print(summ)
print(count)
