def LinearSearch(A, x):
    for i in range(len(A)):
        if A[i] == x:
            return i
    return -1  # Not found

def main():
    A = [3, 5, 2, 9, 1]
    x = 9
    index = LinearSearch(A, x)
    if index != -1:
        print(f"Giá trị {x} được tìm thấy tại vị trí: {index}")
    else:
        print(f"Giá trị {x} không tồn tại trong mảng.")

if __name__ == "__main__":
    main()
