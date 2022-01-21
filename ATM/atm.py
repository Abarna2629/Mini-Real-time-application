import os
import datetime
amount={2000:0,500:0,200:0,100:0}
users=[{'name':'abarna','pass':'123','balance':20000,'bank':'iob','dailylimit':10000,"extra_charge":20},
        {'name':'dudu','pass':'345','balance':20000,'bank':'sbi','dailylimit':20000,"extra_charge":10},
        {'name':'dubu','pass':'567','balance':40000,'bank':'sbi','dailylimit':10000,"extra_charge":10}]
atmdetail={'bank':'sbi','balance':0}
transaction=[]
balance=0
# Withdraw,show balance,transaction,pinchange,exit
def customer(name,a,atmdetail):  
    while(True):
        print("1.withdraw\n2.show balance\n3.Transaction\n4.Pinchange\n5.Direct deposit\n6.Account Transfer\n7.Exit")  
        n=int(input("Enter your choice: "))
        if(n==1):
            amt=int(input("Enter amount to withdraw: "))
            balance=a['balance']
            if(amt<atmdetail['balance']):
                if(balance>=amt):
                    if(amt%100==0):
                        if(amt<a['dailylimit']):
                            a['dailylimit']-=amt
                            val=0
                            for i in amount:
                                no=int(input("Enter no of "+str(i)+" notes : "))
                                val+=no*i
                                if(no<=amount[i]):
                                    amount[i]-=no
                                else:
                                    print("Insufficient"+str(i)+"notes")
                            if(amt==val):
                                if(atmdetail['bank']==a['bank']):
                                    balance-=amt
                                    a['balance']=balance
                                    ref=amt,datetime.datetime.now()
                                    transaction.append([ref])
                                    print("Amount withdrawn successfully")
                                    
                                else:
                                    balance-=amt+a['extra_charge']
                                    a['balance']=balance
                                    ref=amt,datetime.datetime.now(),a['extra_charge']
                                    transaction.append([ref])
                                    print("Amount withdrwan successfully")
                                    
                            elif(val<amt or val>amt):
                                print("Amount does not match")
                        else:
                            print("Amount exceeded")
                    else:
                        print("enter Amount in 100's")
                else:
                    print("insufficient balance in account")
            else:
                print("Insufficient balance in atm")
        elif(n==2):
            for i in users:
                if(name==i['name']):
                    print(i['balance'])           
        elif(n==3):
            ab=int(input("Enter required number of transaction : "))
            for i in range(0,ab):
                print(transaction[i])
        elif(n==4):
            k=input("Enter your current password : ")
            for i in users:
                if(k==i['pass']):
                    m=input("Enter new password : ")
                    i['pass']=m
                    print("password changed successfully!!!")
                    print(i['pass'])
                    break
            else:
                print("Password incorrect")
        elif(n==5):
            direct_deposit(name,a)
        elif(n==6):
            print("\tWelcome to account Transfer")
            account_transfer(name,a)
        else:
            break
# to add amount to atm    
def addamount():
    os.system('cls')
    print("enter amount to load")
    for i in amount:
        money=int(input("Enter no of "+str(i)+" notes "))
        amount[i]+=money
        a = amount[i]*i
        atmdetail['balance'] += a
        print("Amount loaded to atm successfully!!!")
# to show no of notes in atm
def showamount():
    os.system('cls')
    print("Here you have")
    for i in amount:
        print(i,"=",amount[i])
#no of notes to withdraw,condition checking,denomination checking,atm stock checking 
#direct deposit by user
def direct_deposit(name,a):
    ab=int(input("Enter amount to deposit to your account : "))
    if(ab%100==0):
        ref=0
        for i in amount:
            no=int(input("Enter no of"+str(i)+":"))
            ref+=i*no
            amount[i]+=no
        if(ref==ab):
            a['balance']+=ab
            print("Amount credied successfully")
        else:
            print("Amount deposited")
    else:
        print("Enter correct amount")
#account transfer
def account_transfer(name,a):
    print("1.Account transfer\n2.Exit")
    val=int(input("Enter choice : "))
    
    if(val==1):
        name1=input("Enter receipent name : ")
        amount=int(input("Enter amount: "))
        if(amount<a['balance']):
            for i in users:
                if(i['name']==name1):
                    i['balance']+=amount
                    a['balance']-=amount

        else:
            print("Amount should be less than your balance")
            a['balance']=a['balance']
#to check the current balance of atm       
def atmbalance(atmdetails):
    atmdetail['balance']=0
    for i in amount:
        a=i*amount[i]
        atmdetail['balance']+=a
    print("Atm balance is ",atmdetail['balance'])
print("\tATM")
attempt=4
# 1. admin-- add amount(),show amount(),atmbalance(),exit
# 2. customer -- attempt checking, customer()--Withdraw,show balance,transaction,exit
#3.exit
while(True): 
    print('''1.Admin\n2.Customer\n3.Exit''')
    n=int(input("Enter Your Choice : "))
    if(n==1):
        os.system('cls')
        print("Welcome Admin!!!")
        name=input("Enter Admin Name : ")
        passwd=input("Enter your Password : ")
        if(name=="Abarna" and passwd=="262903"):
            os.system('cls')
            print("Welcome",name)
            while(True):
               
                print("1.Add amount\n2.Show amount\n3.Exit\n4.Atmbalance")
                a=int(input("Enter choice :"))
                if(a==1):
                    addamount()
                    
                elif(a==2):
                    showamount()
                    
                elif(a==3):
                    break
                elif(a==4):
                    atmbalance(atmdetail)
                    
                else:
                    print("Invalid Input")
                    
        else:
        
            print("Username and password doesnot match")
            continue
    elif(n == 2):
        os.system('cls')
        print("Customer")
        print("1.Login\n2.Logout")
        a=int(input("Enter customer's choice : "))
        if(a==1):
            if(attempt<=0):
                break
            else:
                name=input("Enter customer name : ")
                password=input("Enter password : ")
                for i in users:
                    if(name==i['name'] and password==i['pass']):
                        a=i
                        customer(name,a,atmdetail)
                    else:
                        continue 
                else:
                    attempt-=1
                    print("Attempt left :",attempt)
        elif(a==2):
            break
    else:
        exit()