#Used to input keyboard presses.
import pyautogui

Py_Ver = input("Python version to base virtual enviroment from: ")

#Start of the command to create virtual enviroment.
Path_Start = "virtualenv -p C:\Py\Py_"

#Midle part of the command.
Path_Middle = "\python.exe"

#Changed after the input value is in right format.
Float_Bool = False

#Changed after input value is in versions directory.
Float_In_Versions = False

#Installed python versions.
Versions =  {
           2 : 3.4,
           3 : 3.5,
           5 : 3.6,
           7 : 3.7,
           8 : 3.8,
            }

#Run loop until float is found that exists in the directory.
while not Float_In_Versions:
    #Run loop until input value is on right format and is in the dictionary.
    while not Float_Bool or not Float_In_Versions:
        try:
            #If float is on the wrong format skip to exeption and start again, if float is not in the dictionary values, ask for new and start again.
            if float(Py_Ver) or not Float_In_Versions:
                #Set values to end loops and ask for enviroment name.
                if float(Py_Ver) in Versions.values():
                    Float_Bool = True
                    Float_In_Versions = True
                    VE_Name = input("Enviroment name: ")
                else:
                    Py_Ver = input("Version value not in dictionary, ensure right version and input: ")
                    pass
        except ValueError:
            Py_Ver = input("Version value invalid, enter value in the format like (3.6): ")
            Float_Bool = False
#After exiting both loops "type" command to create new virtual enviroment.
pyautogui.typewrite(Path_Start + Py_Ver + Path_Middle + " " + VE_Name)
