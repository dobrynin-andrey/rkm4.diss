import sys
#import math
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (QWidget, QDesktopWidget, QToolTip, QPushButton, QApplication, QMessageBox, QMainWindow, QAction, qApp, QLabel, QLineEdit, QTextEdit, QGridLayout, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import QFont, QIcon 
#from PyQt5.QtCore import QCoreApplication 


# Визуализация приложения
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
    def initUI(self):
        
        '''
        #cancelButton = QPushButton("Cancel")
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        #hbox.addWidget(cancelButton)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        '''
        
        okButton = QPushButton("Рассчитать")
        okButton.clicked.connect(self.rkm4)
        step = QLabel('Размер шага:')
        final_x = QLabel('Решать с x = [0, xfinal]:')
        nach_x = QLabel('Начальное значение X:')
        nach_y = QLabel('Начальное значение Y:')
        znach_function= QLabel('Функция:')
        self.stepEdit = QLineEdit()
        self.final_xEdit = QLineEdit()
        self.nach_xEdit = QLineEdit()
        self.nach_yEdit = QLineEdit()
        self.znach_functionEdit = QLineEdit()
        
        lbl_otvet = QLabel('Ответ:')
        self.otvet = QLabel(self)
        #znach_functionEdit.textChanged[str].connect(self.rkm4)
        
        
        
        
        #eviewEdit = QTextEdit()
        
        '''
        zhachbox = QHBoxLayout()
        zhachbox.addStretch(1)
        zhachbox.addWidget(stepEdit)
        zhachbox.addWidget(final_xEdit)
        zhachbox.addWidget(nach_xEdit)
        Bbox = QVBoxLayout()
        Bbox.addStretch(1)
        Bbox.addLayout(hbox)
        
        '''
        grid = QGridLayout()
        grid.setSpacing(1)
        grid.addWidget(step, 1, 0)
        grid.addWidget(self.stepEdit, 1, 1)
        grid.addWidget(final_x, 1, 2)
        grid.addWidget(self.final_xEdit, 1, 3)
        grid.addWidget(nach_x, 2, 0)
        grid.addWidget(self.nach_xEdit, 2, 1)
        grid.addWidget(nach_y, 2, 2)
        grid.addWidget(self.nach_yEdit, 2, 3)
        grid.addWidget(znach_function, 3, 0)
        grid.addWidget(self.znach_functionEdit, 3, 1, 1, 1)
        grid.addWidget(lbl_otvet, 4, 0)
        grid.addWidget(self.otvet, 4, 1, 1, 1)
        grid.addWidget(okButton, 5, 0)
        
        
       # print step.text()
#        h = self.stepEdit.text()
         
        #print(h)
        
        
        # Click on button okButton
        
        #self.connect(okButton, QtCore.SIGNAL('clicked()'),
                    # self.rkm4)
        
        
        
        '''
        ## Реализация вплывающих подсказок
        # Задаем шрифт для подсказок и его размер
        QToolTip.setFont(QFont('SansSerif', 11))
        #self.setToolTip('This is a <b>QWidget</b> widget')
        # Создаем кнопку "Button"
        btn = QPushButton('Button', self)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)       
       
        # и подсказку для нее
        btn.setToolTip('Это подсказка для <b>Button</b>')
        '''
        # Кнопка выхода
        '''
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 100)
        
        
        # Создание окна программы: размеры и расположение, загловок, иконка
        # self.setGeometry(300, 300, 700, 500)
        
        exitAction = QAction(QIcon('exit.png'), '&Выход', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Выход из приложения')
        exitAction.triggered.connect(qApp.quit)
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Файл')
        fileMenu.addAction(exitAction)
        
        '''
        
        self.setLayout(grid) 
      # self.setLayout(vbox)
      # self.setLayout(Bbox) 
        
      # self.statusBar().showMessage('Ready')
        self.resize(700, 500)
        self.center()
        self.setWindowTitle('Вычисление ОДУ методом Рунге-Кутты')
        self.setWindowIcon(QIcon('exe.png'))        
        self.show()
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Выход', "Вы действительно хотите выйти?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()   
        
            
    def rkm4(self):
        self.resize(1000, 500)
        self.otvet.setText(self.znach_functionEdit.text())
        self.otvet.adjustSize()
        
     
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_()) 


'''
# Метод Рунге-Кутты 4-го порядка
# Пример dy/dx = sin(x)+cos(y), y(0)=5;


# Параметры
h = 0.1        # Размер шага
xfinal = 1     # Решать с x = [0, xfinal]

# Начальные значения
x = 0
y = 5

y0 = y

Xframe = [x]
Yframe = [y]
# Определим функцию ОДУ
function = math.sin(x)+math.cos(y)
lable_fun = str(math.sin(x)+math.cos(y))

def functionODU (x, y):
    f = function
    return f

# Цикл метода РК4
for i in range(math.ceil(xfinal/h)):

    k1 = functionODU (x        , y           )
    k2 = functionODU (x + 0.5*h, y + 0.5*k1*h)
    k3 = functionODU (x + 0.5*h, y + 0.5*k2*h)
    k4 = functionODU (x +     h, y +     k3*h)

    y = y + h/6*(k1 + 2*k2 + 2*k3 + k4)
    # Поместим y в массив
    Yframe += [y]
    # Поместим x в массив
    Xframe += [x]
    # Обновим x
    x = x + h;

print ('Это х: ', Xframe)
print ('Это у: ', Yframe)


'''
    #print ('Это k1: ', k1)
    #print ('Это k2: ', k2)
    #print ('Это k3: ', k3)
    #print ('Это k4: ', k4)
'''
# График результата

#plt.rc('font',**{'family':'verdana'})
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(Xframe, Yframe, "b-", label=lable_fun)
plt.legend()
plt.grid()
plt.show()


#plt.plot(Xframe, Yframe, 'r-')
#plt.show()
print ('Ответ: y('+ str(y0) + ') =', Yframe[-1])



'''

'''

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    label = QLabel ('<сеntеr>Привет , мир! </center>')
    w.show()
    
    sys.exit(app.exec_())

арр = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Пepвaя nрограмма а PyQt")
window.resize(ЗOO, 70)
label = QLabel ("<сеntеr>Привет , мир! </center>")
btnQuit = QPushButton("&Закрыть окно")
vbox = QVВoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQuit)
window.setLayout(vbox)
QtCore.QObject .connect (btnQuit, QtCore.SIGNAL ("clicked()"),
                         QtGui.qApp, QtCore.SLOT("quit()"))
window.show ()
sys.exit(app.exec_())



арр.= QtGui.QApplication(sys.argv)
window = QtGui.QWidget() #Создаем окно
window.setWindowТitle("Зaгoлoвoк окна") # Указываем заголовок
window.resize(300, 50) #Минимальные размеры
window. show () # Отображаем окно
sys.exit(app.exec ()) 
'''