def help():
    print("\n\nSCUI will help you make UI for your python project.", end="")
    print("\nFor importing, type in \"from ShortCode.SCUI import *\".")
    
    print("\n\nGetRoot(title, size, colour, image_path):", end="")
    print("\nCreates and returns a Tk() window.", end="")
    print("\nArguments:\ntitle (string): The name of the window. If not", end="")
    print("\n\tprovided, default window name (\"SCUI_Window\") will be set.", end="")
    print("\nsize (string): The size of the window. If not", end="")
    print("\n\tprovided, default window size (\"512x512\") will be set.", end="")
    print("\ncolour (string, optional): The background colour of the window.", end="")
    print("\nimage_path (string, optional): The path to the image of the icon", end="")
    print("\n\tof the window. If not provided, default window icon", end="")
    print("\n\t(\"SCUI\") will be set. To remove it, enter \"None\" in its place.", end="")
    print("\nReturns: A Tk() window.", end="")
    
    print("\n\nGetMenu(root, commands, subcommands):", end="")
    print("\nCreates and returns a tkinter window menu, attached to window \"root\".", end="")
    print("\nArguments:\nroot (Tk window): The window to attach the menu to.", end="")
    print("\ncommands (dictionary, optional): The name of the menu, with commands. Eg:", end="")
    print("\n\t{\"Exit\" : commandname}", end="")
    print("\nsubcommands (nested dictionary, optional): Same as commands, but has options. Eg:", end="")
    print("\n\t{\"File\" : {\"Open\" : command1, \"Save\" : command2, \"Exit\" : command3}}", end="")
    print("\nReturns: A tkinter menu, already attached to the window.", end="")
    print("\nIMPORTANT: Even though \"commands\" and \"subcommands\" are marked as \'optional\',", end="")
    print("\n\tyou need to input either one of them for the menu to function.", end="")
    
    print("\n\nGetFont(family, size, weight):", end="")
    print("\nCreates and returns a tkinter.font font.", end="")
    print("\nArguments:\nfamily (string): The name of the font family. If not", end="")
    print("\n\tprovided, default font (\"Calibri\") will be set.", end="")
    print("\nsize (int): The font size. If not provided, default font", end="")
    print("\n\tsize (10) will be set.", end="")
    print("\nweight (string, optional): The weight of the font, eg: \"bold\".", end="")
    print("\nReturns: A tkinter.font font.", end="")
    
    print("\n\nGetLabel(root, text, image, width, height, font, colour):", end="")
    print("\nCreates and returns a tkinter label.", end="")
    print("\nArguments:\nroot (Tk window): The Tk window for the label", end="")
    print("\n\tto be displayed on.", end="")
    print("\ntext (string, optional): The text to be displayed on the label.", end="")
    print("\nimage (photoImage, optional): The image to be displayed on the label.", end="")
    print("\nwidth (int, optional): The width of the label.", end="")
    print("\nheight (int, optional): The height of the label.", end="")
    print("\nfont (tkinter.font font, optional): Font for the label\'s text.", end="")
    print("\ncolour (string, optional): Colour for the label\'s text, eg: \"green\".", end="")
    print("\nReturns: A tkinter label.", end="")
    print("\nIMPORTANT: Even though \"text\" and \"image\" are marked as \'optional\',", end="")
    print("\n\tyou need to input either one of them for the label to function.", end="")
    
    print("\n\nGetButton(root, text, function, image, width, height, font, bgColour, fgColour):", end="")
    print("\nCreates and returns a tkinter button that responds to the given function.", end="")
    print("\nArguments:\nroot (Tk window): The Tk window for the button", end="")
    print("\n\tto be displayed on.", end="")
    print("\ntext (string, optional): The text to be displayed on the button.", end="")
    print("\nimage (photoImage, optional): The image to be displayed on the button.", end="")
    print("\nfunction (function): The function for the button to respond to.", end="")
    print("\nwidth (int, optional): The width of the button.", end="")
    print("\nheight (int, optional): The height of the button.", end="")
    print("\nfont (tkinter.font font, optional): Font for the button\'s text.", end="")
    print("\nbgColour (string, optional): Colour for the button\'s background, eg: \"green\".", end="")
    print("\nfgColour (string, optional): Colour for the button\'s text, eg: \"blue\".", end="")
    print("\nReturns: A tkinter button.", end="")
    print("\nIMPORTANT: Even though \"text\" and \"image\" are marked as \'optional\',", end="")
    print("\n\tyou need to input either one of them for the button to function.", end="")
    
    print("\n\nGetDropDown(root, options, width, height, font, bgColour, fgColour):", end="")
    print("\nCreates and returns a tkinter dropdown with \"options\".", end="")
    print("\nArguments:\nroot (Tk window): The Tk window for the dropdown", end="")
    print("\n\tto be displayed on.", end="")
    print("\noptions (list/tuple): The options of the dropdown in a list/tuple.", end="")
    print("\nwidth (int, optional): The width of the dropdown.", end="")
    print("\nheight (int, optional): The height of the dropdown.", end="")
    print("\nfont (tkinter.font font, optional): Font for the dropdown\'s text.", end="")
    print("\nbgColour (string, optional): Colour for the dropdown\'s background, eg: \"green\".", end="")
    print("\nfgColour (string, optional): Colour for the dropdown\'s text, eg: \"blue\".", end="")
    print("\nReturns: A tkinter dropdown, a StringVar containing the option.", end="")
    print("\nTIP: Use the function like this: \"dropdown, option = GetDropDown(..., ..., ....)\",", end="")
    print("\n\tso that \"dropdown\" is the tkinter dropdown and \"option\" is the StringVar.", end="")
    print("\n\tThen you can use \"option.get()\" to get the option\'s string.", end="")
    
    print("\n\nGetEntry(root, outVar, default, width, font, bgColour, fgColour, borderSize):", end="")
    print("\nCreates and returns a tkinter entry.", end="")
    print("\nArguments:\nroot (Tk window): The Tk window for the entry", end="")
    print("\n\tto be displayed on.", end="")
    print("\noutVar (tkinter.StringVar(root)): The StringVar which contains the text in the entry.", end="")
    print("\ndefault (string, optional): The default text in the entry.", end="")
    print("\nwidth (int, optional): The width of the entry.", end="")
    print("\nfont (tkinter.font font, optional): Font for the entry\'s text.", end="")
    print("\nbgColour (string, optional): Colour for the entry\'s background, eg: \"green\".", end="")
    print("\nfgColour (string, optional): Colour for the entry\'s text, eg: \"blue\".", end="")
    print("\nReturns: A tkinter entry.", end="")
    print("\nTIP: To get the output write \"output = StringVar.get\". The \"StringVar\" is the", end="")
    print("\n\t\"outVar\" entered in the GetEntry function.", end="")
    
    print("\n\nIMPORTANT: For using a \"PhotoImage\", import it as:", end="")
    print("\n\t\'from tkinter import PhotoImage\'.\n\tFor creating a PhotoImage, type:", end="")
    print("\n\t\'image = PhotoImage(file=\'path/to/image.png\')\'.", end="")

    print("\n\nNOTE: tkinter grid support coming soon.")

