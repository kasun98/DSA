def main():
    n = int(input())
    n_list = list(map(int, input().split()))
    m = int(input())
    m_list = list(map(int, input().split()))

    print(*binary_search(n,n_list,m,m_list))


def binary_search(n,n_list,m,m_list):
    result = [0 for i in range(m)]
    for i in range(m):
        left = 0
        right = n-1
        while right>=left:
            mid = int((left + right)/2)
            if n_list[mid] == m_list[i]:
                result[i] = mid 
                break
            elif n_list[mid]<m_list[i]:
                left = mid + 1
            elif n_list[mid]>m_list[i]:
                right = mid - 1
            result[i] = -1
    return result
        
    
if __name__=='__main__':
    main()