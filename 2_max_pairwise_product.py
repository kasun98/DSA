
def main():
    a = int(input())
    c = [int(num) for num in input().split()]
    print(prod(a, c))
    

def prod(a, c):
    if a == len(c):
        prod = 0
        max_1 = max(c)
        c.remove(max_1)
        max_2 = max(c)

        if max_1 == 0 or max_2 == 0:
            prod = 0
        else:
            prod = max_1 * max_2
            
        return prod
    else:
        raise ValueError
        
        

if __name__ == "__main__":
    main()