from tkinter import *
from tkinter import font as f

from enum import *
from tkinter.messagebox import *
from types import FunctionType

class Error(Enum):
    Title_NonString = "\"Title\" was found to be a non-string value, aborting function."
    Size_NonString = "\"Size\" was found to be a non-string value, aborting function."
    Image_NonString = "\"Image_path\" was found to be a non-string value, aborting function."

    CommandsAndSubcommands_Null = "\"Commands\" nor \"Subcommands\" exist, aborting function."
    Commands_NonDictionary = "\"Commands\" was found to be a non-dictionary value, aborting function."
    Commands_Key_NonString = "Some of the keys of \"Commands\" were found to be non-string values, aborting function."
    Commands_Value_NonFunction = "Some of the values of \"Commands\" were found to be non-function values, aborting function."
    Subcommands_NonDictionary = "\"Subcommands\" was found to be a non-dictionary value, aborting function."
    Subcommands_Key_NonString = "Some of the keys of \"Subcommands\" were found to be non-string values, aborting function."
    Subcommands_Value_NonFunction = "Some of the values of \"Subcommands\" were found to be non-function values, aborting function."

    Family_NonString = "\"Family\" was found to be a non-string value, aborting function."
    Size_NonInt = "\"Size\" was found to be a non-integer value, aborting function."
    Weight_NonString = "\"Weight\" was found to be a non-string value, aborting function."

    Root_Null = "\"Root\" does not exist, aborting function."
    Root_NonWindow = "\"Root\" was found to be a non-Tkinter.Tk() value, aborting function."
    ImageAndText_Null = "\"Text\" nor \"Image_path\" exists, aborting function."
    Image_NonImage = "\"Image\" was found to be a non-photoImage value, aborting function."
    Text_NonString = "\"Text\" was found to be a non-string value, aborting function."
    Font_NonFont = "\"Font\" was found to be a non-font value, aborting function."
    Colour_NonString = "\"Colour\" was found to be a non-string value, aborting function."
    Width_NonInt = "\"Width\" was found to be a non-integer value, aborting function."
    Height_NonInt = "\"Height\" was found to be a non-integer value, aborting function."
    
    Text_Null = "\"Text\" does not exist, aborting function."

    Function_Null = "\"Function\" does not exist, aborting function."
    Function_NonFunction = "\"Function\" was found to be a non-function value, aborting function."
    BackgroundColour_NonString = "\"BgColour\" was found to be a non-string value, aborting function."
    FrontgroundColour_NonString = "\"FgColour\" was found to be a non-string value, aborting function."
    
    Options_Null = "\"Options\" does not exist, aborting function."
    Options_NonList = "\"Options\" was found to be a non-list/tuple value, aborting function."

    OutVar_Null = "\"OutVar\" does not exist, aborting function."
    OutVar_NonStringVar = "\"OutVar\" was found to be a non-StringVar value, aborting function."
    Default_NonString = "\"Default\" was found to be a non-string value, aborting function."
    Bordersize_NonInt = "\"BorderSize\" was found to be a non-int value, aborting function."

