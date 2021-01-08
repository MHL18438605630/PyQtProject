import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__=='__main__':
    app=QApplication(sys.argv)
    W=QWidget()
    W.resize(300,300)
    W.move(100,100)
    W.setWindowTitle("第一个基于PyQt5的桌面应用程序")
    W.show();

    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())


