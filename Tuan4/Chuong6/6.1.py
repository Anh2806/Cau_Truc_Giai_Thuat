#SO Nhi phan tu 1 den N
def binary_numbers(n):
    result = []
    for i in range(1, n + 1):
        result.append(bin(i)[2:])
    return " ".join(result)
def main():
    T = int(input(" "))
    for i in range(T):
        n = int(input(""))
        print(binary_numbers(n))
if __name__ == "__main__":
    main()