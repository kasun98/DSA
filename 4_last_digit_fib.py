
def main():
    n = int(input())
    print(fib_last_dig(n))

   

def fib_last_dig(n):
 
    fib = [0, 1, 1, 2, 3, 5, 8]
    
    if n<7:
        return fib[n]
    else:
        for i in range(7,n+1):
            f_ = (fib[i-1]+fib[i-2]) % 10
            fib.append(f_)
        return fib[n]
    

        
    
if __name__ == "__main__":
    main()