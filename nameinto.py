import time
from colorama import init
from colorama import Fore, Back, Style
print(Fore.RED)
name = input("what's your name? ")
name = name.replace("-" , " ")
name = name.replace("_" , " ")
simbols = len(name)
space = name.count(" ")
print(Back.GREEN,Fore.RESET)
time.sleep(0.5)
print (f"you have {space} spaces")
time.sleep(0.5)
print(f"you have {simbols} sombols")
time.sleep(0.5)
print(Back.RESET,Fore.CYAN)
input (f"press enter to finish {name.lower()} ")
print(Back.RESET,Fore.RESET)