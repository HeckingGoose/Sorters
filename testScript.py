import sorters, random, time

def RunTests(testSize):
    # Assuming bubble sort is correct, use to generate 'known' correct cases for other sorting algorithms
    print()
    print()
    print(">Running test of size " + str(testSize) + "<")
    print("Generating lists to test algorithms...")
    timeTaken = time.time()
    unsorted = []
    for i in range(testSize):
        unsorted.append(random.randint(-999999, 999999))
    ascend = sorters.bubble.sort(unsorted, "ascend")
    temp = unsorted
    descend = sorters.bubble.sort(unsorted, "descend")
    print("Done (" + str(time.time() - timeTaken) + "s)")
    print()
    print()
    # Test bubble sortIndex
    print(">Testing Bubble Sort<")
    timeTaken = time.time()
    
    indices = sorters.bubble.sortIndex(unsorted, "ascend")
    temp = []
    for i in indices:
        temp.append(unsorted[i])
    if temp == ascend:
        print("(passed): bubble.sortIndex - Ascend - " + str(time.time() - timeTaken) + "s")
    else:
        print("(failed): bubble.sortIndex - Ascend - " + str(time.time() - timeTaken) + "s")

    timeTaken = time.time()
    indices = sorters.bubble.sortIndex(unsorted, "descend")
    temp = []
    for i in indices:
        temp.append(unsorted[i])
    if temp == descend:
        print("(passed): bubble.sortIndex - Descend - " + str(time.time() - timeTaken) + "s")
    else:
        print("(failed): bubble.sortIndex - Descend - " + str(time.time() - timeTaken) + "s")

# Test bubble sort
numValues = random.randint(30,50)
unsorted = []
for i in range(numValues):
    unsorted.append(random.randint(10,99))

print("Bubble sort ascend:")
print(sorters.bubble.sort(unsorted, "ascend"))
print()
print("Bubble sort descend")
print(sorters.bubble.sort(unsorted, "descend"))
print()
print("Bubble sort wrong direction test:")
try:
    print(sorters.bubble.sort(unsorted, "jfdkgj"))
except Exception as e:
    print(e)

RunTests(0)
RunTests(1)
RunTests(10)
RunTests(100)
RunTests(1000)
RunTests(10000)

