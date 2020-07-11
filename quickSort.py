
def partition(arr, st, n):

 pivot = arr[st]

  low, high = st+1, n

   while True:

        while low <= high and arr[high] >= pivot:
            high -= 1

        while low <= high and arr[low] <= pivot:
            low += 1
        if low > high:
            break
        arr[high], arr[low] = arr[low], arr[high]
    arr[st], arr[high] = arr[high], arr[st]
    return high


def quickSort(arr, st, n):

    if st < n:
        ind = partition(arr, st, n)
        quickSort(arr, st, ind-1)
        quickSort(arr, ind+1, n)
    return arr


if __name__ == '__main__':

    arr = [3, 8, 1, 9, 12, 2, 11, 7, 5, 4]
    print(arr)
    print(quickSort(arr, 0, len(arr)-1))
