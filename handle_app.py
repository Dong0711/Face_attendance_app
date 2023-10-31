import database_layer
import cv2
from PyQt6 import QtCore, QtGui, QtWidgets
# import face_attendace
import os
# from app import Ui_MainWindow
class Handle_app:
    def __init__(self) -> None:
        self.data=database_layer.DataBase()
        self.load_data_to_table
        
        
    def load_data_to_table(self,table,query=None):
        number_of_columns=self.data.get_number_of_cloumns()
        number_of_rows=self.data.get_number_of_rows()
        columns_name=self.data.get_columns_name()
        table.setColumnCount(number_of_columns)
        table.setRowCount(number_of_rows)
        table.setHorizontalHeaderLabels(columns_name)
        if query:
            query_data=query
        else:
            query_data = "select * from thong_tin_sv,diem_danh where thong_tin_sv.mssv=diem_danh.mssv"
        
        data_table=self.data.execute_query(query_data)
        table_row=0
        
        for row in data_table:
            cell_index=0
            for cell in row:
                table_item=QtWidgets.QTableWidgetItem(str(cell))
                if cell_index<5:
                   table_item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled) 
                table.setItem(table_row,cell_index,table_item)
                cell_index+=1
            table_row+=1
        return table
        
  
def RunApp():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Handle_app()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())