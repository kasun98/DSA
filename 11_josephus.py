def main():
    n, k = map(int, input().split())
    print(jos(n, k))

def jos(n, k):
    people = list(range(1, n + 1))
    
    index = 0
    while len(people) > 1:
        # Calculate the index of the person to be eliminated
        index = (index + k - 1) % len(people)
        
        # Remove the person at the calculated index
        del people[index]

    return people[0]



if __name__=="__main__":
    main()