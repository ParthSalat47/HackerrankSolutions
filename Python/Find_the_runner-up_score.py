if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    #print(arr)
    arr.sort()
    
    while max(arr) == arr[-2]:
        arr.pop()
    
    print(arr[-2])
