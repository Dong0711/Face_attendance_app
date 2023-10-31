
import cv2
from PyQt6 import QtCore, QtGui, QtWidgets
import database_layer 
import face_attendace
import os
import handle_app 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.data=database_layer.DataBase()
        self.handle_app=handle_app.Handle_app()
        self.day = QtCore.QDateTime.currentDateTime().toString("dd.MM.yyyy hh:mm:ss").replace(' ','_')
        #.toString("dd.MM.yyyy hh:mm:ss")
        print(self.day)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1311, 676)
        icon=QtGui.QIcon()
        icon.addFile('images/icon_app.png')
        MainWindow.setWindowIcon(icon)
        self.check_click_btn_diem_danh = False
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 961, 641))
        self.groupBox.setObjectName("groupBox")
        
        self.tw_danh_sach_sv = QtWidgets.QTableWidget(parent=self.groupBox)
        self.tw_danh_sach_sv.setGeometry(QtCore.QRect(10, 20, 941, 611))
        self.tw_danh_sach_sv.setObjectName("tw_danh_sach_sv")
        self.tw_danh_sach_sv=self.handle_app.load_data_to_table(self.tw_danh_sach_sv)

        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(980, 390, 321, 191))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txt_search = QtWidgets.QTextEdit(parent=self.groupBox_2)
        self.txt_search.setGeometry(QtCore.QRect(90, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.txt_search.setFont(font)
        self.txt_search.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor)
        )
        self.txt_search.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.txt_search.setLocale(
            QtCore.QLocale(
                QtCore.QLocale.Language.Vietnamese, QtCore.QLocale.Country.Vietnam
            )
        )
        self.txt_search.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.txt_search.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.txt_search.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored
        )
        self.txt_search.setObjectName("txt_search")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.groupBox_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 301, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rd_mssv = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rd_mssv.setFont(font)
        self.rd_mssv.setObjectName("rd_mssv")
        self.horizontalLayout.addWidget(self.rd_mssv)
        self.rd_ho = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rd_ho.setFont(font)
        self.rd_ho.setObjectName("rd_ho")
        self.horizontalLayout.addWidget(self.rd_ho)
        self.rd_ten = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rd_ten.setFont(font)
        self.rd_ten.setObjectName("rd_ten")
        self.horizontalLayout.addWidget(self.rd_ten)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.groupBox_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 130, 301, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rd_all_dd = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rd_all_dd.setFont(font)
        self.rd_all_dd.setObjectName("rd_all_dd")
        self.horizontalLayout_2.addWidget(self.rd_all_dd)
        self.rd_da_dd = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rd_da_dd.setFont(font)
        self.rd_da_dd.setObjectName("rd_da_dd")
        self.horizontalLayout_2.addWidget(self.rd_da_dd)
        self.rd_chua_dd = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rd_chua_dd.setFont(font)
        self.rd_chua_dd.setObjectName("rd_chua_dd")
        self.horizontalLayout_2.addWidget(self.rd_chua_dd)
        self.btn_xuat_file_excel = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_xuat_file_excel.setGeometry(QtCore.QRect(1080, 590, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_xuat_file_excel.setFont(font)
        self.btn_xuat_file_excel.setObjectName("btn_xuat_file_excel")
        
        self.lb_camera = QtWidgets.QLabel(parent=self.centralwidget)
        self.lb_camera.setGeometry(QtCore.QRect(990, 20, 311, 311))
        self.lb_camera.setStyleSheet("background-color:rgb(30, 130, 111);")
        self.lb_camera.setText("")
        self.lb_camera.setObjectName("lb_camera")

        self.lb_camera.setPixmap(
            QtGui.QPixmap(str(os.path.join(os.getcwd(), "images/icon_app.png")))
        )
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(990, 340, 311, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_diem_danh_bu = QtWidgets.QPushButton(
            parent=self.horizontalLayoutWidget_3
        )
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_diem_danh_bu.setFont(font)
        self.btn_diem_danh_bu.setObjectName("btn_diem_danh_bu")
        self.horizontalLayout_3.addWidget(self.btn_diem_danh_bu)
        self.btn_diem_danh = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_diem_danh.setFont(font)
        self.btn_diem_danh.setObjectName("btn_diem_danh")
        self.horizontalLayout_3.addWidget(self.btn_diem_danh)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
       
        self.timer = QtCore.QTimer(MainWindow)
        self.btn_diem_danh_bu.clicked.connect(self.Diem_danh_bu)
        self.btn_xuat_file_excel.clicked.connect(self.export_excel)
        
        # button click
        self.btn_diem_danh.clicked.connect(self.btn_diem_danh_click)
        self.txt_search.textChanged.connect(self.search)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Điểm danh sinh viên"))
        self.groupBox.setTitle(_translate("MainWindow", "Danh sách sinh viên"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Tìm kiếm"))
        self.label.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt;">Thông tin:</span></p></body></html>',
            )
        )
        self.txt_search.setAccessibleDescription(
            _translate("MainWindow", "Nhập vào thông tin cần tìm kiếm")
        )
        self.rd_mssv.setText(_translate("MainWindow", "MSSV"))
        self.rd_mssv.setChecked(True)
        self.rd_ho.setText(_translate("MainWindow", "Họ"))
        self.rd_ten.setText(_translate("MainWindow", "Tên"))
        self.rd_all_dd.setText(_translate("MainWindow", "Tất cả"))
        self.rd_all_dd.setChecked(True)
        self.rd_da_dd.setText(_translate("MainWindow", "Đã ĐD"))
        self.rd_chua_dd.setText(_translate("MainWindow", "Chưa ĐD"))
        self.btn_xuat_file_excel.setText(_translate("MainWindow", "Xuất file Excel"))
        self.btn_diem_danh_bu.setText(_translate("MainWindow", "Điểm danh bù"))
        self.btn_diem_danh.setText(_translate("MainWindow", "Bắt đầu điểm danh"))
    
    
    def btn_diem_danh_click(self):
        # row = self.tw_danh_sach_sv.currentRow()
        # column = self.tw_danh_sach_sv.currentColumn()
        self.check_click_btn_diem_danh = not self.check_click_btn_diem_danh
        if self.check_click_btn_diem_danh:
            self.data.create_collumn(self.day)
            self.video_caputer = cv2.VideoCapture(0)
            self.face = face_attendace.face_recognition()
            self.timer.timeout.connect(self.update_frame)
            self.timer.start(60)
            self.btn_diem_danh.setText(QtCore.QCoreApplication.translate("MainWindow", "Kết thúc điểm danh"))          
        else:
            self.data.attendance(self.face.registered_names,self.day)
            self.tw_danh_sach_sv.setRowCount(0)
            self.tw_danh_sach_sv=self.handle_app.load_data_to_table(self.tw_danh_sach_sv)
            self.close_evet(self.update_frame)
            self.lb_camera.setPixmap(
                QtGui.QPixmap(str(os.path.join(os.getcwd(), "images/icon_app.png")))
            )
            self.btn_diem_danh.setText(QtCore.QCoreApplication.translate("MainWindow", "Bắt đầu điểm danh"))
            

    def update_frame(self):
        ret, frame = self.video_caputer.read()       
        if ret:
            processed_frame = self.face.get_processed_frame(frame)
            self.display_image(processed_frame)

    def display_image(self, frame):
        q_format = QtGui.QImage.Format.Format_BGR888
        out_image = QtGui.QImage(
            frame, frame.shape[1], frame.shape[0], frame.strides[0], q_format
        )
        out_image = out_image.rgbSwapped()
        self.lb_camera.setPixmap(QtGui.QPixmap.fromImage(out_image))

    def close_evet(self, event):
        self.video_caputer.release()

    def ThoatQuay(self):
        self.close_evet(self.update_frame)

    def search(self):
    
        query = f"""SELECT * 
        FROM thong_tin_sv,diem_danh
        WHERE thong_tin_sv.mssv=diem_danh.mssv        
        """
        sub_query1 = (
            " AND thong_tin_sv.mssv like '%{}%' ".format(self.txt_search.toPlainText())
            if self.rd_mssv.isChecked()
            else " AND ho like '%{}%'".format(self.txt_search.toPlainText())
            if self.rd_ho.isChecked()
            else " AND ten like '%{}%'".format(self.txt_search.toPlainText())
        )

        sub_query2 = (
            ""
            if self.rd_all_dd.isChecked()
            else " AND {} IS NULL".format(self.day)
            if self.rd_chua_dd
            else " AND {} IS NOT NULL AND {} <> 'Đủ'".format(self.day,self.day)
        )
        print("{}{}{}".format(query, sub_query1, sub_query2))
        self.tw_danh_sach_sv.setRowCount(0)
        self.tw_danh_sach_sv=self.handle_app.load_data_to_table(self.tw_danh_sach_sv,"{}{}{}".format(query, sub_query1, sub_query2))
        # if self.rd_all_dd.isChecked:
    def export_excel(self):
        self.data.write_excel()
    def Diem_danh_bu(self):
        current_row = self.tw_danh_sach_sv.currentRow()
        current_column = self.tw_danh_sach_sv.currentColumn()
        # print(current_row.index)
        tw_item = QtWidgets.QTableWidgetItem("Trễ")
        date=self.tw_danh_sach_sv.horizontalHeaderItem(current_column).text()
        value=self.tw_danh_sach_sv.item(current_row,0).text()
        self.data.make_up_attendance(value,date,tw_item.text())
        self.tw_danh_sach_sv.setItem(current_row, current_column, tw_item)



def RunApp():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
  