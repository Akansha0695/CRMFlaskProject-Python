from flask import Flask,render_template
import Database as db
from flask import request,url_for,redirect

app = Flask(__name__)



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')

@app.route("/contactus")
def contactus():
    return render_template('contactus.html')

@app.route("/custlist")
def custlist():
    customerlist = db.getall()
    return render_template("customerlist.html",customerlist=customerlist)


@app.route("/addCustomer",methods=['GET','POST'])    
def addCustomer():
    if request.method=='GET':
        return render_template("CustDetail.html")
    elif request.method=='POST':
        CustName = request.form['CustName']
        CustContact = request.form['CustContact']
        CustLocation = request.form['CustLocation']
        CustIncome = request.form['CustIncome']
        CustJobType = request.form['CustJobType']
        remarkCust = request.form['remarkCust']  
        db.insert(CustName,CustContact,CustLocation,CustIncome,CustJobType,remarkCust)
        return redirect(url_for('custlist'))

@app.route("/delcustomer/<int:id>",methods=['POST','GET'])
def delcustomer(id):
    if request.method=='GET':
        Customer = db.getcustomerbyid(id)
        return render_template('confirm.html',Customer=Customer)
    elif request.method=='POST':
        db.delete(id)
        return redirect(url_for('custlist'))


@app.route("/UpdateCustDetail/<int:id>",methods=['POST','GET'])
def UpdateCustDetail(id):
    if request.method=='GET':
        Customer = db.getcustomerbyid(id)
        return render_template('UpdateCustDetail.html',Customer=Customer)
    elif request.method=='POST':
        CustId = request.form['CustId']
        CustName = request.form['CustName']
        CustContact = request.form['CustContact']
        CustLocation = request.form['CustLocation']
        CustIncome = request.form['CustIncome']
        CustJobType = request.form['CustJobType']    
        remarkCust = request.form['remarkCust']  
        db.update(CustId,CustName,CustContact,CustLocation,CustIncome,CustJobType,remarkCust)
        return redirect(url_for('custlist'))


if __name__=='__main__':
    app.run(debug=True)
