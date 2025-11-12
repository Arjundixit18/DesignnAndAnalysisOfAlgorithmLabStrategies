def binary(arr, k, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            return binary(arr, k, mid + 1, high)
        else:
            return binary(arr, k, low, mid - 1)
    return -1

def main():
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter the sorted array: ").split()))

    if len(arr) != n:
        print(f"Error: Expected {n} elements, but got {len(arr)}.")
        return

    k = int(input("Enter the item to be searched: "))
    result = binary(arr, k, 0, n - 1)

    if result == -1:
        print("Item not present")
    else:
        print("Item present")

if __name__ == "__main__":
    main()
