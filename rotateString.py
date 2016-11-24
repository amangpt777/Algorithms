def rotate_array_1(arr, k, direction) :
    print("Rotating array by %d cells towards %s" % (k, direction))
    lengthArray = len(arr)
    if lengthArray == 0 :
        return arr
    else :
        tempArray = arr[:]
        for i in range(lengthArray) :
            if direction == 'right' :
                tempArray[(i + k) % lengthArray] = arr[i]
            else :
                if i - k >= 0 :
                    tempArray[(i - k) % lengthArray] = arr[i]
                else :
                    tempArray[lengthArray - abs(i - k) % lengthArray] = arr[i]
        return tempArray
    
def rotate_array_2(arr, k , direction) :
    lengthArray = len(arr)
    if lengthArray == 0 :
        return arr
    else :
        tempArray = arr[:]
        for i in range(k) :
            if direction == 'right' :
                for j in range(lengthArray - 1, 0, -1) :
                    temp = tempArray[j]
                    tempArray[j] = tempArray[j - 1]
                    tempArray[j - 1] = temp
            else :
                for j in range(lengthArray - 1) :
                    temp = tempArray[j]
                    tempArray[j] = tempArray[j + 1]
                    tempArray[j + 1] = temp
    return tempArray
    
arr = [2,3,5,6,1,0]
arr = rotate_array_2(arr, 2, 'left')
print(arr)
