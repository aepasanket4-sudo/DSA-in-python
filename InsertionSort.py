def insertionSort(seq):
    for sliceEnd in range(len(seq)):
        pos = sliceEnd
        while pos > 0 and seq[pos] < seq[pos-1]:
            (seq[pos],seq[pos-1]) = (seq[pos-1],seq[pos])
            pos = pos-1
    print(seq)
            
l = [56,25,13,65,45]
insertionSort(l)