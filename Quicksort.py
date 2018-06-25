def qsort(lst):
        if len (lst) <=0:
            return lst
        p = lst[len(lst) // 2]
        l = [x for x in lst if x < p]
        m = [x for x in lst if x == p]
        h = [x for x in lst if x > p]
        
        return qsort(l) + m + qsort(h)
    
print (qsort([6,3,9,1,9,2,4]))
