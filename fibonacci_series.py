def fibonacci(n):
    if n>=3:
        return fibonacci(n-1)+fibonacci(n-2)
    else:
        return 1

num=int(input('Enter n^th number:'))
print(fibonacci(num))