class Warning(Enum):
    Title_Null = "\"Title\" was null. \"root.title\" will be set as \"SCUI_Window\"."
    Image_Null = "\"Image_path\" was null. \"root.iconphoto\" will be set as \"SCUI_Logo\"."
    ImageAndText_Exist = "Both \"Text\" and \"Image\" have been inputted. This will cause issues. Removing \"Image_path\" ."
    CommandsAndSubcommands_Exist = "Both \"Commands\" and \"Subcommands\" have been inputed. This will cause issues. Removing \"Subcommands\" ."

useWarning = True
    
def GetRoot(title = "SCUI_Window", size = "512x512", colour = None, image_path = "ShortCode/Data/SCUI.png"):
    """
        Author: Udayshankar R

        Creates a Tkinter window and returns "root".
    """

    if type(title) != str:
        showerror("ERROR", str(Error.Title_NonString.value).split())
        return Error.Title_NonString
    if type(size) != str:
        showerror("ERROR", str(Error.Size_NonString.value).split())
        return Error.Size_NonString
    if colour != None and type(colour) != str:
        showerror("ERROR", str(Error.Colour_NonString.value).split())
        return Error.Colour_NonString

    root = Tk()
    root.title(title)
    root.geometry(size)

    if image_path != None:
        if type(image_path) != str and image_path != None:
            showerror("ERROR", str(Error.Image_NonString.value).split())
            return Error.Image_NonString

        if image_path == "Data/SCUI.png" and useWarning:
            showwarning("WARNING", str(Warning.Image_Null.value).split())
        
        if image_path != None:
            try:
                root.iconphoto(False, PhotoImage(file=image_path))
            except FileNotFoundError:
                string = "File: " + image_path + " does not exist, aborting function."
                showerror("ERROR", string.split())
                return None;

    if colour != None:
        root.config(bg= colour)

    if title == "SCUI_Window" and useWarning:
        showwarning("WARNING", str(Warning.Title_Null.value).split())
    
    return root

