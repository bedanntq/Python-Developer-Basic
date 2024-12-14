def BubbleSort(arrry):
    n = len(arrry)
    for i in range(n - 1):
        Swapped = False
        for j  in range(n - i - 1):
            if arrry[j] > arrry[j + 1]:
                arrry[j] ,arrry[j + 1] = arrry[j + 1], arrry[j]
                Swapped = True
        if not Swapped:
            break
    return arrry
            
array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = BubbleSort(array)
print("Danh sách đã sắp xếp:", sorted_array)