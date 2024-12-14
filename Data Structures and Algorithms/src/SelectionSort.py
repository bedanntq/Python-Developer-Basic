def Selection_Sort(arrry):
    n = len(arrry)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1 , n):
            if arrry[j] < arrry[min_index]:
                min_index = j
            
        if min_index != i:
            arrry[i] , arrry[min_index] = arrry[min_index] , arrry[i]
    return arrry

array = [64, 34, 25, 12, 22, 11, 90]
selection_sort = Selection_Sort(array)
print("Danh sách đã sắp xếp:", selection_sort)