def GetMenu(root = None, commands = {}, subcommands = {}):
    """
        Author: Udayshankar R

        Creates a menu for the tkinter window.
    """

    if root == None:
        showerror("ERROR", str(Error.Root_Null.value).split())
        return Error.Root_Null
    if type(root) != Tk:
        showerror("ERROR", str(Error.Root_NonWindow.value).split())
        return Error.Root_NonWindow
    if (commands == {} or commands == None) and (subcommands == {} or subcommands == None):
        showerror("ERROR", str(Error.CommandsAndSubcommands_Null.value).split())
        return Error.CommandsAndSubcommands_Null
    if type(commands) != dict:
        showerror("ERROR", str(Error.Commands_NonDictionary.value).split())
        return Error.Commands_NonDictionary
    if type(subcommands) != dict and subcommands != None:
        showerror("ERROR", str(Error.Subcommands_NonDictionary.value).split())
        return Error.Subcommands_NonDictionary
   
    for i in commands.keys():
        if type(i) != str:
            showerror("ERROR", str(Error.Commands_Key_NonString.value).split())
            return Error.Commands_Key_NonString
    
    for i in commands.values():
        if type(i) != FunctionType:
            showerror("ERROR", str(Error.Commands_Value_NonFunction.value).split())
            return Error.Commands_Value_NonFunction

    if subcommands != {} and subcommands != None:
        for i in subcommands.keys():
            if type(i) != str:
                showerror("ERROR", str(Error.Subcommands_Key_NonString.value).split())
                return Error.Subcommands_Key_NonString

        for i in subcommands.values():
            if type(i) != dict:
                showerror("ERROR", str(Error.Subcommands_NonDictionary.value).split())
                return Error.Subcommands_NonDictionary
            for j in i.keys():
                if type(j) != str:
                    showerror("ERROR", str(Error.Subcommands_Key_NonString.value).split())
                    return Error.Subcommands_Key_NonString
                if type(i[j]) != FunctionType:
                    showerror("ERROR", str(Error.Subcommands_Value_NonFunction.value).split())
                    return Error.Subcommands_Value_NonFunction
    
    menu = Menu(root)
    
    if commands != {} and commands != None:
        for i in commands.keys():
            menu.add_command(label=str(i), command=commands[i])
    elif subcommands != {} and subcommands != None:
        for i in subcommands.keys():
            submenu = Menu(menu, tearoff=0)
            for j in subcommands[i].keys():
                submenu.add_command(label=str(j), command=subcommands[i][j])
            menu.add_cascade(label=i, menu=submenu)

    root.config(menu=menu)

    if (commands != {} and commands != None) and (subcommands != {} and subcommands != None) and useWarning:
        showwarning("WARNING", str(Warning.CommandsAndSubcommands_Exist.value).split())

    return menu
        
def GetFont(family = "Calibri", size = 10, weight = None):
    """
        Author: Udayshankar R

        Creates and returns a Tkinter.Font font. Default = "Calibri".
    """

    if type(family) != str:
        showerror("ERROR", str(Error.Family_NonString.value).split())
        return Error.Family_NonString
    if type(size) != int:
        showerror("ERROR", str(Error.Size_NonInt.value).split())
        return Error.Size_NonInt

    if weight != None:
        if type(weight) != str:
            showerror("ERROR", str(Error.Weight_NonString.value).split())
            return Error.Weight_NonString

        font = f.Font(family=family, size=size, weight=weight)
        return font
    else:
        font = f.Font(family=family, size=size)
        return font

