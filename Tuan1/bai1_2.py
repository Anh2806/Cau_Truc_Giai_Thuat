def FindMax(A):
    if not A:
        print("Error: Empty array!")
        return None
    
    max_val = A[0]
    for i in range(1, len(A)):
        if A[i] > max_val:
            max_val = A[i]
    return max_val

def main():
    A = [3, 5, 2, 9, 1]
    max_val = FindMax(A)
    if max_val is not None:
        print(f"Giá trị lớn nhất trong mảng là: {max_val}")

if __name__ == "__main__":
    main()
