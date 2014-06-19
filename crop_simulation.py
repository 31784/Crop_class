import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class CropWindow(QMainWindow):
    """this class creates a main window to observe the growth of a simulation"""

    #constructor
    def __init__(self):
        super().__init__() #call super class constructor
        self.setWindowTitle("Crop Simulator") #set window title

