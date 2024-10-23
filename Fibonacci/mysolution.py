def fibonacci1(n):
    # Manual approach
    a = 0
    b = 1
    result = []
    if n > 2:
        result.append(a)
        result.append(b)
        for i in range(2, n):
            if i % 2 == 0:
                a = a + b
                result.append(a)
            else:
                b = a + b
                result.append(b)
    return result


def fibo(n):
    # Recursive function
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)


def fibonacci2(n):
    # Recursive approach
    result = []
    for i in range(n):
        result.append(fibo(i))
    return result


# Asks the user for the number of terms
n = int(input("Enter no. of terms: "))
result1 = fibonacci1(n)
result2 = fibonacci2(n)
print(result1)
print(result2)
