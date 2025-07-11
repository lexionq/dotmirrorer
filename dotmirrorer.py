# This tool copies all your dotfiles and dotfolders to the location of your choice and creates a timestamp. You may need this application when you change and reset your system or in other different situations.
# LEXIONQ IS NOT RESPONSIBLE FOR ANY FILE LOSS THAT MAY OCCUR!
# The developer lexionq is not responsible for file losses and system errors that may occur.
# Follow me on GitHub : https://github.com/lexionq

import os
import shutil
from datetime import datetime
from colorama import init, Fore, Style
init(autoreset=True)

copy_dotfolders = False


home_dir = os.path.expanduser("~")

dot_files = []

print(Fore.MAGENTA + Style.BRIGHT + "This tool copies dotfiles from the user directory to the desired location. Do you want dotfolders to be copied too? ( y / n )", end="")
copy_dotfolders_option = input()
if copy_dotfolders_option == "y":
    copy_dotfolders = True

print(Fore.WHITE + Style.BRIGHT + "Enter a folder or memory path to back up: ", end="")
dest_path = input()

if not os.path.exists(dest_path):
    print(Fore.RED + Style.BRIGHT + "[! ERROR !] Not a valid directory.")
    exit(1)

timestamp = datetime.now().strftime("%d %m %Y %H:%M:%S")
dest_dir = os.path.join(dest_path, f"dotfiles_backup_{timestamp}")
os.makedirs(dest_dir, exist_ok=True)

print(Fore.BLUE + Style.BRIGHT + f"[? INFO ?] Backup started: {dest_dir}\n")
print(Fore.BLUE + Style.BRIGHT + f"[? INFO ?] Listing directory: {home_dir}\n")

for item in os.listdir(home_dir):
    if item.startswith(".") and item not in [".",".."]:
        src_path = os.path.join(home_dir, item)
        dst_path = os.path.join(dest_dir, item)

        try: 
            if copy_dotfolders == True:
                if os.path.isfile(src_path):
                    shutil.copy2(src_path, dst_path)
                    print(Fore.GREEN + Style.BRIGHT + f"[✓ SUCCESSFULL ✓] File copied: {item}")
                elif os.path.isdir(src_path):
                    shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
                    print(Fore.GREEN + Style.BRIGHT + f"[✓ SUCCESSFULL ✓] Folder copied: {item}")
            else:
                if os.path.isfile(src_path):
                    shutil.copy2(src_path, dst_path)
                    print(Fore.GREEN + Style.BRIGHT + f"[✓ SUCCESSFULL ✓] File copied: {item}")
                elif os.path.isdir(src_path):
                    print(Fore.BLUE + Style.BRIGHT + f"[? INFO ?] The folder {src_path}, could not be copied because you had previously said you did not want it.")
        except Exception as e :
            print(Fore.RED + Style.BRIGHT + f"[! ERROR !] {item}:{e}")

print(Fore.GREEN + Style.BRIGHT + f"[✓ SUCCESSFULL ✓] Files and folders copied to: {dest_dir}")
