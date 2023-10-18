def array_sort(arr):
    length = len(arr)
    counter = 0
    while counter < length - 1:
        if (arr[counter] > arr[counter + 1]):
            temp = arr[counter]
            arr[counter] = arr[counter + 1]
            arr[counter + 1] = temp

            counter = -1
        counter += 1
    return arr
