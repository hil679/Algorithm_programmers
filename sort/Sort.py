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

#실행
Sort.selectionSort()
Sort.insertSort()