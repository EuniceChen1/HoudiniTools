import os
import hou
import sys
from PySide2 import QtCore
from PySide2 import QtWidgets

class EditVariables(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        hbox = QtWidgets.QFormLayout()
        
        self.setGeometry(250, 150, 250, 200)
        self.setMaximumSize(QtCore.QSize(250, 250))
        self.setWindowTitle('Edit Variables')
        
        #Project Path Label
        self.projLabel = QtWidgets.QLabel('Enter Project path: ', self)
        hbox.addWidget(self.projLabel)

        #Project Line Edit
        self.projLine = QtWidgets.QLineEdit()
        self.projLine.setMaxLength(300)
        hbox.addWidget(self.projLine)

        #JOB Path Label
        self.jobLabel = QtWidgets.QLabel('Enter JOB path: ', self)
        hbox.addWidget(self.jobLabel)
        
        #JOB Line Edit
        self.jobLine = QtWidgets.QLineEdit()
        self.jobLine.setMaxLength(300)
        hbox.addWidget(self.jobLine)
        
        #CACHE Path Label
        self.cacheLabel = QtWidgets.QLabel('Enter CACHE path: ', self)
        hbox.addWidget(self.cacheLabel)

        #CACHE Line Edit
        self.cacheLine = QtWidgets.QLineEdit()
        self.cacheLine.setMaxLength(300)
        hbox.addWidget(self.cacheLine)
        
        #vertical spacer
        self.vspace1 = QtWidgets.QSpacerItem(1,8)
        hbox.addItem(self.vspace1)
        
        #OK Button
        self.OKBt = QtWidgets.QPushButton('OK')
    
        hbox.addWidget(self.OKBt)

      
        self.setLayout(hbox)
        
        #CONNECTIONS
        self.projLine.textChanged.connect(self.dirName)
        self.jobLine.returnPressed.connect(self.jobPATH)
        self.cacheLine.returnPressed.connect(self.cachePATH)
        self.OKBt.clicked.connect(self.OKButton)
        
    def dirName(self):   
        if sys.platform == 'win32':
            JOBdir = r'C:/mnt/animation/'+self.projLine.text()+"/asset/images/cg/"
            CACHEdir = r'C:/mnt/animation/'+self.projLine.text()+"/asset/cache/"
            
            self.jobLine.setText(JOBdir)
            self.cacheLine.setText(CACHEdir)
            
        elif sys.platform == 'linux':
            JOBdir = r'/mnt/animation/'+self.projLine.text()+"/asset/images/cg/"
            CACHEdir = r'/mnt/animation/'+self.projLine.text()+"/asset/cache/"
            
            self.jobLine.setText(JOBdir)
            self.cacheLine.setText(CACHEdir)
        
    def OKButton(self):
        JOB_PATH= (self.jobLine.text()).replace('\\','/')
        hou.hscript("setenv JOB = %s"%JOB_PATH)
        hou.hscript("varchange JOB")
        
        CACHE_PATH = (self.cacheLine.text()).replace('\\','/')
        hou.hscript("setenv CACHE = %s"%CACHE_PATH)
        hou.hscript("varchange CACHE")
        self.close()

    def jobPATH(self):
        JOB_PATH= (self.jobLine.text()).replace('\\','/')
        hou.hscript("setenv JOB = %s"%JOB_PATH)     
        hou.hscript("varchange JOB")
        
    def cachePATH(self):
        CACHE_PATH = (self.cacheLine.text()).replace('\\','/')
        hou.hscript("setenv CACHE = %s"%CACHE_PATH)
        hou.hscript("varchange CACHE")

dialog = EditVariables()        
dialog.show()
