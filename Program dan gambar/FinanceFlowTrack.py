import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pymysql.cursors
import locale

db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="finance_flow"
)


class Ui_MainWindow(QMainWindow):

    def windowPengeluaran(self):
        self.pengeluaran = QtWidgets.QMainWindow()
        self.ui = Ui_Pengeluaran()
        self.ui.setupUi(self.pengeluaran)
        self.pengeluaran.show()

    def windowPemasukkan(self):
        self.Pemasukkan = QtWidgets.QMainWindow()
        self.ui = Ui_Pemasukkan()
        self.ui.setupUi(self.Pemasukkan)
        self.Pemasukkan.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindows")
        MainWindow.setWindowIcon(QIcon('logo.png'))
        MainWindow.setEnabled(True)
        MainWindow.resize(1080, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1080, 720))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setColumnCount(4)
        self.header_table = self.tableView.horizontalHeader()
        self.header_table.setSectionResizeMode(0, QHeaderView.Stretch)
        self.header_table.setSectionResizeMode(1, QHeaderView.Stretch)
        self.header_table.setSectionResizeMode(2, QHeaderView.Stretch)
        self.header_table.setSectionResizeMode(3, QHeaderView.Stretch)
        self.tableView.setHorizontalHeaderLabels(
            ['Keterangan Transaksi', 'Keterangan Uang', 'Terakhir Diperbarui', 'Aksi'])
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setGeometry(QtCore.QRect(20, 180, 1041, 341))
        self.tableView.setMaximumSize(QtCore.QSize(1080, 720))
        self.tableView.setMouseTracking(True)
        self.tableView.setObjectName("tableView")

        self.tabeltotalkeluar = QtWidgets.QTableWidget(self.centralwidget)
        self.tabeltotalkeluar.setColumnCount(1)
        self.header_table = self.tabeltotalkeluar.horizontalHeader()
        self.header_table.setSectionResizeMode(0, QHeaderView.Stretch)
        self.tabeltotalkeluar.setHorizontalHeaderLabels(['Total Pengeluaran'])
        self.tabeltotalkeluar.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabeltotalkeluar.setGeometry(QtCore.QRect(300, 580, 261, 75))
        self.tabeltotalkeluar.setMinimumSize(QtCore.QSize(261, 75))
        self.tabeltotalkeluar.setMaximumSize(QtCore.QSize(261, 75))
        self.tabeltotalkeluar.setMouseTracking(True)
        self.tabeltotalkeluar.setObjectName("tabeltotalkeluar")

        self.tabeltotalmasuk = QtWidgets.QTableWidget(self.centralwidget)
        self.tabeltotalmasuk.setColumnCount(1)
        self.header_table = self.tabeltotalmasuk.horizontalHeader()
        self.header_table.setSectionResizeMode(0, QHeaderView.Stretch)
        self.tabeltotalmasuk.setHorizontalHeaderLabels(['Total Pemasukkan'])
        self.tabeltotalmasuk.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabeltotalmasuk.setGeometry(QtCore.QRect(20, 580, 261, 75))
        self.tabeltotalmasuk.setMinimumSize(QtCore.QSize(261, 75))
        self.tabeltotalmasuk.setMaximumSize(QtCore.QSize(261, 75))
        self.tabeltotalmasuk.setMouseTracking(True)
        self.tabeltotalmasuk.setObjectName("tabeltotalkeluar")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 180, 1031, 341))
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1029, 339))
        self.scrollAreaWidgetContents.setMouseTracking(True)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.Btn_keluar = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.windowPengeluaran())
        self.Btn_keluar.setGeometry(QtCore.QRect(950, 630, 111, 51))
        self.Btn_keluar.setObjectName("Btn_keluar")

        self.Btn_masuk = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.windowPemasukkan())
        self.Btn_masuk.setGeometry(QtCore.QRect(950, 550, 111, 51))
        self.Btn_masuk.setObjectName("Btn_masuk")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 45, 271, 91))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 90, 90))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.gambar = QtGui.QPixmap("logo2.png")
        self.label2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label2.setPixmap(self.gambar)
        self.verticalLayout.addWidget(self.label2)
        self.verticalLayout.addLayout(self.verticalLayout)
        self.verticalLayout.setGeometry(QtCore.QRect(20, 20, 90, 90))
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(20, 20, 90, 90)
        self.verticalLayout.setObjectName("verticalLayout")

        self.tabeltotalfinance = QtWidgets.QTableWidget(self.centralwidget)
        self.tabeltotalfinance.setColumnCount(1)
        self.header_table = self.tabeltotalfinance.horizontalHeader()
        self.header_table.setSectionResizeMode(0, QHeaderView.Stretch)
        self.tabeltotalfinance.setHorizontalHeaderLabels(['Total Uang yang dimiliki'])
        self.tabeltotalfinance.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabeltotalfinance.setGeometry(QtCore.QRect(580, 580, 261, 75))
        self.tabeltotalfinance.setMinimumSize(QtCore.QSize(261, 75))
        self.tabeltotalfinance.setMaximumSize(QtCore.QSize(261, 75))
        self.tabeltotalfinance.setMouseTracking(True)
        self.tabeltotalfinance.setObjectName("tabeltotalfinance")

        self.show_semua_transaksi()
        self.total_uangMasuk()
        self.total_uangKeluar()
        self.total_uang()
        self.tabeltotalmasuk.raise_()
        self.tabeltotalkeluar.raise_()
        self.tabeltotalfinance.raise_()
        self.scrollArea.raise_()
        self.tableView.raise_()
        self.Btn_keluar.raise_()
        self.Btn_masuk.raise_()
        self.label.raise_()
        self.verticalLayoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def total_uangmasuk(self, cursor, data):
        self.tabeltotalmasuk.setRowCount(len(self.data))
        uangmasuk = QtWidgets.QTableWidgetItem(str(self.data[0]))
        uangmasuk.setTextAlignment(QtCore.Qt.AlignCenter)
        if self.cursor.rowcount == 0:
            msgBox = QMessageBox()
            msgBox.setText('Tidak ada data transaksi ditemukan!')
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle("Finance Flow Tracker")
            msgBox.show()
        else:
            for index, data in enumerate(self.data):
                self.tabeltotalmasuk.setItem(index, 0, uangmasuk)

    def total_uangkeluar(self, cursor, data):
        self.tabeltotalkeluar.setRowCount(len(self.data))
        uangkeluar = QtWidgets.QTableWidgetItem(str(self.data[0]))
        uangkeluar.setTextAlignment(QtCore.Qt.AlignCenter)
        if self.cursor.rowcount == 0:
            msgBox = QMessageBox()
            msgBox.setText('Tidak ada data transaksi ditemukan!')
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle("Finance Flow Tracker")
            msgBox.show()
        else:
            for index, data in enumerate(self.data):
                self.tabeltotalkeluar.setItem(index, 0, uangkeluar)

    def totaluang(self, cursor, data):
        self.tabeltotalfinance.setRowCount(len(self.data))
        uangtotal = QtWidgets.QTableWidgetItem(str(self.data[0]))
        uangtotal.setTextAlignment(QtCore.Qt.AlignCenter)
        if self.cursor.rowcount == 0:
            msgBox = QMessageBox()
            msgBox.setText('Tidak ada data transaksi ditemukan!')
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle("Finance Flow Tracker")
            msgBox.show()
        else:
            for index, data in enumerate(self.data):
                self.tabeltotalfinance.setItem(index, 0, uangtotal)

    def show_transaksi(self, cursor, results):
        # Looping data
        self.tableView.setRowCount(len(self.results))
        # Looping data
        if self.cursor.rowcount == 0:
            msgBox = QMessageBox(self)
            msgBox.setText('Tidak ada data transaksi ditemukan!')
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle("Finance Flow Tracker")
            msgBox.show()
        else:
            for index, data in enumerate(self.results):
                tabeluang = QtWidgets.QTableWidgetItem(str(data[2]))
                tabeluang.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableView.setRowHeight(index, 50)
                # Tombol Hapus
                self.btn_hapus = QPushButton('Hapus')
                self.btn_hapus.clicked.connect(lambda checked, i=data[0]: self.hapus_transaksi(i))
                self.btn_hapus.setFixedHeight(30)
                # Layout Tombol
                self.btn_layout = QHBoxLayout()
                self.btn_layout.addWidget(self.btn_hapus)
                # Layout tombol menjadi widget
                self.btn_widget = QWidget()
                self.btn_widget.setLayout(self.btn_layout)
                # Menampilkan Baris
                self.tableView.setItem(index, 0, QTableWidgetItem(str(data[1])))
                self.tableView.setItem(index, 1, tabeluang)
                self.tableView.setItem(index, 2, QTableWidgetItem(data[3].strftime("%A,%d %B %Y %X")))
                self.tableView.setCellWidget(index, 3, self.btn_widget)

    # Tampilkan semua data transaksi
    def show_semua_transaksi(self):
        self.cursor = db.cursor()
        self.sql = "SELECT * FROM transaksi ORDER BY last_update DESC"
        self.cursor.execute(self.sql)
        self.results = self.cursor.fetchall()
        self.show_transaksi(self.cursor, self.results)

    def total_uangMasuk(self):
        self.cursor = db.cursor()
        self.sql = "SELECT SUM(jumlah_masuk) AS total_pemasukkan FROM transaksi_masuk;"
        self.cursor.execute(self.sql)
        self.data = self.cursor.fetchone()
        self.total_uangmasuk(self.cursor, self.data)

    def total_uangKeluar(self):
        self.cursor = db.cursor()
        self.sql = "SELECT SUM(jumlah_keluar) AS total_pengeluaran FROM transaksi_keluar;"
        self.cursor.execute(self.sql)
        self.data = self.cursor.fetchone()
        self.total_uangkeluar(self.cursor, self.data)

    def total_uang(self):
        self.cursor = db.cursor()
        self.sql = "SELECT SUM(total_uang) AS total FROM transaksi;"
        self.cursor.execute(self.sql)
        self.data = self.cursor.fetchone()
        self.totaluang(self.cursor, self.data)

    # Hapus Data Transaksi
    def hapus_transaksi(self, id_transaksi):
        self.cursor = db.cursor()
        self.sql = "SELECT * FROM transaksi WHERE id_transaksi=%s"
        self.val = (id_transaksi,)
        self.cursor.execute(self.sql, self.val)
        self.data = self.cursor.fetchone()
        self.msgBox = QMessageBox.question(self, 'Konfirmasi Penghapusan Transaksi',
                                           f"Apakah anda yakin ingin menghapus semua data Transaksi '{self.data[1]}' ?",
                                           QMessageBox.Yes | QMessageBox.No)
        if (self.msgBox == QMessageBox.Yes):
            self.sql = "DELETE FROM transaksi WHERE id_transaksi=%s"
            self.val = (id_transaksi,)
            self.cursor.execute(self.sql, self.val)
            db.commit()
            self.sukses = QMessageBox()
            self.sukses.setWindowTitle('Berhasil!')
            self.sukses.setText('Data berhasil dihapus!')
            self.sukses.setIcon(QMessageBox.Information)
            self.sukses.show()
            self.show_semua_transaksi()
            self.total_uangMasuk()
            self.total_uangKeluar()
            self.total_uang()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Finance Flow Tracker"))
        self.Btn_keluar.setText(_translate("MainWindow", "Pengeluaran"))
        self.Btn_masuk.setText(_translate("MainWindow", "Pemasukkan"))
        self.label.setText(_translate("MainWindow",
                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'Merriweather\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                      "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; color:#1ad669;\">Finance Flow</span></p></body></html>"))


class Ui_Pemasukkan(QMainWindow):
    def setupUi(self, Pemasukkan):
        Pemasukkan.setObjectName("Pemasukkan")
        Pemasukkan.setWindowIcon(QIcon('logo.png'))
        Pemasukkan.resize(655, 416)
        Pemasukkan.setMinimumSize(QtCore.QSize(655, 416))
        Pemasukkan.setMaximumSize(QtCore.QSize(655, 416))
        self.centralwidget = QtWidgets.QWidget(Pemasukkan)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 18, 191, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.submit_form())
        self.pushButton.setGeometry(QtCore.QRect(510, 340, 111, 41))
        self.pushButton.setObjectName("pushButton")

        self.input_pemasukkan = QtWidgets.QLineEdit(self.centralwidget)
        self.input_pemasukkan.setGeometry(QtCore.QRect(200, 100, 421, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_pemasukkan.setFont(font)
        self.input_pemasukkan.setObjectName("lineEdit_3")

        self.input_uang_masuk = QtWidgets.QLineEdit(self.centralwidget)
        self.input_uang_masuk.setGeometry(QtCore.QRect(200, 180, 421, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_uang_masuk.setFont(font)
        self.input_uang_masuk.setObjectName("lineEdit_2")

        self.input_keterangan = QtWidgets.QLineEdit(self.centralwidget)
        self.input_keterangan.setGeometry(QtCore.QRect(200, 260, 421, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_keterangan.setFont(font)
        self.input_keterangan.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 181, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 180, 181, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 260, 181, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 40, 40))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.gambar = QtGui.QPixmap("logo45x45.png")
        self.label2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label2.setPixmap(self.gambar)
        self.verticalLayout.addWidget(self.label2)
        self.verticalLayout.addLayout(self.verticalLayout)
        self.verticalLayout.setGeometry(QtCore.QRect(10, 10, 40, 40))
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(10, 10, 40, 40)
        self.verticalLayout.setObjectName("verticalLayout")

        Pemasukkan.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Pemasukkan)
        self.statusbar.setObjectName("statusbar")
        Pemasukkan.setStatusBar(self.statusbar)

        self.retranslateUi(Pemasukkan)
        QtCore.QMetaObject.connectSlotsByName(Pemasukkan)

    def submit_form(self):
        asal_pemasukkan = str(self.input_pemasukkan.text())
        jumlah_uang_masuk = str(self.input_uang_masuk.text())
        keterangan_uang_masuk = str(self.input_keterangan.text())

        if (not asal_pemasukkan or not jumlah_uang_masuk):
            self.error = QMessageBox()
            self.error.setWindowTitle("GAGAL | Finance Flow Tracker || Pemasukkan")
            self.error.setText('Pastikan asal pemasukan dan jumlah uang sudah terisi!')
            self.error.setIcon(QMessageBox.Warning)
            self.error.show()
        elif (int(jumlah_uang_masuk) <= 0):
            self.error = QMessageBox()
            self.error.setWindowTitle("GAGAL | Finance Flow Tracker || Pemasukkan")
            self.error.setText('Pastikan jumlah uang lebih dari nol!')
            self.error.setIcon(QMessageBox.Warning)
            self.error.show()
        else:
            val = (asal_pemasukkan, jumlah_uang_masuk, keterangan_uang_masuk)
            cursor = db.cursor()
            sql = "CALL transaksi_masuk (%s,%s,%s)"
            cursor.execute(sql, val)
            db.commit()
            self.sukses = QMessageBox()
            self.sukses.setWindowTitle("BERHASIL | Finance Flow Tracker || Pemasukkan")
            self.sukses.setText('Data transaksi berhasil ditambahkan!')
            self.sukses.setIcon(QMessageBox.Information)
            self.sukses.show()
            window.total_uangMasuk()
            window.show_semua_transaksi()
            window.total_uang()
            self.close()

    def retranslateUi(self, Pemasukkan):
        _translate = QtCore.QCoreApplication.translate
        Pemasukkan.setWindowTitle(_translate("Pemasukkan", "Finance Flow Tracker || Pemasukkan"))
        self.label.setText(_translate("Pemasukkan",
                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'Merriweather\'; font-size:8pt; font-weight:600; font-style:normal;\">\n"
                                      "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; color:#1ad669;\">Finance Flow</span></p></body></html>"))
        self.pushButton.setText(_translate("Pemasukkan", "Submit"))
        self.label_2.setText(_translate("Pemasukkan", "Asal Pemasukkan  : "))
        self.label_3.setText(_translate("Pemasukkan", "Jumlah Masuk       : "))
        self.label_4.setText(_translate("Pemasukkan", "Keterangan           : "))


class Ui_Pengeluaran(QMainWindow):
    def setupUi(self, Pengeluaran):
        Pengeluaran.setObjectName("Pengeluaran")
        Pengeluaran.setWindowIcon(QIcon('logo.png'))
        Pengeluaran.resize(655, 416)
        Pengeluaran.setMinimumSize(QtCore.QSize(655, 416))
        Pengeluaran.setMaximumSize(QtCore.QSize(655, 416))
        self.centralwidget = QtWidgets.QWidget(Pengeluaran)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 18, 191, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.submit_form())
        self.pushButton.setGeometry(QtCore.QRect(510, 340, 111, 41))
        self.pushButton.setObjectName("pushButton")

        self.input_pengeluaran = QtWidgets.QLineEdit(self.centralwidget)
        self.input_pengeluaran.setGeometry(QtCore.QRect(200, 100, 421, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_pengeluaran.setFont(font)
        self.input_pengeluaran.setObjectName("lineEdit_3")

        self.input_uang_keluar = QtWidgets.QLineEdit(self.centralwidget)
        self.input_uang_keluar.setGeometry(QtCore.QRect(200, 180, 421, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_uang_keluar.setFont(font)
        self.input_uang_keluar.setObjectName("lineEdit_2")

        self.input_keterangan = QtWidgets.QLineEdit(self.centralwidget)
        self.input_keterangan.setGeometry(QtCore.QRect(200, 260, 421, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_keterangan.setFont(font)
        self.input_keterangan.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 181, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 180, 181, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 260, 181, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 40, 40))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.gambar = QtGui.QPixmap("logo45x45.png")
        self.label2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label2.setPixmap(self.gambar)
        self.verticalLayout.addWidget(self.label2)
        self.verticalLayout.addLayout(self.verticalLayout)
        self.verticalLayout.setGeometry(QtCore.QRect(10, 10, 40, 40))
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(10, 10, 40, 40)
        self.verticalLayout.setObjectName("verticalLayout")
        Pengeluaran.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Pengeluaran)
        self.statusbar.setObjectName("statusbar")
        Pengeluaran.setStatusBar(self.statusbar)

        self.retranslateUi(Pengeluaran)
        QtCore.QMetaObject.connectSlotsByName(Pengeluaran)

    def submit_form(self):
        tujuan_pengeluaran = str(self.input_pengeluaran.text())
        jumlah_uang_keluar = str(self.input_uang_keluar.text())
        keterangan_uang_keluar = str(self.input_keterangan.text())

        if (not tujuan_pengeluaran or not jumlah_uang_keluar):
            self.error = QMessageBox()
            self.error.setWindowTitle("GAGAL | Finance Flow Tracker || Pengeluaran")
            self.error.setText('Pastikan tujuan pengeluaran dan jumlah uang sudah terisi!')
            self.error.setIcon(QMessageBox.Warning)
            self.error.show()
        elif (int(jumlah_uang_keluar) <= 0):
            self.error = QMessageBox()
            self.error.setWindowTitle("GAGAL | Finance Flow Tracker || Pemasukkan")
            self.error.setText('Pastikan jumlah uang lebih dari nol!')
            self.error.setIcon(QMessageBox.Warning)
            self.error.show()
        else:
            val = (tujuan_pengeluaran, jumlah_uang_keluar, keterangan_uang_keluar)
            cursor = db.cursor()
            sql = "CALL transaksi_keluar (%s,%s,%s)"
            cursor.execute(sql, val)
            db.commit()
            self.sukses = QMessageBox()
            self.sukses.setWindowTitle("BERHASIL | Finance Flow Tracker || Pengeluaran")
            self.sukses.setText('Data transaksi berhasil ditambahkan!')
            self.sukses.setIcon(QMessageBox.Information)
            self.sukses.show()
            window.total_uangKeluar()
            window.show_semua_transaksi()
            window.total_uang()
            self.close()

    def retranslateUi(self, Pengeluaran):
        _translate = QtCore.QCoreApplication.translate
        Pengeluaran.setWindowTitle(_translate("Pengeluaran", "Finance Flow Tracker || Pengeluaran"))
        self.label.setText(_translate("Pengeluaran",
                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'Merriweather\'; font-size:8pt; font-weight:600; font-style:normal;\">\n"
                                      "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; color:#1ad669;\">Finance Flow</span></p></body></html>"))
        self.pushButton.setText(_translate("Pengeluaran", "Submit"))
        self.label_2.setText(_translate("Pengeluaran", "Tujuan Pengeluaran : "))
        self.label_3.setText(_translate("Pengeluaran", "Jumlah Keluar        : "))
        self.label_4.setText(_translate("Pengeluaran", "Keterangan            : "))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    window = Ui_MainWindow()
    window.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())