import pymysql
from .hospitalModel import HospitalModel

connection = pymysql.connect(host = 'l3855uft9zao23e2.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',user = 'pwpx9lp53pp7oobn',port = 3306,password = 'q4f6xa3l2ter9vvk',database = 'hrnvjd7k86z6nj96')


class RecordModel:
    def __init__(self):
        '''hosp_inst = HospitalModel(hospital_name)
        self.table_data = hosp_inst.create_table_data(hospital_name)'''
        self.table_header = "APRI,FIB4,GENDER,HBV,ALT,AST"

    def create_rec_table(self):
        query = "CREATE TABLE IF NOT EXISTS patients_record (id INTEGER PRIMARY KEY)"
        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                return('Patient record table created')
            except:
                return('cannot create table')
        connection.close()

    def format_header(self):

        header = self.table_header
        header = header.split(',')
        return header

    def create_col(self):
        header = self.format_header()
        with connection.cursor() as cursor:
            for item in header:
                item = item.replace(" ","_")
                query=f"ALTER TABLE patients_record ADD COLUMN {item} VARCHAR(20)"
                try:
                    cursor.execute(query)
                except:
                    return('cannot create column')

    def loadCSV(self,path):
        self.create_rec_table()
        self.create_col()
        path = path
        cursor = connection.cursor()
        query = f'''LOAD DATA INFILE {repr(path)} INTO TABLE patients_record COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY "\n" '''
        print(query)
        cursor.execute(query)
        connection.commit()