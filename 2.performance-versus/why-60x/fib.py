def fib(n):
    if n < 2:
        return n
    ans, last = 1, 0  # ans=n=1; last=n=0.
    for _ in range(1, n):
        ans, last = ans + last, ans
    return ans

if __name__ == "__main__":
    import dis
    dis.dis(fib)
