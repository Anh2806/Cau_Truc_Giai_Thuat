def InsertionSort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

def main():
    A = [5, 2, 9, 1, 5, 6]
    InsertionSort(A)
    print("Mảng sau khi sắp xếp:", A)

if __name__ == "__main__":
    main()
