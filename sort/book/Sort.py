class Sort:
    def selectionSort():
        array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
        for i in range(len(array)):
            minIndex = i
            for j in range(i + 1, len(array)):
                if(array[minIndex] > array[j]):
                    minIndex = j
            array[i], array[minIndex] = array[minIndex], array[i]

        print(array)
    
    def insertSort():
        array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
        for i in range(1, len(array)):
            for j in range(i, 0, -1):
                if(array[j] < array[j -1]):
                    array[j], array[j -1] = array[j - 1], array[j]
                else:
                    break
        print(array)

    def quickSort(array, start, end):
        if start >= end:
            return
        pivot = start
        left = start + 1
        right = end
        while left <= right:
            while left <= end and array[left] <= array[pivot]:
                left += 1
            while right > start and array[right] >= array[pivot]:
                right -= 1
            if left > right:
                array[right], array[pivot] = array[pivot], array[right]
            else:
                array[left], array[right] = array[right], array[left]
        Sort.quickSort(array, start, right - 1)
        Sort.quickSort(array, right + 1, end)
        

#실행
Sort.selectionSort()
Sort.insertSort()

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
Sort.quickSort(array, 0, len(array) - 1)
print(array)