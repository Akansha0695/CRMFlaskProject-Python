import Database as db
db.createtable()

menu =f'''
                        Welcome to Customer Relationship Management
        {'=='*40}
        1. Add Customer
        2. Update Customer
        3. Delete Customer
        4. Show All Customer
        5. Exit
        {'=='*40}
        Select Your Choice '''
choice = 0
while choice !=5:
    choice = int(input(menu))
    if choice ==1:
        CustName= input ("Enter Customer Name ")
        CustContact = int (input("Enter Customer Contacts "))
        CustLocation = input("Enter Customer Location ")
        CustIncome = int(input ('Enter Customer Income '))
        CustJobType = input("Enter Customer Job Type ")
        remarkCust = input("Input Lead Of The Day ")
        db.insert(CustId,CustName,CustContact,CustLocation,CustIncome,CustJobType,remarkCust)
        print("Customer Details Inserted in records.")

    elif choice==2:
        CustId= int(input("Enter Customer Id to update "))
        CustName= input ("Enter Customer Name ")
        CustContact = int (input("Enter Customer Contacts "))
        CustLocation = input("Enter Customer Location ")
        CustIncome = int(input ('Enter Customer Income '))
        CustJobType = input("Enter Customer Job Type ")
        remarkCust = input("Input Lead Of The Day ")
        db.update(CustId,CustName,CustContact,CustLocation,CustIncome,CustJobType,remarkCust)
        print("Customer Details updated into table")

    elif choice==3:
        CustId= int(input("Enter Customer Id to delete "))
        db.delete(CustId)
        print("Customer record deleted")

    elif choice==4:
        CustId = db.getall()
        if len(CustId)>0:
            print('==*=='*5,'Customer List','==*=='*5)
            for Customer in CustId:
                print('\t',*Customer)
                print('='*70)
        else:
            print('No Customer Found..!')
            
    elif choice==5:
        print('Thank You..!')

    else:
        print('Invalid Input, Please Try Again..!')
    
