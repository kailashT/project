"""

create_query_for_month()
create_table(conn, create_table_sql)
add_customer_to_db(conn, cmd)
delete_customer_from_db(conn, cmd)

"""


import datetime
from calendar import Calendar
from project_code import loggerfile

dlog = loggerfile.setup_logger('pro','prolog.txt')



sql_Customer_table = """CREATE TABLE IF NOT EXISTS Customers (
                                ID              integer PRIMARY KEY autoincrement,
                                Name            text NOT NULL UNIQUE,
                                Address         text NOT NULL,
                                MoNumber        text NOT NULL UNIQUE,
                                MoNumber2       text NULL,
                                CONSTRAINT      uiocount UNIQUE (Name,Address,MoNumber)
                            );"""

# daily data table
def create_query_for_month():
    try :
        sql_month_table = "CREATE TABLE IF NOT EXISTS " + datetime.date.today().strftime("%B%Y") + \
                          "( ID     integer NOT NULL"
        year = datetime.date.today().strftime("%Y")
        month_no = datetime.date.today().strftime("%m")
        month = Calendar().itermonthdates(int(year), int(month_no))
        for day in month:
            if day.month == int(month_no):
                sql_month_table = sql_month_table + ", '" +(day.strftime("%y%m%d")) + "'"
                sql_month_table = sql_month_table + ("  text  NULL")
        sql_month_table = sql_month_table + ");"
        return sql_month_table
    except Exception as e:
        dlog.error(e)
        return False

# Customer table
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        ret = c.execute(create_table_sql)
        dlog.debug(ret)
        conn.commit()
        return True
    except Exception as e:
        dlog.error(e)
        return False

# INSERT INTO Customers (ID, Name, Address,MoNumber,MoNumber2) VALUES (2,"UV","Panjab","9822583254","9876549315");
def add_customer_to_db(conn, cmd):
    try:
        sql = ''' INSERT INTO Customers (Name,Address,MoNumber,MoNumber2) VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, cmd)
        conn.commit()
    except Exception as e:
        dlog.error(e)

def delete_customer_from_db(conn, cmd):
    try:
        sql = ''' DELETE FROM Customers WHERE Name=?  AND MoNumber=? '''
        cur = conn.cursor()
        cur.execute(sql, cmd)
        conn.commit()
        #TODO need to remove all data
    except Exception as e:
        dlog.error(e)
