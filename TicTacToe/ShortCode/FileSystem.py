def check(full_path, encoding):
    assert type(full_path) == str, f'\'full_path\' is of {type(full_path)}. Only type \'str\' is acceptable.'
    assert full_path != "", "\'full_path\' is empty."
    assert type(encoding) == str, f'\'full_path\' is of {type(encoding)}. Only type \'str\' is acceptable.'
    assert encoding != "", "\'encoding\' is empty."

def file_read(full_path: str, encoding = "utf8"):
    '''
    Author: Udayshankar R

        Reads file at "full_path" and returns its data in a list.
    '''

    check(full_path, encoding)

    read = []
    file = open(full_path, "r", encoding=encoding)
    read = list(file.read())
    file.close
    return read

def file_readline(full_path: str, encoding = "utf8"):
    '''
        Author: Udayshankar R

        Reads file at "full_path" and returns the first line.
    '''

    check(full_path, encoding)

    read = []
    file = open(full_path, "r", encoding=encoding)
    read = list(file.readline())
    file.close
    return read

def file_readlines(full_path: str, encoding = "utf8"):
    '''
        Author: Udayshankar R
        
        Reads file at "full_path" and returns all data as lines in a list.
    '''
    
    check(full_path, encoding)
    
    read = []
    file = open(full_path, "r", encoding=encoding)
    read = list(file.readlines())
    file.close
    return read

def file_override(full_path: str, data = "", encoding = "utf8"):
    '''
        Author: Udayshankar R
    
        Clears all data in the file at "full_path".
        If "data" is provided, writes it into the file.

        NOTE: If file does not exist, this creates it.
    '''

    check(full_path, encoding)
    
    file = open(full_path, "w", encoding=encoding)
    if data != "":
        file.write(str(data))
    file.close()

def file_append(full_path: str, data: str, encoding = "utf8"):
    '''
        Author: Udayshankar R
    
        Adds "data" to the file at "full_path".
        NOTE: If file does not exist, this creates it.
    '''

    check(full_path, encoding)
    
    file = open(full_path, "a", encoding=encoding)
    file.write(data)
    file.close()

def file_exists(full_path: str):
    '''
        Author: Udayshankar R
    
        Checks if file at "full_path" exists.
        Returns True if it does, otherwise False.
    '''

    try:
        file = open(full_path, "r")
        file.close()
        return True
    except FileNotFoundError:
        return False