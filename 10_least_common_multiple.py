
def main():
    a, b = map(int, input().split())
    print(int(lcm(a, b)))

def gcd(a, b):
    if b==0:
        return a
    else:
        a_ = a % b
        return gcd(b, a_)

def lcm(a, b):
    return a*b/gcd(a, b)
    

if __name__=="__main__":
    main()