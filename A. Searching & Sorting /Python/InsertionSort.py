def insertion(arr, n):
    for i in range(n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    n = int(input("Enter size of the array: "))
    arr = list(map(int, input(f"Enter {n} elements into the array: ").split()))
    
    if len(arr) != n:
        print(f"Error: Expected {n} elements, but got {len(arr)}.")
        return

    insertion(arr, n)
    print("After sorting the elements are:", *arr)

if __name__ == "__main__":
    main()
