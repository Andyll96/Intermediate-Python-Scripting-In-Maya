from tkinter import Spinbox
from maya import cmds
from PySide2 import QtWidgets, QtGui, QtCore

"""A script that generates a field of spheres that are offset by their position, size and color to create a wave
"""

class rainbowWaveController():

    def createField(self, length=1, width=1, height=1):
        print(f'length: {length}\nwidth: {width}\nheight: {height}')
        self.deleteExisting()
        for l in range(length):
            for w in range(width):
                for h in range(height):
                    sphereName = f'sphere_{l}_{w}_{h}'
                    cmds.polySphere(name=f'{sphereName}_geo', r=0.3, sx=8, sy=8)
                    cmds.polySoftEdge(angle=180, constructionHistory=0)

                    # be careful that your naming objects the same thing, as Maya will automatically renumber it
                    cmds.group(name=f'{sphereName}_grp')
                    cmds.move(l, h, w)
                    cmds.select(f'{sphereName}_geo')
                    cmds.move(l + 0.5, h, w)

                    # l+w+h is the offset which is different for every circle
                    cmds.expression(s=f'{sphereName}_grp.rotateX = (time + {l + w + h}) * 30')
                    cmds.expression(s=f'{sphereName}_grp.rotateY = (time + {l + w + h}) * 30')
                    cmds.expression(s=f'{sphereName}_grp.rotateZ = (time + {l + w + h}) * 30')

                    # offset = random.uniform(0,1)
                    # cmds.expression(s=f'{sphereName}_geo.scaleX = abs(sin(time) + 1/{l+w+h+1})')
                    # cmds.expression(s=f'{sphereName}_geo.scaleY = abs(sin(time) + 1/{l+w+h+1})')
                    # cmds.expression(s=f'{sphereName}_geo.scaleZ = abs(sin(time) + 1/{l+w+h+1})')

    def deleteExisting(self):
        cmds.select(clear=True)
        objects = cmds.ls(dag=True, long=True)
        print(f'objects:\n{objects}')
        for obj in objects:
            if('_grp' in obj and '_geo' not in obj):
                cmds.select(obj)
                cmds.delete()
                # print(f'Deleted: {obj}')

class rainbowWaveUI(QtWidgets.QDialog):
    def __init__(self):
        super(rainbowWaveUI, self).__init__()
        self.setWindowTitle("Rainbow Wave")
        self.setFixedSize(QtCore.QSize(400,500))
        self.library = rainbowWaveController()
        self.spinBox1Val = 0
        self.spinBox2Val = 0
        self.spinBox3Val = 0
        self.buildUI()
        
    def buildUI(self):
        layout = QtWidgets.QVBoxLayout(self)
        Hlayout1 = QtWidgets.QHBoxLayout()
        Hlayout2 = QtWidgets.QHBoxLayout()
        Hlayout3 = QtWidgets.QHBoxLayout()


        label1 = QtWidgets.QLabel('Width(X):')
        self.spinBox1 = QtWidgets.QSpinBox()
        self.spinBox1.setRange(1,10)
        self.spinBox1.valueChanged.connect(self.updateSpinBox1Val)
        Hlayout1.addWidget(label1)
        Hlayout1.addWidget(self.spinBox1)
        layout.addLayout(Hlayout1)

        slider1 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        slider1.setRange(1,10)
        slider1.sliderMoved.connect(self.spinBox1.setValue)
        self.spinBox1.valueChanged.connect(slider1.setValue)
        layout.addWidget(slider1)

        label2 = QtWidgets.QLabel('Length(Z):')
        self.spinBox2 = QtWidgets.QSpinBox()
        self.spinBox2.setRange(1,10)
        self.spinBox2.valueChanged.connect(self.updateSpinBox2Val)
        Hlayout2.addWidget(label2)
        Hlayout2.addWidget(self.spinBox2)
        layout.addLayout(Hlayout2)
        
        slider2 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        slider2.setRange(1,10)
        slider2.sliderMoved.connect(self.spinBox2.setValue)
        self.spinBox2.valueChanged.connect(slider2.setValue)
        layout.addWidget(slider2)
        
        label3 = QtWidgets.QLabel('Height(Y):')
        self.spinBox3 = QtWidgets.QSpinBox()
        self.spinBox3.setRange(1,10)
        self.spinBox3.valueChanged.connect(self.updateSpinBox3Val)
        Hlayout3.addWidget(label3)
        Hlayout3.addWidget(self.spinBox3)
        layout.addLayout(Hlayout3)

        slider3 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        slider3.setRange(1,10)
        slider3.sliderMoved.connect(self.spinBox3.setValue)
        self.spinBox3.valueChanged.connect(slider3.setValue)
        layout.addWidget(slider3)
        
        generateButton = QtWidgets.QPushButton('Generate')
        generateButton.clicked.connect(self.generate)
        layout.addWidget(generateButton)

    def updateSpinBox1Val(self, i):
        self.spinBox1Val = i

    def updateSpinBox2Val(self, i):
        self.spinBox2Val = i

    def updateSpinBox3Val(self, i):
        self.spinBox3Val = i

    def generate(self):
        self.library.createField(self.spinBox1Val, self.spinBox2Val, self.spinBox3Val)

def showUI():
    ui = rainbowWaveUI()
    ui.show()
    return ui

# you have to store in a variable otherwise Maya's garbage collector will
ui = showUI()