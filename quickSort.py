def quicksort(alist, p , r) :
    
    if p < r :
        # Partition 
        q = partition(alist, p , r)
        # Quicksort both parts
        quicksort(alist, p, q - 1)
        quicksort(alist, q + 1, r)
    
    
def partition(alist, p , r) :
    counter_p = p
    while alist[counter_p] < alist[r] :
        counter_p = counter_p + 1
    counter_q = counter_p
    
    while counter_q < r :
        while alist[counter_q] > alist[r] :
            counter_q = counter_q + 1
        if counter_q < r :    
            temp = alist[counter_p]
            alist[counter_p] = alist[counter_q]
            alist[counter_q] = temp
            counter_p = counter_p + 1
    
    temp = alist[counter_p]
    alist[counter_p] = alist[r]
    alist[r] = temp
    
    return counter_p

alist2 = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
quicksort(alist2, 0, 9)
print alist2
