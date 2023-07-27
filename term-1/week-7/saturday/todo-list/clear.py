import os
import platform

def clear_terminal():
    current_platform = platform.system()
    if current_platform == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
