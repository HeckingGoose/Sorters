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
    def SortIndex(unsorted, direction):
        pass
    
    def Merge(inA, inB, direction):
        output = []
        listA = deepcopy(inA)
        listB = deepcopy(inB)
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
