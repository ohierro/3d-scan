import sys
from PyQt4 import QtGui, QtCore, uic
 
class TestApp(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
 
        self.ui = uic.loadUi('/home/ohierro/git/scanner/main.ui')
        self.ui.show()
 
        #self.connect(self.ui.doubleSpinBox, QtCore.SIGNAL("valueChanged(double)"), spinFn)
        #self.connect(self.ui.comboBox, QtCore.SIGNAL("currentIndexChanged(QString)"), comboFn)
        #self.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), buttonFn)
        self.connect(self.ui.analyzeButton, QtCore.SIGNAL("clicked()"), analyzeClick)
                
 
 
def analyzeClick(self):
    print 'click'

# def spinFn(value):
#     win.ui.doubleSpinBoxLabel.setText('doubleSpinBox is set to ' + str(value))
#def buttonFn():
#     win.ui.setWindowTitle(win.ui.lineEdit.text())
# def comboFn(value):
#     win.ui.comboBoxLabel.setText(str(value) + ' is selected')
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win = TestApp()
    sys.exit(app.exec_())