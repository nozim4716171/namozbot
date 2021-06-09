from psycopg2 import connect
import  datetime
print(datetime.date.today())
DB_name = 'regions'
DB_user = 'postgres'
DB_pass = '2303'
DB_host = 'localhost'
DB_port = '5432'

try:
    con = connect(database = DB_name, user = DB_user, password =DB_pass, host =DB_host, port =DB_port)
    print('DB succesfully connected')
except:
    print('DB don\'t connected')
cur = con.cursor()
def get_regions():
    cur.execute('Select region_name , region_id from regions')
    return (cur.fetchall())
def get_region(region_id1):
    cur.execute('select region_id , region_name from regions where region_id ={}'.format(region_id1 ))
def get_time(region_id1 = 1, date1 = str(datetime.date.today())):
    print(type(region_id1), type(date1))
    cur.execute("""select "Tong" ,"Quyosh" , "peshin" ,"Asr" , "Shom" , "Xufton" 
    from public."Namaz" where region_id={} and date = '{}'""".format(region_id1 ,date1))
    return (cur.fetchone())
# a=get_time()
# print(a[1])