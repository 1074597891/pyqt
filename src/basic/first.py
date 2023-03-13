import sys
import PyQt5.QtWidgets

app = PyQt5.QtWidgets.QApplication(sys.argv)
w = PyQt5.QtWidgets.QWidget()
w.resize(300, 150)
w.move(300, 300)

w.setWindowTitle("first project ")
w.show()
sys.exit(app.exec_())
