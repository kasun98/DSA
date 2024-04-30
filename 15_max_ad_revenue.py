def main():
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))

    print(max_rev(prices, clicks))


def max_rev(prices, clicks):
    s_prices = sorted(prices)
    s_clicks = sorted(clicks)

    rev = [p*c for p,c in zip(s_prices,s_clicks)]
    return sum(rev)



if __name__=="__main__":
    main()