def GetLabel(
    root = None,
    text = None,
    image = None,
    width = None,
    height = None,
    font = None,
    colour = None):
    """
        Author: Udayshankar R

        Creates and returns a Tkinter label.
    """

    if root == None:
        showerror("ERROR", str(Error.Root_Null.value).split())
        return Error.Root_Null
    if type(root) != Tk:
        showerror("ERROR", str(Error.Root_NonWindow.value).split())
        return Error.Root_NonWindow
    if text == None and image == None:
        showerror("ERROR", str(Error.ImageAndText_Null.value).split())
        return Error.ImageAndText_Null
    if text != None and type(text) != str:
        showerror("ERROR", str(Error.Text_NonString.value).split())
        return Error.Text_NonString
    if image != None and type(image) != PhotoImage:
        showerror("ERROR", str(Error.Image_NonImage.value).split())
        return Error.Image_NonString
    if width != None and type(width) != int:
        showerror("ERROR", str(Error.Width_NonInt.value).split())
        return Error.Width_NonInt
    if height != None and type(height) != int:
        showerror("ERROR", str(Error.Height_NonInt.value).split())
        return Error.Height_NonInt
    if font != None and type(font) != f.Font:
        showerror("ERROR", str(Error.Font_NonFont.value).split())
        return Error.Font_NonFont
    if colour != None and type(colour) != str:
        showerror("ERROR", str(Error.Colour_NonString.value).split())
        return Error.Colour_NonString
    
    
    label = Label(root)

    if text != None:
        label = Label(root, text=text)
        if font != None:
            label['font'] = font
        if colour != None:
            label['fg'] = colour
        if width != None:
            label['width'] = width
        if height != None:
            label['height'] = height
        label.pack()
    elif image != None:
        if width != None:
            image.config(width=width)
        if height != None:
            image.config(height=height)

        label = Label(root, image=image).pack()

    if text != None and image != None and useWarning:
        showwarning("WARNING", str(Warning.ImageAndText_Exist.value).split())

    return label
    
def GetButton(
    root = None,
    text = None,
    image = None,
    function = None,
    width = None,
    height = None,
    font = None,
    bgColour = None,
    fgColour = None):
    """
        Author: Udayshankar R

        Creates and returns a tkinter button which responds to "function".
    """

    if root == None:
        showerror("ERROR", str(Error.Root_Null.value).split())
        return Error.Root_Null
    if type(root) != Tk:
        showerror("ERROR", str(Error.Root_NonWindow.value).split())
        return Error.Root_NonWindow
    if text == None and image == None:
        showerror("ERROR", str(Error.ImageAndText_Null.value).split())
        return Error.ImageAndText_Null
    if text != None and type(text) != str:
        showerror("ERROR", str(Error.Text_NonString.value).split())
        return Error.Text_NonString
    if image != None and type(image) != PhotoImage:
        showerror("ERROR", str(Error.Image_NonImage.value).split())
        return Error.Image_NonString
    if function == None:
        showerror("ERROR", str(Error.Function_Null.value).split())
        return Error.Function_Null
    if type(function) != FunctionType:
        showerror("ERROR", str(Error.Function_NonFunction.value).split())
        return Error.Function_NonFunction
    if width != None and type(width) != int:
        showerror("ERROR", str(Error.Width_NonInt.value).split())
        return Error.Width_NonInt
    if height != None and type(height) != int:
        showerror("ERROR", str(Error.Height_NonInt.value).split())
        return Error.Height_NonInt
    
    if font != None and type(font) != f.Font:
        showerror("ERROR", str(Error.Font_NonFont.value).split())
        return Error.Font_NonFont
    if bgColour != None and type(bgColour) != str:
        showerror("ERROR", str(Error.BackgroundColour_NonString.value).split())
        return Error.BackgroundColour_NonString
    if fgColour != None and type(fgColour) != str:
        showerror("ERROR", str(Error.FrontgroundColour_NonString.value).split())
        return Error.FrontgroundColour_NonString

    button = Button(root, command=function)

    if text != None:
        button = Button(root, text=text, command=function)
        if font != None:
            button['font'] = font
        if bgColour != None:
            button['bg'] = bgColour
        if fgColour != None:
            button['fg'] = fgColour
        if width != None:
            button['width'] = width
        if height != None:
            button['height'] = height
        button.pack()
    elif image != None:
        if width != None:
            image.config(width=width)
        if height != None:
            image.config(height=height)
        button = Button(root, image=image, command=function).pack()
        
    if text != None and image != None and useWarning:
        showwarning("WARNING", str(Warning.ImageAndText_Exist.value).split())

    return button

