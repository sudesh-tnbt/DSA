def fibonacci1(n):
    # Manual approach
    n = int(n)
    a = 1
    b = 1
    fibo = []
    if n > 2:
        fibo.append(a)
        fibo.append(b)
        for i in range(2, n):
            if i % 2 == 0:
                a = a + b
                fibo.append(a)
            else:
                b = a + b
                fibo.append(b)
    return fibo


# Asks the user for the number of terms
n = input("Enter no. of terms: ")
result = fibonacci1(n)
print(result)
