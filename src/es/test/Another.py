'''
Created on Sep 24, 2013

@author: ohierro
'''
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QDialog, QFileDialog, QGraphicsScene, QPixmap, QImage, QApplication, QColor

#from ui_imagedialog import Ui_ImageDialog

class ImageDialog(QDialog):
    image = None
    
    def __init__(self, parent = None):
        QDialog.__init__(self)        
        self.ui = uic.loadUi("/home/ohierro/git/scanner/main.ui",self)        
        self.ui.show()
        
        self.dial.setValue(48)
        self.xLabel.setText('Aloh')        
        #self.update()
                
        self.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.analyze)
        self.connect(self.loadFileButton, QtCore.SIGNAL('clicked()'), self.loadFile)
        
        self.loadFileFromFile('/home/ohierro/Pictures/test.png')
        
    def analyze(self):
        global image
        
        print 'Height: ' + str(image.height()) + ' - Width: ' + str(image.width())
        
        outputImage = QImage(image.width(),image.height(),image.format())
        
        for i in range(0,image.height()):
            line = image.scanLine(i)
            for j in range(0,image.width()):
                pixel = image.pixel(j,i)
                print str(i) + ':' + str(j) + ' => (' + str(QtGui.qRed(pixel)) + ',' + str(QtGui.qGreen(pixel)) + ',' + str(QtGui.qBlue(pixel)) + ')'
                
                if (QtGui.qRed(pixel) > 225 and QtGui.qGreen(pixel) == 0 and QtGui.qBlue(pixel) == 0):
                    outputImage.setPixel(j,i, QtGui.qRgb(255,0,0))        
                else:
                    outputImage.setPixel(j,i, QtGui.qRgb(0,0,0))
                                                       
                #colors = QColor(line[j]).getRgbF()
                #print "(%s,%s) = %s" % (i, j, colors)
            
        self.displayOutput(outputImage)
        print 'clicked'
        
    def loadFile(self):
        global image
        
        path = QFileDialog.getOpenFileName()
        
        image = QImage(path) 
        
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(path))
        
        self.graphicsView.setScene(scene)
        print 'loading ' + path
        
    def loadFileFromFile(self,path):
        global image
        
        image = QImage(path) 
        
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(path))
        
        self.graphicsView.setScene(scene)
        print 'loading ' + path
        
    def displayOutput(self,image):
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap.fromImage(image))
        
        self.analysisView.setScene(scene)
        print 'displayOutput'
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ImageDialog()
    sys.exit(app.exec_())