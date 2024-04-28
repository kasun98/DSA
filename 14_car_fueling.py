def main():
    d = int(input())        #Distance between cities
    m = int(input())        #Full tank distance
    n = int(input())        #no of gas stations
    x = [0]
    stops = list(map(int, input().split()))     #Distance to gas stations
    x=x+stops
    x.append(d)

    if m >= d:
        print(0)
    else:
        print(car(d,m,n,x))
    

def car(d,m,n,x):
    n_refills = 0
    c_refill = 0
    while c_refill <= n:
        lastrefill = c_refill
        while (c_refill <= n and (x[c_refill+1]-x[lastrefill])<=m):
            c_refill += 1
        if c_refill==lastrefill:
            return -1
        if c_refill <= n:
            n_refills += 1
    return n_refills


if __name__=='__main__':
    main()