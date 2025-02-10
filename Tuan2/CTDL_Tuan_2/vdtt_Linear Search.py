def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Ví dụ sử dụng
contacts = ["Alice", "Bob", "Charlie", "David"]
target_name = "Charlie"
result = linear_search(contacts, target_name)

if result != -1:
    print(f"{target_name} được tìm thấy ở vị trí: {result}")
else:
    print(f"{target_name} không có trong danh bạ.")