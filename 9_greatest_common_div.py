
def main():
    a, b = map(int, input().split())
    print(gcd(a, b))

def gcd(a, b):
    if b==0:
        return a
    else:
        a_ = a % b
        return gcd(b, a_)

if __name__=='__main__':
    main()