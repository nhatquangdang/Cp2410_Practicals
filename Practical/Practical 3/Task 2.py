def power(x, n):
    """Compute the value x**n for integer n."""
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


def main():
    print(power(2, 5))


if __name__ == "__main__":
    main()
