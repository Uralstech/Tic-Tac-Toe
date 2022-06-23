from tkinter import *
from tkinter import font as f

from tkinter.messagebox import *
from ShortCode.InDev.UIExceptions import UIWarning as Warning
from ShortCode.InDev.UIExceptions import UIError as Error
from types import FunctionType

show_warning = True

def GetRoot(title = "SCUI_Window", size = "512x512", colour = None, image_path = "ShortCode/InDev/Data/SCUI.png"):
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

        if image_path == "Data/SCUI.png" and show_warning:
            showwarning("WARNING", str(Warning.Image_Null.value).split())
        
        if image_path != None:
            try:
                root.iconphoto(False, PhotoImage(file = image_path))
            except FileNotFoundError:
                string = "File: " + image_path + " does not exist, aborting function."
                showerror("ERROR", string.split())
                return None;

    if colour != None:
        root.config(bg= colour)

    if title == "SCUI_Window" and show_warning:
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
    if type(root) != Tk and type(root) != Toplevel:
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

    if (commands != {} and commands != None) and (subcommands != {} and subcommands != None) and show_warning:
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
    if type(root) != Tk and type(root) != Toplevel:
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

    if text != None and image != None and show_warning:
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
    if type(root) != Tk and type(root) != Toplevel:
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
        
    if text != None and image != None and show_warning:
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
    if type(root) != Tk and type(root) != Toplevel:
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
    if type(root) != Tk and type(root) != Toplevel:
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