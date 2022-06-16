from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.Qt3DCore import *

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('calc.ui', None)
        self.ui.show()

        # numbers
        self.ui.btn0.clicked.connect(partial(self.nums,"0"))
        self.ui.btn1.clicked.connect(partial(self.nums,"1"))
        self.ui.btn2.clicked.connect(partial(self.nums,"2"))
        self.ui.btn3.clicked.connect(partial(self.nums,"3"))
        self.ui.btn4.clicked.connect(partial(self.nums,"4"))
        self.ui.btn5.clicked.connect(partial(self.nums,"5"))
        self.ui.btn6.clicked.connect(partial(self.nums,"6"))
        self.ui.btn7.clicked.connect(partial(self.nums,"7"))
        self.ui.btn8.clicked.connect(partial(self.nums,"8"))
        self.ui.btn9.clicked.connect(partial(self.nums,"9"))

        # elements
        self.ui.btnac.clicked.connect(self.ac)
        self.ui.btnpercent.clicked.connect(self.percent)
        self.ui.btndiv.clicked.connect(self.div)
        self.ui.btnmul.clicked.connect(self.mul)
        self.ui.btnmin.clicked.connect(self.minus)
        self.ui.btnadd.clicked.connect(self.add)
        self.ui.btndot.clicked.connect(self.dot)
        self.ui.ebtn.clicked.connect(self.equal)
    
    def nums(self, Number):
        self.ui.view.setText(self.ui.view.toPlainText() + Number)
    
    def ac(self):
        self.ui.view.setText("")

    def percent(self):
        self.placeholder = "%"
        self.num1 = float(self.ui.view.toPlainText())
        self.ui.view.setText("")
        self.ui.view.setText(str(self.num1 / 100))

    def div(self):
        self.placeholder = "/"
        self.num1 = float(self.ui.view.toPlainText())
        self.ui.view.setText("")
    
    def mul(self):
        self.placeholder = "x"
        self.num1 = float(self.ui.view.toPlainText())
        self.ui.view.setText("")
    
    def minus(self):
        self.placeholder = "-"
        self.num1 = float(self.ui.view.toPlainText())
        self.ui.view.setText("")

    def add(self):
        self.placeholder = "+"
        self.num1 = float(self.ui.view.toPlainText())
        self.ui.view.setText("")

    def dot(self):
        if "." in self.ui.view.toPlainText():
            self.ui.view.setText(self.ui.view.toPlainText() + "you already have .")
        else:
            self.ui.view.setText(self.ui.view.toPlainText() + ".")

    def equal(self):

        if self.placeholder == "/":
            self.num2 = float(self.ui.view.toPlainText())
            if self.num2 == 0:
                self.ui.view.setText("Divided by zero")
            else:
                self.ui.view.setText(str(self.num1 / self.num2))

        if self.placeholder == "x":
            self.num2 = float(self.ui.view.toPlainText())
            self.ui.view.setText(str(self.num1 * self.num2))
        
        if self.placeholder == "-":
            self.num2 = float(self.ui.view.toPlainText())
            self.ui.view.setText(str(self.num1 - self.num2))

        if self.placeholder == "+":
            self.num2 = float(self.ui.view.toPlainText())
            self.ui.view.setText(str(self.num1 + self.num2))


calc = QApplication([])
window = Calculator()
calc.exec()