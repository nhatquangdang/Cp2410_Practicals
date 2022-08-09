S = []
T = []



def transfer(S, T):
    if len(S) == 0:
        print(" Stack S has no value")
    elif len(S) > 0:
        for i in range(len(S)):
            T.append(S.pop())
    return T


def main():
    elements = int(input("Enter the number of elements inside stack S: "))
    for i in range(elements):
        n = (input(">> "))
        S.append(n)

    transferList = transfer(S, T)
    print(transferList)


if __name__ == '__main__':
    main()


