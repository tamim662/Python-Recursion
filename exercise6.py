# calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).

def  sum_func(n):
    if (n>=1):
        return n+sum_func(n-2)
    else:
        return 0

number=int(input("enter number:"))
print(sum_func(number))