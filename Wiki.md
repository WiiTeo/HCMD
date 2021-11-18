# HCMD Wiki

HCMD is a simple CLI make by WiiTeo

With HCMD you can :

- Create/Read file !
- Download file on the web !
- Install HLIB !
- and more...

### Part 1 : Commands

In HCMD, commands are very simple :

- To show the help page just type : "help"
- To read a file just type : "read"
- To write a file just type : "write"
- To show list all elements in dir just type : "list"
- To change dir just type : "cd"
- To back to a dir just type : "cdback"
- To install an hlib file just type : "hlib_install"
- To download file on the web just type : "get"

### Part 2 : HLIB

#### What is an HLIB file ?

An HLIB File is a Library for HCMD.

#### How to create an HLIB file ?

Thats very simple !

First, go to filesystem/ folder, and go to lib/ folder

Create a file named "mylib_lib.hlib" (this is an example name)

Open the file with a text editor

Write the example :

```
elif userType == "mylib":
    print("You use MyLib in your HCMD Lib folder")
```

And save.

Now open HCMD

Type the command : "hlib_install"

Now type the name of your hlib file (for example i choice mylib_lib.hlib)

And restart HCMD

Now your Lib is installed !

Type (for example) "mylib"

And "You use MyLib in your HCMD Lib Folder" appear !