def InsertionSort(a):
    for j in range(1, len(a)):
        print "J=%s" % j
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            print a
            a[i+1] = a[i]
            i -= 1
        print "Swap %s With %s" % (a[i+1], key)
        a[i+1] = key
        print a
        print "================="
    return a

InsertionSort([10,23,3,4,4,2,3,4,321,1,5,7,2])
