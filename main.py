from time import sleep
from random import randint, choice
import signal
import sys

from PyQt5.Qt import *

colors = [Qt.red, Qt.blue, Qt.yellow, Qt.green]
 
qt_app = QApplication(sys.argv)
 
# Create a label widget with our text
label = QLabel('Hello, world!')

w, h = 50, 50

lights = []

def create_light():
    frm = QFrame()
    frm.sizeHint = lambda: QSize(w, h)
    lights.append(frm)
    x = randint(0, 1366)
    y = randint(0, 1024)

    color = choice(colors)

    p = frm.palette()
    p.setColor(frm.backgroundRole(), color)
    frm.setPalette(p)

    frm.setGeometry(x, y, 50, 50)
    frm.show()
   
def tick():
    create_light()

    if (len(lights) > 20):
        frm = lights.pop(0)
        frm.hide()

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

timer = QTimer()
timer.timeout.connect(tick)
timer.setInterval(100)
timer.start(100)

app.exec_()
