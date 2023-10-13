import time, sorters

def TestBubble(unsorted, ascend, descend):
    # Test bubble sortIndex
    print(">Testing Bubble Sort<")
    timeTaken = time.time()
    indices = sorters.bubble.SortIndex(unsorted, "ascend")
    temp = []
    for i in indices:
        temp.append(unsorted[i])
    if temp == ascend:
        print("(passed): bubble.SortIndex - Ascend - " + str(time.time() - timeTaken) + "s")
    else:
        print("(failed): bubble.SortIndex - Ascend - " + str(time.time() - timeTaken) + "s")

    timeTaken = time.time()
    indices = sorters.bubble.SortIndex(unsorted, "descend")
    temp = []
    for i in indices:
        temp.append(unsorted[i])
    if temp == descend:
        print("(passed): bubble.SortIndex - Descend - " + str(time.time() - timeTaken) + "s")
    else:
        print("(failed): bubble.SortIndex - Descend - " + str(time.time() - timeTaken) + "s")
