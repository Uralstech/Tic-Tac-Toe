from enum import Enum

class UIError(Enum):
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

class UIWarning(Enum):
    Title_Null = "\"Title\" was null. \"root.title\" will be set as \"SCUI_Window\"."
    Image_Null = "\"Image_path\" was null. \"root.iconphoto\" will be set as \"SCUI_Logo\"."
    ImageAndText_Exist = "Both \"Text\" and \"Image\" have been inputted. This will cause issues. Removing \"Image_path\" ."
    CommandsAndSubcommands_Exist = "Both \"Commands\" and \"Subcommands\" have been inputed. This will cause issues. Removing \"Subcommands\" ."