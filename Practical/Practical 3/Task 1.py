
def MaxElement(S):
    if len(S) == 1:
        return S[0]
    else:
        max_of_rest = MaxElement(S[1:])

        if max_of_rest > S[0]:
            return max_of_rest
        else:
            print(S[0])
            return S[0]


def main():
    S = []
    n = int(input("Enter the number of elements inside sequence S: "))
    for i in range(0, n):
        element = int(input(">>"))
        S.append(element)
    print("The largest number is: ", MaxElement(S))


if __name__ == "__main__":
    main()
