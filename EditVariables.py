import os
import hou
from PySide2 import QtCore
from PySide2 import QtWidgets

class EditVariables(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        hbox = QtWidgets.QFormLayout()
        
        self.setGeometry(300, 150, 250, 150)
        self.setWindowTitle('Variables')

        #JOB Path Label
        self.jobLabel = QtWidgets.QLabel('Enter JOB path: ', self)
        hbox.addWidget(self.jobLabel)
        
        #JOB Line Edit
        self.jobLine = QtWidgets.QLineEdit()
        self.jobLine.setMaxLength(300)
        hbox.addWidget(self.jobLine)
        
        #horizontal spacer
        self.hspace1 = QtWidgets.QSpacerItem(20,10)
        hbox.addItem(self.hspace1)

        #CACHE Path Label
        self.cacheLabel = QtWidgets.QLabel('Enter CACHE path: ', self)
        hbox.addWidget(self.cacheLabel)

        #CACHE Line Edit
        self.cacheLine = QtWidgets.QLineEdit()
        self.cacheLine.setMaxLength(300)
        hbox.addWidget(self.cacheLine)
        
        self.setLayout(hbox)
        
        #CONNECTIONS
        self.jobLine.returnPressed.connect(self.jobPATH)
        self.cacheLine.returnPressed.connect(self.cachePATH)

    def jobPATH(self):
        JOB_PATH = self.jobLine.text()
        hou.hscript("setenv JOB = %s"%JOB_PATH)
        hou.hscript("varchange JOB")
        
    def cachePATH(self):
        CACHE_PATH = self.cacheLine.text()
        hou.hscript("setenv CACHE = %s"%CACHE_PATH)
        hou.hscript("varchange CACHE")

app = EditVariables()        
app.show()
