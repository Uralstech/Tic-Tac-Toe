def help():
    print("\n\nSCFileSystem will help you read and write files.", end="")
    print("\nFor importing, type in \"from ShortCode.SCFileSystem import *\".")
    
    print("\n\nfile_read(full_path):", end="")
    print("\nReads and returns the contents of the file.", end="")
    print("\nArguments:\nfull_path (string): The path of the file to read.", end="")
    print("\nReturns: Data in the file in the form of a list.", end="")
    
    print("\n\nfile_readline(full_path):", end="")
    print("\nReads and returns the first line of the file.", end="")
    print("\nArguments:\nfull_path (string): The path of the file to read.", end="")
    print("\nReturns: First line of the file in the form of a list.", end="")
    
    print("\n\nfile_readlines(full_path):", end="")
    print("\nReads and returns the every line of the file.", end="")
    print("\nArguments:\nfull_path (string): The path of the file to read.", end="")
    print("\nReturns: Every line in the file in the form of a list.", end="")
    
    print("\n\nfile_override(full_path, data):", end="")
    print("\nErases the contents of the file and writes given data.", end="")
    print("\nArguments:\nfull_path (string): The path of the file to read.", end="")
    print("\ndata (any type, optional): Data to be written to the file.", end="")
    print("\nReturns: None.", end="")
    print("\nNOTE: If file does not exist, this will create it.", end="")
    
    print("\n\nfile_append(full_path, data):", end="")
    print("\nAppends given data to the file.", end="")
    print("\nArguments:\nfull_path (string): The path of the file to read.", end="")
    print("\ndata (any type): Data to be written to the file.", end="")
    print("\nReturns: None.", end="")
    print("\nNOTE: If file does not exist, this will create it.", end="")

from tkinter.messagebox import showerror
import enum

class Error(enum.Enum):
    File_Not_Found = "File not found at \"full_path\" ."
    Path_NonString = "\"full_path\" was found to be a non-string value."

def file_read(full_path):
    '''
    Author: Udayshankar R

        Reads file at "full_path" and returns its data in a list.
    '''

    if type(full_path) != str:
        showerror("ERROR", str(Error.Path_NonString.value).split())
        return Error.Path_NonString

    try:
        read = []
        file = open(full_path, "r")
        read = list(file.read())
        file.close
        return read
    except FileNotFoundError:
        showerror("ERROR", str(Error.File_Not_Found.value).split())
        return Error.File_Not_Found

def file_readline(full_path):
    '''
        Author: Udayshankar R

        Reads file at "full_path" and returns the first line.
    '''

    if type(full_path) != str:
        showerror("ERROR", str(Error.Path_NonString.value).split())
        return Error.Path_NonString

    try:
        read = []
        file = open(full_path, "r")
        read = list(file.readline())
        file.close
        return read
    except FileNotFoundError:
        showerror("ERROR", str(Error.File_Not_Found.value).split())
        return Error.File_Not_Found

def file_readlines(full_path):
    '''
        Author: Udayshankar R
        
        Reads file at "full_path" and returns all data as lines in a list.
    '''
    
    if type(full_path) != str:
        showerror("ERROR", str(Error.Path_NonString.value).split())
        return Error.Path_NonString

    try:
        read = []
        file = open(full_path, "r")
        read = list(file.readlines())
        file.close
        return read
    except FileNotFoundError:
        showerror("ERROR", str(Error.File_Not_Found.value).split())
        return Error.File_Not_Found

def file_override(full_path, data = None):
    '''
        Author: Udayshankar R
    
        Clears all data in the file at "full_path".
        If "data" is provided, writes it into the file.

        NOTE: If file does not exist, this creates it.
    '''
        
    if type(full_path) != str:
        showerror("ERROR", str(Error.Path_NonString.value).split())
        return Error.Path_NonString

    file = open(full_path, "w")
    if data != None:
        file.write(str(data))
    file.close()

def file_append(full_path, data):
    '''
        Author: Udayshankar R
    
        Adds "data" to the file at "full_path".
        NOTE: If file does not exist, this creates it.
    '''
        
    if type(full_path) != str:
        showerror("ERROR", str(Error.Path_NonString.value).split())
        return Error.Path_NonString

    try:
        file = open(full_path, "a")
        file.write(str(data))
        file.close()
    except FileNotFoundError:
        showerror("ERROR", str(Error.File_Not_Found.value).split())
        return Error.File_Not_Found