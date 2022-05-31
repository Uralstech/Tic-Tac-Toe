def help():
    print("\n\nSCSort will help you sort lists, tuples and dictionaries.", end="")
    print("\nFor importing, type in \"from ShortCode.SCSort import *\".")
    
    print("\n\nListType:", end="")
    print("\nThis is the enum that tells SORT() and AutoSort()", end="")
    print("\n\twhat datatypes they are working with. This is how to use them:", end="")
    print("\nListType.List: Use this when sorting a list. In SORT() and", end="")
    print("\n\tAutoSORT() this is set as the default ListType.", end="")
    print("\nListType.Tuple: Use this when sorting a tuple.", end="")
    print("\nListType.Dictionary_Key: Use this when sorting only the keys", end="")
    print("\n\tof a dictionary. The values will not change.", end="")
    print("\nListType.Dictionary_Value: Use this when sorting only the values", end="")
    print("\n\tof a dictionary. The keys will not change.", end="")
    
    print("\n\nSORT(passes, listToSort, listType, isLengthwise, greaterThan):", end="")
    print("\nReturns the sorted varient of given list/tuple/dictionary.", end="")
    print("\nArguments:\npasses (int): The amount of times to run the program.", end="")
    print("\n\tThe higher the value, the more accurate. Small lists only need 1 or 2 passes.", end="")
    print("\nlistToSort (list/tuple/dict): The list/tuple/dictionary to sort.", end="")
    print("\nlistType (ListType, not required if type(listToSort) == list): The ListType that", end="")
    print("\n\ttells the program which datatype to use while sorting.", end="")
    print("\nisLengthwise (bool, optional, default = False): Use this only when sorting through", end="")
    print("\n\tlists/tuples/dictionaries that are string only. Enable this if you want to sort", end="")
    print("\n\tby the length of the string. Disable if you want to sort by the order of the letters.", end="")
    print("\ngreaterThan (bool, optional, default = True): The boolean that tells the program", end="")
    print("\n\tto sort from ascending order or descending order.", end="")
    print("\nReturns: The sorted data in the form of a list/tuple/dictionary.", end="")
    
    print("\n\nAutoSORT(listToSort, listType, greaterThan):", end="")
    print("\nSame as SORT(), but sets passes to len(listToSort) * 2.", end="")
    print("\nArguments:\nlistToSort (list/tuple/dict): The list/tuple/dictionary to sort.", end="")
    print("\nlistType (ListType, not required if type(listToSort) == list): The ListType that", end="")
    print("\n\ttells the program which datatype to use while sorting.", end="")
    print("\nisLengthwise (bool, optional, default = False): Use this only when sorting through", end="")
    print("\n\tlists/tuples/dictionaries that are string only. Enable this if you want to sort", end="")
    print("\n\tby the length of the string. Disable if you want to sort by the order of the letters.", end="")
    print("\ngreaterThan (bool, optional, default = True): The boolean that tells the program", end="")
    print("\n\tto sort from ascending order or descending order.", end="")
    print("\nReturns: The sorted data in the form of a list/tuple/dictionary.", end="")
    print("\nNOTE: Recommended for larger lists/tuples/dictionaries.")

from tkinter.messagebox import *
import enum

class Error(enum.Enum):
    DataType_Error = "\"ListToSort\" is a different datatype than the given \"Type\" , aborting function."
    DataType_Error_Value = "Some values in \"ListToSort\" are not supported datatypes, aborting function."
    DataType_Error_MTOT = "There is more than one datatype in \"ListToSort\" . This is not supported, aborting function."
    ListToSort_Null = "\"ListToSort\" is []. This will cause errors in SORT(), aborting function."
    Passes_Zero = "\"Passes\" is 0. This will cause errors in SORT(), aborting function."
    Passes_Less_Than_Zero = "\"Passes\" was less than 0. This will cause errors in SORT(), aborting function."
    Passes_NonNumeric = "\"Passes\" was found to be a non-numerical value, aborting function."
    GreaterThan_NonBoolean = "\"GreaterThan\" was found to be a non-boolean value, aborting function."

class Warning(enum.Enum):
    Passes_Less_Than_ListToSort_Length = "\"Passes\" was less than length of \"ListToSort\" . This may reduce the accuracy of the result."

useWarning = True

class ListType(enum.Enum):
    List = "list"
    Tuple = "tuple"
    Dictionary_Key = "dict1"
    Dictionary_Value = "dict2"

