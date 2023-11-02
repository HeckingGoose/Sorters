import time, sorters

def TestMerge(unsorted, ascend, descend):
    # Test merge Sort
    print(">Testing Merge Sort<")
    timeTaken = time.time()
    output = sorters.merge.Sort(unsorted, "ascend")
    if output == ascend:
        print("(passed): merge.Sort - Ascend - " + str(time.time() - timeTaken) + "s")
    else:
        print("(failed): merge.Sort - Ascend - " + str(time.time() - timeTaken) + "s")
        
    timeTaken = time.time()
    output = sorters.merge.Sort(unsorted, "descend")
    if output == descend:
        print("(passed): merge.Sort - Descend - " + str(time.time() - timeTaken) + "s")
    else:
        print("(failed): merge.Sort - Descend - " + str(time.time() - timeTaken) + "s")

    # Test merge SortIndex
    timeTaken = time.time()
    indices = sorters.merge.SortIndex(unsorted, "ascend")
    temp = []
    for i in indices:
        temp.append(unsorted[i])
    if temp == ascend:
        print("(passed): merge.SortIndex - Ascend - " + str(time.time() - timeTaken) + "s")
    else:
        print("(failed): merge.SortIndex - Ascend - " + str(time.time() - timeTaken) + "s")
        
    timeTaken = time.time()
    indices = sorters.merge.SortIndex(unsorted, "descend")
    temp = []
    for i in indices:
        temp.append(unsorted[i])
    if temp == descend:
        print("(passed): merge.SortIndex - Descend - " + str(time.time() - timeTaken) + "s")
    else:
        print("(failed): merge.SortIndex - Descend - " + str(time.time() - timeTaken) + "s")
        
