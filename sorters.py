from copy import deepcopy
# sort - sorts the list and returns the sorted list
# sortIndex - sorts the list and returns a new list of indices showing where each value in the original list needs to be to be sorted

class InvalidDirectionException(Exception):
    # Raised when an invalid sorting direction is used
    def __init__(self):
        self.message = "Sorting direction was not of form 'Ascend' or 'Descend'"
        super().__init__(self.message)
    

class bubble():
    def sort(unsorted, direction):
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
    def sortIndex(unsorted, direction):
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
