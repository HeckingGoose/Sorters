import time, sorters

def TestMerge(unsorted, ascend, descend):
    # Test merge sort
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
