from PyQt5 import QtCore, QtGui,uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys,os,csv

"""
Hesap Makinesi by Eren
======================

mükemmel bir hesap makinesi.
----------------------------

![ekran görüntüsü ubuntu](https://user-images.githubusercontent.com/75967441/149655076-a4c6302b-ba6c-4365-a6a1-764fda2d2a35.png "Hesap Makinesi by Eren (Ubuntu/GNOME3)") ![ekran görüntüsü windows](https://user-images.githubusercontent.com/75967441/149655847-7183f87a-fbed-4bc4-8833-9054cf3c838a.png "Hesap Makinesi by Eren (Windows)")

bazılarının inanmak istemeyeceğini bilsem de bunu ben yaptım;
internetten vs. çalmadan.

yalan söylediğimi iddia edecek olursanız, beni çıldırtmayın,
iddialıysanız internetten aynısını bulmayı deneyebilirsiniz.

önemli not
----------
şimdi bana kesin gelip bu çalışmıyor diyeceksiniz;
bi zahmet PyQt5'i kurun, beni delirtmeyin: ```pip install PyQt5```

eğer pip3 ile indirmede sıkıntı yaşıyorsanız, [şunu](https://sourceforge.net/projects/pyqt/files/PyQt5/ "PyQt5'in sourceforge reposu") da deneyebilirsiniz (ben denemedim)

eğer o da karışık gelirse benim windows için derlediğim [binaryleri](https://github.com/insanolanbiri/hesap-makinesi-PyQt5/releases/latest "binaryler") de kullanabilirsiniz.
"""

class App(QMainWindow):
    def __init__(self):
        super(App,self).__init__()

        self.win=uic.loadUi(os.path.join(os.getcwd(),"hesap.ui"),self)
        self.setFixedSize(self.size())
        self.setWindowIcon(QtGui.QIcon('hesap.ico'))
        self.win.show()
        self.win.cikti.setFocus()
        self.cikti.returnPressed.connect(self.f_esittir)

        # okura not: lambda'nın ne olduğu ile ilgili en ufak bir fikrim yok, ilk defa duyuyorum
        # sadece stack overflow'da bu sorunu öyle çözmüşler, ben de uygulayayım dedim:
        # https://stackoverflow.com/questions/40982518/argument-1-has-unexpected-type-nonetype

        self.win.btn1.clicked.connect(lambda: self.f_ekle("1"))
        self.win.btn2.clicked.connect(lambda: self.f_ekle("2"))
        self.win.btn3.clicked.connect(lambda: self.f_ekle("3"))
        self.win.btn4.clicked.connect(lambda: self.f_ekle("4"))
        self.win.btn5.clicked.connect(lambda: self.f_ekle("5"))
        self.win.btn6.clicked.connect(lambda: self.f_ekle("6"))
        self.win.btn7.clicked.connect(lambda: self.f_ekle("7"))
        self.win.btn8.clicked.connect(lambda: self.f_ekle("8"))
        self.win.btn9.clicked.connect(lambda: self.f_ekle("9"))
        self.win.btn0.clicked.connect(lambda: self.f_ekle("0"))

        self.win.btn_toplama.clicked.connect(lambda: self.f_ekle("+"))
        self.win.btn_cikarma.clicked.connect(lambda: self.f_ekle("-"))
        self.win.btn_carpma.clicked.connect(lambda: self.f_ekle("*"))
        self.win.btn_bolme.clicked.connect(lambda: self.f_ekle("/"))
        self.win.btn_nokta.clicked.connect(lambda: self.f_ekle("."))
        self.win.btn_p_ac.clicked.connect(lambda: self.f_ekle("("))
        self.win.btn_p_kapa.clicked.connect(lambda: self.f_ekle(")"))
        self.win.btn_us.clicked.connect(lambda: self.f_ekle("**"))
        self.win.btn_karekok.clicked.connect(lambda: self.f_ekle("**(0.5)"))

        self.win.btn_ac.clicked.connect(lambda: self.f_ac())
        self.win.btn_geri.clicked.connect(lambda: self.f_geri())
        self.win.btn_esittir.clicked.connect(lambda: self.f_esittir())
        self.win.btn_asal.clicked.connect(lambda: self.f_asal())

    def f_ekle(self,ek): self.cikti.setText(f"{self.cikti.text()}{ek}")
    def f_ac(self): self.cikti.setText("")
    def f_geri(self): self.cikti.setText(self.cikti.text()[:-1])

    def f_asal(self):
        try:
            no=int(self.cikti.text())
            with open("./anonim-deneme2022_ocak.csv") as file:
                reader=csv.reader(file)
                for row in reader:
                    if row[0]==self.cikti.text():
                        self.cikti.setText(row[6])
                        break 
        except: self.cikti.setText("bir şey oldu") 


    def f_esittir(self):
        try: self.cikti.setText(str(eval(self.cikti.text())))
        except: self.cikti.setText(f"{self.cikti.text()}: doğru düzgün gir")
    
if __name__=="__main__":
    app=QApplication(sys.argv)
    uygulama=App()
    sys.exit(app.exec_())