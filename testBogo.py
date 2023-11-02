import time, sorters

def TestBogo(unsorted, ascend, descend):
    # Test bogo Sort
    print(">Testing Bogo Sort<")
    timeTaken = time.time()
    output = sorters.bogo.Sort(unsorted, "ascend")
    if (output == ascend):
        print("(passed): bogo.Sort - Ascend - " + str(time.time() - timeTaken) + "s")
    else:
        print("(failed): bogo.Sort - Ascend - " + str(time.time() - timeTaken) + "s")
    
    timeTaken = time.time()
    output = sorters.bogo.Sort(unsorted, "descend")
    if (output == descend):
        print("(passed): bogo.Sort - Descend - " + str(time.time() - timeTaken) + "s")
    else:
        print("(failed): bogo.Sort - Descend - " + str(time.time() - timeTaken) + "s")
    
    # Test bogo SortIndex
    timeTaken = time.time()
    indices = sorters.bogo.SortIndex(unsorted, "ascend")
    temp = []
    for i in indices:
        temp.append(unsorted[i])
    if temp == ascend:
        print("(passed): bogo.SortIndex - Ascend - " + str(time.time() - timeTaken) + "s")
    else:
        print("(failed): bogo.SortIndex - Ascend - " + str(time.time() - timeTaken) + "s")
        
    timeTaken = time.time()
    indices = sorters.bogo.SortIndex(unsorted, "descend")
    temp = []
    for i in indices:
        temp.append(unsorted[i])
    if temp == descend:
        print("(passed): bogo.SortIndex - Descend - " + str(time.time() - timeTaken) + "s")
    else:
        print("(failed): bogo.SortIndex - Descend - " + str(time.time() - timeTaken) + "s")