from tkinter.messagebox import *
from enum import Enum

class ListType(Enum):
    List = "list"
    Tuple = "tuple"
    Dictionary_Key = "dict1"
    Dictionary_Value = "dict2"

show_warning = True

def SORT(passes: int, list_to_sort, list_type: ListType, is_lengthwise: bool, greater_than: bool):
    """
        Author: Udayshankar R

        Sorts "ListToSort" using a bubble sort algorithm,
        with a accuracy of "Passes".
    """

    assert type(passes) == int, f'\'passes\' is of {type(passes)}. Only type \'int\' is acceptable.'
    assert passes > 0, f'\'passes\' was found to be less than or equal to zero.'
    assert list_to_sort != [] and list_to_sort != () and list_to_sort != {} and list_to_sort != None, '\'list_to_sort\' is empty.'
    assert type(list_to_sort) == list or type(list_to_sort) == tuple or type(list_to_sort) == dict, f'\'list_to_sort\' is of {type(list_to_sort)}. Only type \'list\', \'tuple\' and \'dict\' are acceptable.'
    assert type(list_type) == ListType, f'\'list_type\' is of {type(list_type)}. Onlt type \'list_type\' is acceptable.'
    assert (type(list_to_sort) == list and list_type == ListType.List) or (type(list_to_sort) == tuple and list_type == ListType.Tuple) or (type(list_to_sort) == dict and (list_type == ListType.Dictionary_Key or list_type == ListType.Dictionary_Value)), f'\"list_to_sort\" is of type {type(list_to_sort)}. That is a different datatype than the given \"list_type\".'
    assert type(is_lengthwise) == bool, f'\'is_lengthwise\' is of {type(is_lengthwise)}. Only type \'bool\' is acceptable.'
    assert type(greater_than) == bool, f'\'greater_than\' is of {type(greater_than)}. Only type \'bool\' is acceptable.'

    t = ""
    for i in range(4):
        t += str(list_type.value)[i]
    if list_type == ListType.Tuple:
        t = ListType.Tuple.value

    firstVal = None
    if list_type == ListType.Dictionary_Value:
        firstVal = list(list_to_sort.values())[0]
        for i in list(list_to_sort.values()):
            assert type(i) == type(firstVal), 'There is more than one datatype in \"list_to_sort\". This is not supported.'
            assert type(i) == int or type(i) == float or type(i) == str, 'The values in \"ListToSort\" are not supported datatypes.'
    elif list_type == ListType.Dictionary_Key:
        firstVal = list(list_to_sort.keys())[0]
        for i in list(list_to_sort.keys()):
            assert type(i) == type(firstVal), 'There is more than one datatype in \"list_to_sort\". This is not supported.'
            assert type(i) == int or type(i) == float or type(i) == str, 'The values in \"ListToSort\" are not supported datatypes.'
    else:
        firstVal = list_to_sort[0]
        for i in list_to_sort:
            assert type(i) == type(firstVal), 'There is more than one datatype in \"list_to_sort\". This is not supported.'
            assert type(i) == int or type(i) == float or type(i) == str, 'The values in \"ListToSort\" are not supported datatypes.'

    dictionary = {}
    outDictionary = {}
    if list_type == ListType.Tuple:
        list_to_sort = list(list_to_sort)
    elif list_type == ListType.Dictionary_Key:
        dictionary = list_to_sort
        list_to_sort = list(dictionary.keys())
    elif list_type == ListType.Dictionary_Value:
        dictionary = list_to_sort
        list_to_sort = list(dictionary.values())
    
    letters = "abcdefghijklmnopqrstuvwxyz"
    lettersCap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letterNum = []
    wordIndices = {}
    sortedValues = []
    key = 0
    if(type(firstVal) == str and is_lengthwise == False):
        for j in range(len(list_to_sort)):
            for i in range(len(list_to_sort[j])):
                letter = list_to_sort[j][i]
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
            
            wordIndices[key] = list_to_sort[j]
            key = 0
            letterNum = []
            
    sortedValues = list(wordIndices.keys())

    for i in range(passes):
        if(type(firstVal) != str or is_lengthwise):
            for j in range(len(list_to_sort)):
                try:
                    if greater_than == False:
                        if(type(firstVal) == int or type(firstVal) == float):
                            if list_to_sort[j] < list_to_sort[j + 1]:
                                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
                        elif(type(firstVal) == str and is_lengthwise):
                            if len(list_to_sort[j]) < len(list_to_sort[j + 1]):
                                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
                    else:
                        if(type(firstVal) == int or type(firstVal) == float):
                            if list_to_sort[j] > list_to_sort[j + 1]:
                                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
                        elif(type(firstVal) == str and is_lengthwise):
                            if len(list_to_sort[j]) > len(list_to_sort[j + 1]):
                                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
                except:
                    continue
        else:
            for j in range(len(sortedValues)):
                try:
                    if greater_than == False:
                        if sortedValues[j] < sortedValues[j + 1]:
                            sortedValues[j], sortedValues[j + 1] = sortedValues[j + 1], sortedValues[j]
                    else:
                        if sortedValues[j] > sortedValues[j + 1]:
                            sortedValues[j], sortedValues[j + 1] = sortedValues[j + 1], sortedValues[j]
                except:
                    continue
    
    if(type(firstVal) == str and is_lengthwise == False):
        list_to_sort = []
        for i in sortedValues:
            list_to_sort.append(wordIndices[i])

    if passes < len(list_to_sort) and show_warning:
        showwarning("WARNING", "\"Passes\" was less than length of \"ListToSort\". This may reduce accuracy of the result.")

    if list_type == ListType.Dictionary_Key:
        for i in list_to_sort:
            for j in dictionary.values():
                if dictionary[i] == j:
                    outDictionary[i] = j
        return outDictionary
    elif list_type == ListType.Dictionary_Value:
        for i in list_to_sort:
            for j in dictionary.keys():
                if dictionary[j] == i:
                    outDictionary[j] = i
        return outDictionary
    
    if list_type == ListType.List:
        return list_to_sort
    elif list_type == ListType.Tuple:
        return tuple(list_to_sort)

def AutoSORT(listToSort = [], listType = ListType.List, isLengthwise = False, greaterThan = True):
    """
        Author: Udayshankar R

        Same as SORT() but sets "Passes" as (length of ListToSort) * 2.
        Best for complex lists.
    """

    return SORT(len(listToSort) * 2, listToSort, listType, isLengthwise, greaterThan)