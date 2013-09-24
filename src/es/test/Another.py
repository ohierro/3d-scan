'''
Created on Sep 24, 2013

@author: ohierro
'''
import sys
from PyQt4 import QtCore, uic
from PyQt4.QtGui import QDialog, QFileDialog, QGraphicsScene, QPixmap, QApplication

#from ui_imagedialog import Ui_ImageDialog

class ImageDialog(QDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self)        
        self.ui = uic.loadUi("/home/ohierro/git/scanner/main.ui",self)
        self.ui.show()
        
        self.dial.setValue(48)
        self.xLabel.setText('Aloh')        
        #self.update()
                

        self.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.analyze)
        self.connect(self.loadFileButton, QtCore.SIGNAL('clicked()'), self.loadFile)
        
    def analyze(self):
        print 'clicked'
        
    def loadFile(self):
        path = QFileDialog.getOpenFileName()
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(path))
        
        self.graphicsView.setScene(scene)
        print 'loading ' + path
        
        # Make some local modifications.
        #self.ui.colorDepthCombo.addItem("2 colors (1 bit per pixel)")

        # Connect up the buttons.
        #self.ui.okButton.clicked.connect(self.accept)
        #self.ui.cancelButton.clicked.connect(self.reject)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ImageDialog()
    sys.exit(app.exec_())