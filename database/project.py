
import sqlite3
from project_code import database
from project_code import loggerfile
import datetime

dlog = loggerfile.setup_logger('pro','prolog.txt')






def add_data(conn):
    try :
        Chor_10 = [["Dolly", "Pune", '9225922747', '1235469871']
            , ["Dvid","london","9876542311","9875642312"]
            , ["Luna", "NY", "9876542312", "9875642311"]
            , ["Jocky", "Bijing", "9876542313", "9875642313"]
            , ["Poo", "WD", "9876542314", "9875642314"]
            , ["Iron", "Bolly", "9876542315", "9875642315"]
            , ["Suse", "Tolly", "9876542316", "9875642316"]
            , ["Linu", "Russia", "9876542317", "9875642317"]
            , ["Tom", "Africa", "9876542318", "9875642318"]
            , ["Jack", "Paris", "9876542319", "9875642319"]]

        for x in Chor_10:
            dlog.debug(x)
            database.add_customer_to_db(conn, x)

    except Exception as e:
        dlog.error(e)






def add_daily_data(conn,data):
    """

    :param conn:
    :param data:
    :return:
    get ID from name
    insert or update Id
    ''' select id from Controller where ControllerName=? COLLATE NOCASE'''
    ''' INSERT OR REPLACE INTO DeviceActivateCard(ControllerID,CreatedDT,CardNo,CSN,Name,Expiry,Commandtype) VALUES(?,?,?,?,?,?,?) '''
    """
    try:
        dlog.debug(data)

        sql = ''' select ID from Customers where Name=?'''
        cur = conn.cursor()
        cur.execute(sql, (data[0],))
        id = cur.fetchone()
        id = id[0]
        dlog.debug(id)
        del cur
        sql = ''' INSERT OR REPLACE INTO ''' + datetime.date.today().strftime("%B%Y") + ''' (ID, "'''+ str(datetime.date.today().strftime("%y%m%d")) + '''" ) VALUES(?,?) '''
        dlog.debug(sql)
        cur = conn.cursor()
        cur.execute(sql, (id,data[2]) )

        conn.commit()

    except Exception as e:
        dlog.error(e)



db_file  = "loha.db"
conn = sqlite3.connect(db_file)
if conn is not None:
    #database.create_table(conn,database.sql_Customer_table)
    #month_data_table = database.create_query_for_month()
    #database.create_table(conn,month_data_table)
    name = ["Suse",14,15,16]
    #add_data(conn)
    add_daily_data(conn, name)

conn.close()


# add_data(conn)
#    database.delete_customer_from_db(conn,["Linu", "9876542317"])
