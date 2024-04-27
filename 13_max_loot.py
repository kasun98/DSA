def main():
    a, n = map(int, input().split())

    #comp = [[cost, weights]]
    comp = []
    for _ in range(a):
        c = list(map(int, input().split()))
        comp.append(c)
    
    print(f"{max_loot(a, n, comp):.4f}")
    

def max_loot(a, n, comp):
    weights = [comps[1] for comps in comp]
    frac = [comps[0]/comps[1] for comps in comp]
    totalValue = 0
    
    for i in range(a):
        if n==0:
            return totalValue
        max_index = max(enumerate(frac), key=lambda x: x[1])[0]
        f = min(weights[max_index], n)
        totalValue += f*frac[max_index]
        n = n-f
        weights.pop(max_index)
        frac.pop(max_index)
        i += 1 
    return totalValue


if __name__=='__main__':
    main()