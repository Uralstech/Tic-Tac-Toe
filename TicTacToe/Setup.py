import os, sys
import winshell
from win32com.client import Dispatch
path = list(os.getcwd().split("\\"))
edpath = ""
for i in path:
    edpath += i + "/"

sys.path
sys.path.append(edpath + "ShortCode/")

from ShortCode.SCUI import *

root = GetRoot("Shortcut Setup", "500x170", image_path=(edpath + "ShortCode/Data/SCUI.png"))
root.resizable(False, False)
buff = GetLabel(root, "")

newpath = StringVar(root)

entry = GetEntry(root, newpath, str(winshell.desktop()), 45, GetFont(size=15), borderSize=3,)
entry.pack()

info = GetLabel(root, "Enter where you want the shortcut created", font=GetFont(size=15))
buff = GetLabel(root, "")

def CreateShortcut():
    desktop = winshell.desktop()
    path = os.path.join(newpath.get(), "TicTacToe.lnk")
    target = os.getcwd() + r"\TicTacToe.exe"
    wDir = os.getcwd()
    icon = os.getcwd() + r"\TicTacToe.exe"
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()

    root.destroy()

button = GetButton(root, "Confirm", function=CreateShortcut, font=GetFont(size=15), width=15)

root.mainloop()