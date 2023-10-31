import mysql.connector
from datetime import datetime
import pandas as pd


class DataBase:
    def __init__(self):
        self.connection_string = {
    'host': 'localhost',
    'user': 'root',
    'password': '0711',
    'database': 'faceattendace'
}
       # self.date=str(datetime.date(datetime.now())).replace("-", "_")
        
    def execute_non_query(self,query):
        try:
            db = mysql.connector.connect(**self.connection_string)
            cursor = db.cursor()
            cursor.execute(query)
            db.commit()
            print("successful")
            db.close()
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return
        
        
    def create_collumn(self,column_name):
        query = f"ALTER TABLE diem_danh ADD COLUMN  `{column_name}` NVARCHAR(50)"
        print(query)
        self.execute_non_query(query)
    
    
    def execute_query(self,query):
        try:
            db = mysql.connector.connect(**self.connection_string)
            cursor = db.cursor()
            cursor.execute(query)
            record = cursor.fetchall()
            print(record)
        except mysql.connector.errors as error:
            print("error", error)
            return
        finally:
            if db.is_connected():
                db.close()
                cursor.close()
                return record
       
        
    def get_number_of_cloumns(self):
        query= "SELECT count(column_name) FROM INFORMATION_SCHEMA.COLUMNS WHERE  TABLE_NAME='thong_tin_sv' or table_name='Diem_danh';"
       # print(query)
        return self.execute_query(query)[0][0]
    def get_number_of_rows(self):
        query= "SELECT count(MSSV) FROM thong_tin_sv"
       # print(query)
        return self.execute_query(query)[0][0]
    def get_columns_name(self):
        columns_name = []
        result = self.execute_query("DESCRIBE thong_tin_sv")
        result2 = self.execute_query("DESCRIBE diem_danh")
        for row in result:
            columns_name.append(row[0])
        for row in result2:
            columns_name.append(row[0])
        return columns_name
    
    
    def attendance(self,regiter_IDs,date):
        query=""
        for id in regiter_IDs:
            query=f'''UPDATE `faceattendace`.`diem_danh` SET `{date}` = 'Đủ' WHERE (`MSSV` = '{id}');
            '''
            self.execute_non_query(query)
            
   
        
    def make_up_attendance(self,regiter_IDs,date,type=None):
        if type==None:
            type='Đủ'
        query= f"UPDATE diem_danh SET `{date}` = N'{type}' WHERE mssv={regiter_IDs};"
        self.execute_non_query(query)
        
    def write_excel(self):
        db = mysql.connector.connect(**self.connection_string)
        columns_name=self.get_columns_name()
        query_data = "select * from thong_tin_sv,diem_danh where thong_tin_sv.mssv=diem_danh.mssv"
        df = pd.read_sql(query_data, con=db)
        exel_file='D:\FaceAttendace\data.xlsx'
        db.close()
        df.to_excel(exel_file)
        print(df)
        
                


