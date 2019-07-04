import sys
from PyQt5.QtWidgets import *

out = sys.stdout
sys.stdout = open(r"./my_help_txt.txt", 'w')
help(QTextEdit)
sys.stdout.close()
sys.stdout = out
