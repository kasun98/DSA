def main():
    n = int(input())
    print(sum(money(n)))

def money(n):
    w10=0
    w5=0
    w1=0

    money=n
    for i in range(money+1):
        if money == 0:
            return w10,w5,w1
        elif money >= 10:
            w10 = int(money/10)
            money = money - 10*w10
        elif money >= 5:
            w5 = int(money/5)
            money = money - 5*w5
        else:
            w1 = money
            money = money - w1
    return w10,w5,w1


if __name__=='__main__':
    main()