def SORT(passes = 10, listToSort = None, listType = ListType.List, isLengthwise = False, greaterThan = True):
    """
        Author: Udayshankar R

        Sorts "ListToSort" using a bubble sort algorithm,
        with a accuracy of "Passes".
    """

    t = ""
    for i in range(4):
        t += str(listType.value)[i]
    if listType == ListType.Tuple:
        t = ListType.Tuple.value

    if listToSort == None or listToSort == [] or listToSort == () or listToSort == {}:
        showerror("ERROR", str(Error.ListToSort_Null.value).split())
        return Error.ListToSort_Null
    elif t != str(type(listToSort).__name__):
        showerror("ERROR", str(Error.DataType_Error.value).split())
        return Error.DataType_Error
    elif type(passes) != int:
        showerror("ERROR", str(Error.Passes_NonNumeric.value).split())
        return Error.Passes_NonNumeric
    elif passes == 0:
        showerror("ERROR", str(Error.Passes_Zero.value).split())
        return Error.Passes_Zero
    elif passes < 0:
        showerror("ERROR", str(Error.Passes_Less_Than_Zero.value).split())
        return Error.Passes_Less_Than_Zero
    elif type(greaterThan) != bool:
        showerror("ERROR", str(Error.GreaterThan_NonBoolean.value).split())
        return Error.GreaterThan_NonBoolean

    firstVal = None
    if listType == ListType.Dictionary_Value:
        firstVal = list(listToSort.values())[0]
        for i in list(listToSort.values()):
            if(type(i) != type(firstVal)):
                showerror("ERROR", str(Error.DataType_Error_MTOT.value).split())
                return Error.DataType_Error_MTOT;
            
            if type(i) != int and type(i) != float and type(i) != str:
                showerror("ERROR", str(Error.DataType_Error_Value.value).split())
                return Error.DataType_Error_Value;
    elif listType == ListType.Dictionary_Key:
        firstVal = list(listToSort.keys())[0]
        for i in list(listToSort.keys()):
            if(type(i) != type(firstVal)):
                showerror("ERROR", str(Error.DataType_Error_MTOT.value).split())
                return Error.DataType_Error_MTOT;
                
            if type(i) != int and type(i) != float and type(i) != str:
                showerror("ERROR", str(Error.DataType_Error_Value.value).split())
                return Error.DataType_Error_Value;
    else:
        firstVal = listToSort[0]
        for i in listToSort:
            if(type(i) != type(firstVal)):
                showerror("ERROR", str(Error.DataType_Error_MTOT.value).split())
                return Error.DataType_Error_MTOT;
            
            if type(i) != int and type(i) != float and type(i) != str:
                showerror("ERROR", str(Error.DataType_Error_Value.value).split())
                return Error.DataType_Error_Value;

    dictionary = {}
    outDictionary = {}
    if listType == ListType.Tuple:
        listToSort = list(listToSort)
    elif listType == ListType.Dictionary_Key:
        dictionary = listToSort
        listToSort = list(dictionary.keys())
    elif listType == ListType.Dictionary_Value:
        dictionary = listToSort
        listToSort = list(dictionary.values())
    
    letters = "abcdefghijklmnopqrstuvwxyz"
    lettersCap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letterNum = []
    wordIndices = {}
    sortedValues = []
    key = 0
    if(type(firstVal) == str and isLengthwise == False):
        for j in range(len(listToSort)):
            for i in range(len(listToSort[j])):
                letter = listToSort[j][i]
                if(i > 0):
                    if(letter in letters):
                        letterNum.append(letters.index(letter) / 2)
                    elif(letter in lettersCap):
                        letterNum.append(lettersCap.index(letter) / 2)
                else:
                    if(letter in letters):
                        letterNum.append(letters.index(letter) * 1.5)
                    elif(letter in lettersCap):
                        letterNum.append(lettersCap.index(letter) * 1.5)
            
            for i in letterNum:
                key += i
            
            wordIndices[key] = listToSort[j]
            key = 0
            letterNum = []
            
    sortedValues = list(wordIndices.keys())

    for i in range(passes):
        if(type(firstVal) != str or isLengthwise):
            for j in range(len(listToSort)):
                try:
                    if greaterThan == False:
                        if(type(firstVal) == int or type(firstVal) == float):
                            if listToSort[j] < listToSort[j + 1]:
                                listToSort[j], listToSort[j + 1] = listToSort[j + 1], listToSort[j]
                        elif(type(firstVal) == str and isLengthwise):
                            if len(listToSort[j]) < len(listToSort[j + 1]):
                                listToSort[j], listToSort[j + 1] = listToSort[j + 1], listToSort[j]
                    else:
                        if(type(firstVal) == int or type(firstVal) == float):
                            if listToSort[j] > listToSort[j + 1]:
                                listToSort[j], listToSort[j + 1] = listToSort[j + 1], listToSort[j]
                        elif(type(firstVal) == str and isLengthwise):
                            if len(listToSort[j]) > len(listToSort[j + 1]):
                                listToSort[j], listToSort[j + 1] = listToSort[j + 1], listToSort[j]
                except:
                    continue
        else:
            for j in range(len(sortedValues)):
                try:
                    if greaterThan == False:
                        if sortedValues[j] < sortedValues[j + 1]:
                            sortedValues[j], sortedValues[j + 1] = sortedValues[j + 1], sortedValues[j]
                    else:
                        if sortedValues[j] > sortedValues[j + 1]:
                            sortedValues[j], sortedValues[j + 1] = sortedValues[j + 1], sortedValues[j]
                except:
                    continue
    
    if(type(firstVal) == str and isLengthwise == False):
        listToSort = []
        for i in sortedValues:
            listToSort.append(wordIndices[i])

    if passes < len(listToSort) and useWarning:
        showwarning("WARNING", str(Warning.Passes_Less_Than_ListToSort_Length.value).split())

    if listType == ListType.Dictionary_Key:
        for i in listToSort:
            for j in dictionary.values():
                if dictionary[i] == j:
                    outDictionary[i] = j
        return outDictionary
    elif listType == ListType.Dictionary_Value:
        for i in listToSort:
            for j in dictionary.keys():
                if dictionary[j] == i:
                    outDictionary[j] = i
        return outDictionary
    
    if listType == ListType.List:
        return listToSort
    elif listType == ListType.Tuple:
        return tuple(listToSort)

def AutoSORT(listToSort = [], listType = ListType.List, isLengthwise = False, greaterThan = True):
    """
        Author: Udayshankar R

        Same as SORT() but sets "Passes" as (length of ListToSort) * 2.
        Best for complex lists.
    """

    return SORT(len(listToSort) * 2, listToSort, listType, isLengthwise, greaterThan)