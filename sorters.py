from random import randint
from copy import deepcopy
# Sort - Sorts the list and returns the Sorted list
# SortIndex - Sorts the list and returns a new list of indices showing where each value in the original list needs to be to be Sorted

class InvalidDirectionException(Exception):
    # Raised when an invalid Sorting direction is used
    def __init__(self):
        self.message = "Sorting direction was not of form 'Ascend' or 'Descend'"
        super().__init__(self.message)

class bubble():
    def Sort(unsorted, direction):
        output = deepcopy(unsorted)
        match (direction.lower()):
            case "ascend":
                change = True
                while change:
                    change = False
                    for i in range(len(output)):
                        if i < len(output) - 1:
                            if output[i] > output[i + 1]:
                                temp = output[i]
                                output[i] = output[i + 1]
                                output[i + 1] = temp
                                change = True
                return output
            case "descend":
                change = True
                while change:
                    change = False
                    for i in range(len(output)):
                        if i < len(output) - 1:
                            if output[i] < output[i + 1]:
                                temp = output[i]
                                output[i] = output[i + 1]
                                output[i + 1] = temp
                                change = True
                return output
            case _:
                raise InvalidDirectionException
    def SortIndex(unsorted, direction):
        output = deepcopy(unsorted)
        match (direction.lower()):
            case "ascend":
                change = True
                indices = list(range(len(output)))
                while change:
                    change = False
                    for i in range(len(output)):
                        if i < len(output) - 1:
                            if output[i] > output[i + 1]:
                                temp = output[i]
                                output[i] = output[i + 1]
                                output[i + 1] = temp
                                
                                temp = indices[i]
                                indices[i] = indices[i + 1]
                                indices[i + 1] = temp
                                change = True
                return indices
            case "descend":
                change = True
                indices = list(range(len(output)))
                while change:
                    change = False
                    for i in range(len(output)):
                        if i < len(output) - 1:
                            if output[i] < output[i + 1]:
                                temp = output[i]
                                output[i] = output[i + 1]
                                output[i + 1] = temp

                                temp = indices[i]
                                indices[i] = indices[i + 1]
                                indices[i + 1] = temp
                                change = True
                return indices
            case _:
                raise InvalidDirectionException

