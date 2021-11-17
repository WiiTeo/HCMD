import os
import sys

# HCMD #
# By WiiTeo

# Check OS

if os.name == "nt":
    systemos = "Windows"
elif os.name == "posix":
    systemos == "Linux"
else:
    systemos == "Unexpected"

# Def part

def clear_screen():
    if systemos == "Windows":
        os.system("cls")
    elif systemos == "Linux":
        os.system("clear")
    else:
        print("Your os in unexpected for HCMD. We can't clear the screen")

def annonce(text):
    print("\n\t# " + text + " #")

def help_page():
    print("\nhelp\t\t\t : Help Page of HShell.")
    print("list\t\t\t : Show all File or Directory in the current folder.")
    print("exit\t\t\t : Exit HCMD with code 0.")

def exit_with_code(code):
    print("Exit with code " + code + ".")
    exit()

# end def part

# class start

class change_dir:
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

# end class start

# start of program

clear_screen()
with change_dir("filesystem"):

    print(f"HCMD 1.0 (with Python {sys.version_info.major}.{sys.version_info.minor} for {systemos} OS)")
    print("\n Type 'help' to get the list of commands.\n")

    while (1):

        userType = input("H:/>")

        if userType == "help":
            print(f"\nHCMD HShell, version 1.0 for {systemos}-Python.{sys.version_info.major}.{sys.version_info.minor}")
            print("This is the list of commands for HShell.")
            help_page()

        elif userType == "list":
            print("Elements in the directory : ")
            for allfiles in os.listdir():
                print("   " + allfiles)

        elif userType == "exit":
            exit_with_code("0")