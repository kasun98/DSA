
def main():
    n = int(input())
    print(fib_num(n))

def fib_num(n):
  
    fib = [0, 1]
    
    if n==0:
        return fib[0]
    elif n==1:
        return fib[1]
    else:
        for i in range(2,n+1):
            f_ = fib[i-1]+fib[i-2]
            fib.append(f_)
        return fib[n]
        
    
if __name__ == "__main__":
    main()