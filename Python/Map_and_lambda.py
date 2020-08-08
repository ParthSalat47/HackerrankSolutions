cube = lambda x: x**3

def fibonacci(n):
    fib = [0,1]
    if n == 0:
        return []
    if n == 1:
        return [0]
    elif n == 2:
        return fib
    else:
        for i in range(n-2):
            add = fib[-1] + fib[-2]
            fib.append(add)
        return fib
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