class merge():
    def Sort(inList, direction):
        direction = direction.lower()
        unsorted = []
        for val in inList:
            unsorted.append([val])
        return merge.MainSort(unsorted, direction)
        
    def MainSort(unsorted, direction):
        outA = unsorted
        outB = []
        if len(outA) > 1:
            i = 0
            while i < len(outA):
                try:
                    outB.append(merge.Merge(outA[i], outA[i + 1], direction))
                except:
                    outB.append(outA[i])
                i += 2
            return merge.MainSort(outB, direction)
        else:
            if len(outA) > 0:
                return outA[0]
            else:
                return outA

    def Merge(listA, listB, direction):
        output = []
        match (direction):
            case "ascend":
                for i in range(len(listA) + len(listB)):
                    if len(listB) > 0:
                        if len(listA) > 0:
                            if listA[0] > listB[0]:
                                output.append(listB[0])
                                del listB[0]
                            else:
                                output.append(listA[0])
                                del listA[0]
                        else:
                            output.append(listB[0])
                            del listB[0]
                    else:
                        output.append(listA[0])
                        del listA[0]
                return output
            case "descend":
                for i in range(len(listA) + len(listB)):
                    if len(listB) > 0:
                        if len(listA) > 0:
                            if listA[0] > listB[0]:
                                output.append(listA[0])
                                del listA[0]
                            else:
                                output.append(listB[0])
                                del listB[0]
                        else:
                            output.append(listB[0])
                            del listB[0]
                    else:
                        output.append(listA[0])
                        del listA[0]
                return output
            case _:
                raise InvalidDirectionException

    def SortIndex(inList, direction):
        direction = direction.lower()
        unsorted = []
        indices = []
        for i in range(len(inList)):
            unsorted.append([inList[i]])
            indices.append([i])
        return merge.MainSortIndex(unsorted, indices, direction)

    def MainSortIndex(unsorted, indices, direction):
        outA = unsorted
        indA = indices # Something is wrong with index sorting
        outB = [] # but it's nearly 3AM and I need to be up in 4 hours
        indB = []
        if len(outA) > 1:
            i = 0
            while i < len(outA):
                try:
                    lis, ind = merge.MergeIndex(outA[i], outA[i + 1], indA[i], indA[i + 1], direction)
                    outB.append(lis)
                    indB.append(ind)
                except:
                    outB.append(outA[i])
                    indB.append(indA[i])
                i += 2
            return merge.MainSortIndex(outB, indB, direction)
        else:
            if len(indA) > 0:
                return indA[0]
            else:
                return indA

    def MergeIndex(listA, listB, indA, indB, direction):
        output = []
        outInd = []
        match (direction):
            case "ascend":
                for i in range(len(listA) + len(listB)):
                    if len(listB) > 0:
                        if len(listA) > 0:
                            if listA[0] > listB[0]:
                                output.append(listB[0])
                                outInd.append(indB[0])
                                del listB[0]
                                del indB[0]
                            else:
                                output.append(listA[0])
                                outInd.append(indA[0])
                                del listA[0]
                                del indA[0]
                        else:
                            output.append(listB[0])
                            outInd.append(indB[0])
                            del listB[0]
                            del indB[0]
                    else:
                        output.append(listA[0])
                        outInd.append(indA[0])
                        del listA[0]
                        del indA[0]
                return output, outInd
            case "descend":
                for i in range(len(listA) + len(listB)):
                    if len(listB) > 0:
                        if len(listA) > 0:
                            if listA[0] < listB[0]:
                                output.append(listB[0])
                                outInd.append(indB[0])
                                del listB[0]
                                del indB[0]
                            else:
                                output.append(listA[0])
                                outInd.append(indA[0])
                                del listA[0]
                                del indA[0]
                        else:
                            output.append(listB[0])
                            outInd.append(indB[0])
                            del listB[0]
                            del indB[0]
                    else:
                        output.append(listA[0])
                        outInd.append(indA[0])
                        del listA[0]
                        del indA[0]
                return output, outInd
            case _:
                raise InvalidDirectionException
class bogo():
    def Sort(inList, direction):
        # Ensure input list isn't modified by this function
        unsorted = deepcopy(inList)
        # Ensure list will be sorted the correct way
        match (direction):
            case "ascend":
                pass
            case "descend":
                for i in range(len(unsorted)):
                    unsorted[i] = -unsorted[i]
            case _:
                raise InvalidDirectionException
        done = False
        while not done:
            # Do iteration
            newList = []
            while len(unsorted) > 0:
                i = randint(0, len(unsorted) - 1)
                newList.append(unsorted[i])
                del unsorted[i]
            unsorted = deepcopy(newList)
            # Assume list is sorted
            done = True
            # Check if list is sorted
            lastVal = unsorted[0]
            for val in unsorted:
                if lastVal > val:
                    done = False
                lastVal = val
        # Fix changes made to ensure correct sort direction
        match (direction):
            case "descend":
                for i in range(len(unsorted)):
                    unsorted[i] = -unsorted[i]
        # Return sorted list
        return unsorted
    def SortIndex(inList, direction):
        # Ensure input list isn't modified by this function
        unsorted = deepcopy(inList)
        # Ensure list will be sorted the correct way
        match (direction):
            case "ascend":
                pass
            case "descend":
                for i in range(len(unsorted)):
                    unsorted[i] = -unsorted[i]
            case _:
                raise InvalidDirectionException
        done = False
        indices = []
        for i in range(len(unsorted)):
            indices.append(i)
        while not done:
            # Do iteration
            newList = []
            tI = indices
            indices = []
            while len(unsorted) > 0:
                i = randint(0, len(unsorted) - 1)
                newList.append(unsorted[i])
                indices.append(tI[i])
                del unsorted[i]
                del tI[i]
            unsorted = deepcopy(newList)
            # Assume list is sorted
            done = True
            # Check if list is sorted
            lastVal = unsorted[0]
            for val in unsorted:
                if lastVal > val:
                    done = False
                lastVal = val
        # Return sorted indices
        return indices
