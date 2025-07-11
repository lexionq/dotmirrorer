# dotmirrorer 💻
Copy your dotfiles and dotfolders in your user directory to the desired location! 🚀💾

This project coded for Linux!🐧

>[!CAUTION]
> The developer lexionq is not responsible for file losses and system errors that may occur.

>[!TIP]
> When you run the program, if you say yes to copy dotfolders, you will copy more and more important settings folders.

# Installation

## Install Git
Before, install the Git if you didn't install:

`apt install git` 
>[!NOTE]
> If your distribution isn't Ubuntu-based or Debian-based, you may have different package manager. You must install the Git with your package manager(yay,pacman etc.)

## Clone Repository
Then, clone this repository:

`git clone https://github.com/lexionq/dotmirrorer` 

Enter cloned repository:

`cd dotmirrorer`

And install Python dependencies:

`pip3 install -r requirements.txt` or `pip install -r requirements.txt`
>[!WARNING]
>You may get errors when installing Python dependencies. Here's what to do if you get an error:
> 1. `python3 -m venv venv`
>
> 2. In Bash:
>`source venv/bin/activate`
>
> 3. In Fish Shell:
>
> 4. And install Python dependencies again:
>`pip3 install -r requirements.txt`
>
> 5. Run the program
> `python3 dotmirrorer.py`
>
> Each time you want to run the program, you will need to do step 2 or 3 again, depending on the shell you are using, and then run the program.

## Run Program
If you don't get an error, directly run the program:
`python3 dotmirrorer.py`

# Usage
The first time you run the program it says `This tool copies dotfiles from the user directory to the desired location. Do you want dotfolders to be copied too? ( y / n )` you will get such a question.  If you say yes (y), your dotfolders will be backed up as well as folders like `.config` for example. But if you say no, there will be no backup for your dotfolders.

Then, the program will ask you for a folder for backup and you will enter the path of the folder you want for backup.

Then you don't have to do anything. The program will back up all the DotFiles and Dotfolders you want to back up in your user directory to the folder you want to back up.





