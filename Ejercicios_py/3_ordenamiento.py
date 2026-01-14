def integerSort(inputArray):
    arr = inputArray.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(integerSort([5, -2, 10, 0, 3]))
