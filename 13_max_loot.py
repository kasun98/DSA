def main():
    a, n = map(int, input().split())

    #comp = [[cost, weights]]
    comp = []
    for _ in range(a):
        c = list(map(int, input().split()))
        comp.append(c)

    print(f"{max_loot(a, n, comp):.4f}")

    

    


def max_loot(a, n, comp):
    totalValue = 0
    for i in range(a):
        if n == 0:
            return totalValue
        else:
            f = min(comp[i][1], n)
            totalValue = totalValue + f*(comp[i][0]/comp[i][1])
            #comp[i][1] -= f 
            n = n - f
            print(f, totalValue, n)

    return totalValue




if __name__=='__main__':
    main()