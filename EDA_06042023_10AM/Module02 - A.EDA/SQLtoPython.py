# MySQL Database connection


pip install pymysql # after pip install , restart the kernel execute below commands
import pandas as pd
from sqlalchemy import create_engine
import pymysql

data = pd.read_csv(r"C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\EDA_06042023_10AM\DataSets\education.csv")

# Creating engine which connect to MySQL
user = 'root' # user name
pw = 'Seemscrazy1994#' # password
db = 'education_db' # database

# creating engine to connect database
#conn = pymysql.connect(db='education_db', user='root', passwd='Seemscrazy1994#', host='localhost', port=3307)
#conn = pymysql.connect(
    #host = '127.0.0.1',
    #port = 3306,
    #user = 'root',
    #passwd = 'Seemscrazy1994#',
    #db = 'education_db'
#)
engine = create_engine(f"mysql+pymysql://{user}:{pw}@localhost/{db}")

# dumping data into database 
data.to_sql('education', con = engine, if_exists = 'replace', chunksize = 500, index = False)

# loading data from database
sql = 'select * from education'

edu = pd.read_sql_query(sql, con = engine)

print(edu)

//data



