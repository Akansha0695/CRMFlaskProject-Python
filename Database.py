import pymysql as pm
con = pm.connect(host='localhost',port=3306,user='root',password='',database='CRM')

print("connected")
cur = con.cursor()

def createtable():
    sqlQuery = '''create table if not exists Customer(
                  CustId int primary key AUTO_INCREMENT,
                  CustName varchar(100) not null,
                  CustContact varchar(10),
                  CustLocation varchar(200),
                  CustIncome int(15),
                  CustJobType varchar(200),
                  remarkCust varchar(150))
               '''
    i = cur.execute(sqlQuery)
    print(i,'rows affected')
    print("Table is Created")

def insert(CustName,CustContact,CustLocation,CustIncome,CustJobType,remarkCust):
    sqlQuery = f"insert into Customer(CustName,CustContact,CustLocation,CustIncome,CustJobType,remarkCust) values ('{CustName}',{CustContact},'{CustLocation}','{CustIncome}','{CustJobType}','{remarkCust}')"
    i = cur.execute(sqlQuery)
    print(i,'rows affected')
    con.commit()

    
def update(CustId,CustName,CustContact,CustLocation,CustIncome,CustJobType,remarkCust):
    sqlQuery = f"update Customer set CustName='{CustName}',CustContact='{CustContact}',CustLocation='{CustLocation}',CustIncome='{CustIncome}',CustJobType='{CustJobType}',remarkCust='{remarkCust}' where CustId={CustId}"
    i = cur.execute(sqlQuery)
    print(i,'rows affected')
    con.commit()

def delete(CustId):
    sqlQuery = f"delete from Customer where CustId={CustId}"
    i = cur.execute(sqlQuery)
    print(i,'rows affected')
    con.commit()

def getall():
      sqlQuery = "select * From Customer"
      i = cur.execute(sqlQuery)
      print(i,'rows affected')
      rows = cur.fetchall()
      return rows

def getcustomerbyid(CustId):
      sqlQuery = f"select * From Customer where CustId={CustId}"
      i = cur.execute(sqlQuery)
      print(i,'rows affected')
      row = cur.fetchone()
      return row


def closeDB():
    con.close()

createtable()
