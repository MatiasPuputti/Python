#Used to input keyboard presses.
import pyautogui
#Libary used to verify that folder with the input value exists.
import os

#Start of the folder path to the activation file.
Env_Fol = input("Virtual enviroment name: ")

#End path to the activation file.
Path_End = "\Scripts\\activate"

#Confirming folder with the input values exists. 
if os.path.exists(os.getcwd() + "\\" + Env_Fol + Path_End):
    #"Typing" the activation command.
    pyautogui.typewrite(Env_Fol + Path_End)

#Error message
else:
    print("ERROR: enviroment either not created, not in a current directory, or typed wrong.")
