MAP AND LAMBDA
cube = lambda x: x** 3

def fibonacci(n):
    # return a list of fibonacci numbers
    alpha, beta, gamma = 0,1,1
    for _ in range(n):
        yield alpha
        alpha, beta = beta, alpha + beta