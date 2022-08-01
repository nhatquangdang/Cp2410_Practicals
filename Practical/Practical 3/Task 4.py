#  m × n = m + (m × (n - 1)).
def Multiply(m, n):
    # generate base case for the recursive algorithm
    # base case m x 1 = m
    if n == 1:
        return m
    else:
        return m + Multiply(m, n - 1)


def main():
    print(Multiply(5, 4))


if __name__ == '__main__':
    main()
