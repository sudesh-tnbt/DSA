# Maximum pairwise product

def mpp(n):
    max = 0
    for i in range(len(n) - 1):
        product = n[i] * n[i + 1]
        if product > max:
            max = product
    return max


numbers = [1, 3, 3]
print(mpp(numbers))