def GetDropDown(
    root = None,
    options = None,
    width = None,
    height = None,
    font = None,
    bgColour = None,
    fgColour = None):
    """
        Author: Udayshankar R

        Creates and returns a tkinter dropdown with "options".
    """

    if root == None:
        showerror("ERROR", str(Error.Root_Null.value).split())
        return Error.Root_Null
    if type(root) != Tk:
        showerror("ERROR", str(Error.Root_NonWindow.value).split())
        return Error.Root_NonWindow
    if options == None:
        showerror("ERROR", str(Error.Options_Null.value).split())
        return Error.Options_Null
    if type(options) != list and type(options) != tuple:
        showerror("ERROR", str(Error.Options_NonList.value).split())
        return Error.Options_NonList
    if width != None and type(width) != int:
        showerror("ERROR", str(Error.Width_NonInt.value).split())
        return Error.Width_NonInt
    if height != None and type(height) != int:
        showerror("ERROR", str(Error.Height_NonInt.value).split())
        return Error.Height_NonInt

    if font != None and type(font) != f.Font:
        showerror("ERROR", str(Error.Font_NonFont.value).split())
        return Error.Font_NonFont
    if bgColour != None and type(bgColour) != str:
        showerror("ERROR", str(Error.BackgroundColour_NonString.value).split())
        return Error.BackgroundColour_NonString
    if fgColour != None and type(fgColour) != str:
        showerror("ERROR", str(Error.FrontgroundColour_NonString.value).split())
        return Error.FrontgroundColour_NonString

    if type(options) == tuple:
        options = list(options)

    clicked = StringVar()
    clicked.set(options[0])

    dropdown = OptionMenu(root, clicked, *options)

    if font != None:
        dropdown['font'] = font
    if bgColour != None:
        dropdown['bg'] = bgColour
    if fgColour != None:
        dropdown['fg'] = fgColour
    if width != None:
        dropdown['width'] = width
    if height != None:
        dropdown['height'] = height

    dropdown.pack()

    return dropdown, clicked

def GetEntry(
    root = None,
    outVar = None,
    default = None, 
    width = None,
    font = None,
    bgColour = None,
    fgColour = None,
    borderSize = None):
    """
        Author: Udayshankar R

        Creates and returns a tkinter entry.
    """
    
    if root == None:
        showerror("ERROR", str(Error.Root_Null.value).split())
        return Error.Root_Null
    if type(root) != Tk:
        showerror("ERROR", str(Error.Root_NonWindow.value).split())
        return Error.Root_NonWindow  
    if outVar == None:
        showerror("ERROR", str(Error.OutVar_Null.value).split())
        return Error.OutVar_Null
    if type(outVar) != StringVar:
        showerror("ERROR", str(Error.OutVar_NonStringVar.value).split())
        return Error.OutVar_NonStringVar
    if default != None and type(default) != str:
        showerror("ERROR", str(Error.Default_NonString.value).split())
        return Error.Default_NonString
    if width != None and type(width) != int:
        showerror("ERROR", str(Error.Width_NonInt.value).split())
        return Error.Width_NonInt
    if font != None and type(font) != f.Font:
        showerror("ERROR", str(Error.Font_NonFont.value).split())
        return Error.Font_NonFont
    if bgColour != None and type(bgColour) != str:
        showerror("ERROR", str(Error.BackgroundColour_NonString.value).split())
        return Error.BackgroundColour_NonString
    if fgColour != None and type(fgColour) != str:
        showerror("ERROR", str(Error.FrontgroundColour_NonString.value).split())
        return Error.FrontgroundColour_NonString
    if borderSize != None and type(borderSize) != int:
        showerror("ERROR", str(Error.Bordersize_NonInt.value).split())
        return Error.Bordersize_NonInt

    entry = Entry(root, textvariable=outVar)

    if width != None:
        entry['width'] = width
    if font != None:
        entry['font'] = font
    if bgColour != None:
        entry['bg'] = bgColour
    if fgColour != None:
        entry['fg'] = fgColour
    if borderSize != None:
        entry['bd'] = borderSize
    if default != None:
        entry.insert(END, default)
    entry.pack()

    return entry