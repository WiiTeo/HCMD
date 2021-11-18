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
    print("\t# " + text + " #\n")

def help_page():
    print("\nhelp\t\t\t : Help Page of HShell.")
    print("list\t\t\t : Show all File or Directory in the current folder.")
    print("exit\t\t\t : Exit HCMD with code 0.")
    print("read\t\t\t : Read File")
    print("write\t\t\t : Create File")
    print("cd\t\t\t : Change Directory")
    print("cdback\t\t\t : Return to the principal dir")
    print("hlib_install\t\t : Install HLIB library")
    print("get\t\t\t : Download a file on the web")

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

        print(f"HCMD 1.1 (with Python {sys.version_info.major}.{sys.version_info.minor} for {systemos} OS)")
        print("\n Type 'help' to get the list of commands.\n")

        annonce("Version 1.1 !")

        while (1):

            userType = input("H:/>")

            if userType == "help":
                print(f"\nHCMD HShell, version 1.1 for {systemos}-Python.{sys.version_info.major}.{sys.version_info.minor}")
                print("This is the list of commands for HShell.")
                help_page()

            elif userType == "list":
                print("Elements in the directory : ")
                for allfiles in os.listdir():
                    print("   " + allfiles)

            elif userType == "exit":
                exit_with_code("0")
                # 0 = EXIT BY USER

            elif userType == "read":
                filename = input("Name of file : ")
                f = open(filename, "r")
                print(f.read())
                f.close()

            elif userType == "write":
                wfilename = input("Name of file : ")
                wf = open(wfilename, "w")
                wtext = input("Text : ")
                wf.write(wtext)
                print(wfilename + " has created !")
                wf.close()

            elif userType == "cd":
                wheredir = input("Name of Dir : ")

                if wheredir == "../":
                    print("Error ! To back use the command : 'cdback' ")
                
                else:
                    os.chdir(wheredir)

            elif userType == "cdback":
                if os.path.isfile(".hcmdf"):
                    print("ERROR ! You are in the root dir !")
                else:
                    os.chdir("../")

            elif userType == "hlib_install":
                libtoinstall = input("Name of HLIB to Install : ")
                os.chdir("lib")
                if os.path.isfile(libtoinstall):
                    print(libtoinstall + " found !")
                    hlib = open(libtoinstall, 'r')
                    os.chdir("../../")
                    hcmd_py = open("hcmd.py", "a")
                    for hlib_line in hlib:
                        hcmd_py.write("\n\n            " + hlib_line)
                    hcmd_py.close()
                    hlib.close()
                    print("HCMD require to restart to active the new library.")
                    exit_with_code("1")
                else:
                    print("Error ! The Lib file is not in the lib dir (H:/lib/)")
                    os.chdir("../")

            elif userType == "get":
                os.chdir("download")
                import urllib.request

                url = input('File URL (type "no" to cancel) : ')

                if url == "no":
                    print("Get commands cancel.")

                else:  
                    nurl = input("Name to the file : ")
                    urllib.request.urlretrieve(url, nurl)

                    print(nurl + " is download in downloads folder.")
                    os.chdir("../")

            # Lib Part #
