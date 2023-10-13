import sorters, random, time, testBubble, testMerge

def GenerateData(testSize):
    print("Generating lists to test algorithms...")
    timeTaken = time.time()
    unsorted = []
    for i in range(testSize):
        unsorted.append(random.randint(-999999, 999999))
    ascend = sorters.bubble.Sort(unsorted, "ascend")
    temp = unsorted
    descend = sorters.bubble.Sort(unsorted, "descend")
    print("Done (" + str(time.time() - timeTaken) + "s)")
    return unsorted, ascend, descend

def RunTests(testSize):
    # Assuming bubble Sort is correct, use to generate 'known' correct cases for other Sorting algorithms
    print()
    print()
    print(">Running test of size " + str(testSize) + "<")
    unsorted, ascend, descend = GenerateData(testSize)
    print()
    print()
    testBubble.TestBubble(unsorted, ascend, descend)
    testMerge.TestMerge(unsorted, ascend, descend)

# Test bubble Sort
numValues = random.randint(30,50)
unsorted = []
for i in range(numValues):
    unsorted.append(random.randint(10,99))

print("Bubble Sort ascend:")
print(sorters.bubble.Sort(unsorted, "ascend"))
print()
print("Bubble Sort descend")
print(sorters.bubble.Sort(unsorted, "descend"))
print()
print("Bubble Sort wrong direction test:")
try:
    print(sorters.bubble.Sort(unsorted, "jfdkgj"))
except Exception as e:
    print(e)

RunTests(0)
RunTests(1)
RunTests(5)
RunTests(10)
RunTests(25)
RunTests(100)
RunTests(101)
RunTests(1000)
RunTests(10000)

