import os
import datetime
admin=[{'name':'admin1','pass':'1'},{'name':'admin2','pass':'2'}]
users=[{'email':'user1@gmail.com','name':'user1','pass':'1','wallet':5000,'friend':'user2'},{'email':'user2@gmail.com','name':'user2','pass':'2','wallet':5000,'friend':'user1'}]

group=[{'username':'user1','contact1':'abc','contact1 wallet':2000,'contact2':'abcd','contact2 wallet':3000},
        {'username':'user2','contact1':'xyz','contact1 wallet':2000,'contact2':'wxyz','contact2 wallet':3000}]

expense=[{'username':'user1','expense name':'room rent','total expense amount':1000}]

friend=[]

equal_share_history=[]

unequal_share_history=[]

history=[]

def user():
    while(True):
        print("\t-----USER-----")
        print("1.Existing user\n2.New user\n3.Exit")
        a=int(input("Enter choice : "))
        if(a==1):
            os.system('cls')
            existinguser()
        elif(a==2):
            os.system('cls')
            newuser()
        elif(a==3):
            break

#user---->existing user
def existinguser():
    while(True):
        print("\t-----LOGIN TO CONTINUE-----\n")
        print("1.Login\n2.Logout")
        n=int(input("Enter choice : "))
        if(n==1):
            user_email=input("Enter user's email : ")
            user_pass=input("Enter user's pass : ")
            for i in users:
                a=i
                if(i['email']==user_email and i['pass']==user_pass):
                    print("Welcome",i['name'])
                    os.system('cls')
                    user_options(a)
        elif(n==2):
            break

#user---->new user---->create account
def newuser():
    d={}
    while(True):
        print("\t-----USER-----")
        print("1.Create account\n2.Exit")
        c=int(input("Enter choice : "))
        if(c==1):
            os.system('cls')
            print("\t-----Create account here-----")
            email=input(("Enter user email : "))
            name=input("Enter user name : ")
            passwd=input("Enter user's password : ")
            flag=1
            for i in users:
                if(name==i['name'] ):
                    flag=0
            if(flag==1):
                d['email']=email
                d['name']=name
                d['pass']=passwd
                users.append(d)
                print("\nUser created successfully")
            else:
                print("User name already exist..\n Please try again with another name")
        elif(c==2):
            break

#user option--->add expense,update wallet,add friends,remove friends,view and pay pending dues,transaction history
def user_options(a):
    while(True):
        print("\t-----WELCOME",a['name'],"-----")
        print("""1.EXPENSE\n2.GROUP\n3.WALLET\n4.ADD FRIENDS\n5.REMOVE FRIENDS\n6.SHARE EXPENSES\n7.VIEW AND PAY PENDING DUES\n8.TRANSACTION HISTORY\n9.EXIT""")
        k=int(input("Enter choice : "))
        if(k==1):#add expense
            os.system('cls')
            user_expense(a)
        elif(k==2):#create group
            user_create_group(a)
        elif(k==3):#wallet
            user_wallet(a)
        elif(k==4):#add friend
            user_add_friend(a)
        elif(k==5):#remove friend
            user_remove_friend(a)
        elif(k==6):#share expense
            user_share_expense(a)
        elif(k==7):#pending dues
            user_view_and_pay_pending_dues(a)
        elif(k==8):#transaction history
            user_transaction_history(a)
        elif(k==9):
            break

#existing user---->user option---->add expense
def user_expense(a):
    os.system('cls')
    e={}
    print("1.View expenses\n2.Add expenses")
    n=int(input("Enter choice : "))
    if(n==1):
        os.system('cls')
        print("\t-----VIEW EXPENSES-----\n")
        for i in expense:
            if(i['username']==a['name']):
                print("Username : {}\nExpense name : {}\nExpense amount : {}".format(i['username'],i['expense name'],i['total expense amount']))
                print()
    elif(n==2):
        print("\t-----ADD EXPENSES-----\n")
        print()
        expense_name=input("Enter expense name : ")
        total_expense=input("Enter total expense amount : ")
        e['username']=a['name']
        e['expense name']=expense_name
        e['total expense amount']=total_expense
        expense.append(e)
        print("\nExpense added successfully\n")

#existing user---->user option----->create group
def user_create_group(a):
    os.system('cls')
    g={}
    print("1.View group\n2.Create group")
    n=int(input("Enter choice : "))
    if(n==1):
        os.system('cls')
        print("\t-----VIEW GROUP-----\n")
        for i in group:
            if(i['username']==a['name']):
                print("User name : {}\nContact1 : {}\nContact1 wallet : {}\n\nContact2 : {}\nContact2 : {}".format(i['username'],i['contact1'],i['contact1 wallet'],i['contact2'],i['contact2 wallet']))
                print()
                break
        else:
            print("\nNo user found\n")
    elif(n==2):
        os.system('cls')
        print("\t-----CREATE GROUP-----\n")
        name=input("Enter user name : ")
        
        for i in group:
            if(i['username']==name):
                print("\nGroup already exist\n")
                break
        else:
            p=input("Enter 1st contact name : ")
            q=int(input("Enter 1st contact wallet amount : "))
            r=input("Enter 2nd contact name : ")
            s=int(input("Enter 2nd contact wallet amount : "))
            g['username']=a['name']
            g['contact1']=p
            g['contact1 wallet']=q
            g['contact2']=r
            g['contact2 wallet']=s
            group.append(g)
            print("\nGroup created successfully\n")

#existing user---->user option----->add friend
def user_add_friend(a):
    u={}
    os.system('cls')
    print("\t-----ADD FRIEND-----\n")
    name=input("Enter Friend name : ")
    amount=int(input("Enter Friends's wallet amount : "))
    for i in users:
        if(a['name']==i['name']):
            u['username']=a['name']
            u['friend']=name
            u['friend wallet']=amount
            friend.append(u)
            print("Friend added successfully")
            print(friend)

#existing user---->user option---->remove friend
def user_remove_friend(a):
    os.system('cls')
    print("\t-----REMOVE FRIENDS-----\n")
    if(len(friend)!=0):
        for i in friend:
            if(i['username']==a['name']):
                print("\nUsername : {}\nFriend name : {}\nFriend wallet amount : {}".format(i['username'],i['friend'],i['friend wallet']))
                print()
            name=input("Enter friend name to remove : ")
            if(i['username']==a['name']):
                if(i['friend']==name):
                    friend.remove(i)
                    print("\nFriend removed\n")
                    break
    else:
        print("No friend found")

#existing user---->user option---->share expense
def user_share_expense(a):
    os.system('cls')
    print("\t-----SHARE EXPENSE-----\n")
    print("1.Share with Group\n2.Share with Friend\n")
    k=int(input("Enter choice : "))
    if(k==1):
        user_group_expense(a)
    elif(k==2):
        user_share_with_friend(a)

#existing user---->user option---->share expense---->group expense
def user_group_expense(a):
    h={}
    os.system('cls')
    print("\t-----GROUP EXPENSE-----\n")
    name=input("Enter expense name : ")
    for i in expense:
        if(i['username']==a['name']):
            if(i['expense name']==name):
                print("Expense amount is ",i['total expense amount'])
                k=i['total expense amount']
                ans=k//3
                for r in group:
                    s=r['contact1']
                    r['contact1 wallet']-=ans
                    r['contact2 wallet']-=ans
                    print("Amount debited for contact")
                    break
                for j in users:
                    j['wallet']-=ans
                    print("Amount debited for you")
                    break

        break
    else:
        print("\nExpense not available")

#existing user---->user option---->share expense---->share with friend
def user_share_with_friend(a):
    os.system('cls')
    print("\t-----SHARE EXPENSE WITH FRIEND-----")
    print("1.View Friends\n2.Share Equally\n3.Share unequally")
    c=int(input("Enter choice : "))
    if(c==1):
        os.system('cls')
        view_friends(a)
    elif(c==2):
        os.system('cls')
        share_expense_equally(a)
    elif(c==3):
        os.system('cls')
        share_expense_unequally(a)

#existing user---->user option---->view friends
def view_friends(a):
    print("\t-----VIEW FRIENDS-----\n")
    for i in users:
        if(i['name']==a['name']):
            print("Username : {}\nFriend name :{}".format(i['name'],i['friend']))
            print()

#existing user---->user option---->share expense---->share equally
def share_expense_equally(a):
    f={}
    print("\t-----SHARE EXPENSE EQUALLY-----")
    name=input("Enter expense name : ")
    friend_name=input("Enter friend name : ")
    for i in expense:
        if(i['username']==a['name']):
            if(i['expense name']==name):
                k=i['total expense amount']
                ans=k//2
                for i in users:
                    if(i['name']==a['name'] and i['friend']==friend_name):
                        f['username']=a['name']
                        f['friend name']=friend_name
                        f['expense name']=name
                        f['total expense amount']=k
                        f['your share']=ans
                        f['user status']='pending'
                        f['friend status']='pending'
                        equal_share_history.append(f)

#existing user---->user option---->share expense ---->share unequally
def share_expense_unequally(a):
    f={}
    print("\t-----SHARE EXPENSE UNEQUALLY-----")
    name=input("Enter expense name : ")
    friend_name=input("Enter friend name : ")
    for i in expense:
        if(i['username']==a['name']):
            if(i['expense name']==name):
                k=i['total expense amount']
                ans=k//2
                print("\n1.PAY BY YOU\n2.PAY BY FRIEND\n")

                os.system('cls')
                print("\t-----PAY BY YOU-----\n")
                for i in users:
                    if(i['name']==a['name']):
                        i['wallet']-=k
                        print("\nAmount Debited\n")

                for i in users:
                    if(i['name']==a['name'] and i['friend']==friend_name):
                        f['username']=a['name']
                        f['friend name']=friend_name
                        f['expense name']=name
                        f['total expense amount']=k
                        f['your share']=ans
                        f['amount paid by user']=k
                        f['user status']='paid'
                        f['friend status']='pending'
                        unequal_share_history.append(f)

#view pending dues and history
def user_view_and_pay_pending_dues(a):
    h={}
    os.system('cls')
    print("\t-----VIEW PENDING DUES AND PAY-----\n")
    print("1.Share equally\n2.Unequally\n")
    w=int(input("Enter choice : "))
    print()
    if(w==1):
        for i in equal_share_history:
            b=i['your share']
            print("Creater name : {}\nFriend name :{}\nExpense name :{}\nTotal Expense Amount :{}\nYour share :{}\nUser Status :{}\nFriend status :{}".format(i['username'],i['friend name'],i['expense name'],i['total expense amount'],i['your share'],i['user status'],i['friend status']))
            print()
            for k in equal_share_history:
                if(k['user status']=='pending' or k['friend status']=='pending'):
                    print("1.Settle up\n2.Exit")
                    j=int(input("Enter choice : "))
                    if(j==1):
                        if(a['name']==i['username']):
                            a['wallet']-=b
                            i['user status']='paid'
                            print("Amount paid successfully")
                            
                            h['username']=i['username']
                            h['friend name']=i['friend name']
                            h['expense name']=i['expense name']
                            h['total expense amount']=i['total expense amount']
                            h['your share']=i['your share']
                            h['user status']=i['user status']
                            h['payment type']='Share equally'
                            h['date']=datetime.date.today()
                            history.append(h)
                            break
                        
                        elif(a['name']==i['friend name']):
                            a['wallet']-=b
                            i['friend status']='paid'
                            print("\nAmount paid successfully")
                            
                            h['username']=i['username']
                            h['friend name']=i['friend name']
                            h['expense name']=i['expense name']
                            h['total expense amount']=i['total expense amount']
                            h['your share']=i['your share']
                            h['user status']=i['friend status']
                            h['payment type']='Share equally'
                            h['date']=datetime.date.today()
                            history.append(h)
                            break
                    else:
                        break
            else:
                print("\nYou have no dues to pay")
                break
    elif(w==2):
        for i in unequal_share_history:
            b=i['your share']
            c=i['username']
            print("Creater name : {}\nFriend name :{}\nExpense name :{}\nTotal Expense Amount :{}\nAmount paid by creater :{}\nYour share :{}\nUser Status :{}\nFriend status :{}".format(i['username'],i['friend name'],i['expense name'],i['total expense amount'],i['amount paid by user'],i['your share'],i['user status'],i['friend status']))
            print()
           
            if(i['friend status']=='pending'):
                print("1.Settle up\n2.Exit")
                j=int(input("Enter choice : "))
                if(j==1):

                    if(a['name']==i['friend name']):
                        print(b)
                        a['wallet']-=b
                        for p in users:
                            if(p['name']==c):
                                p['wallet']+=b
                        i['friend status']='paid'
                        print("Amount paid successfully")
                        
                        h['username']=c
                        h['friend name']=i['friend name']
                        h['expense name']=i['expense name']
                        h['total expense amount']=i['total expense amount']
                        h['your share']=i['your share']
                        h['friend status']=i['friend status']
                        h['payment type']='Share unequally'
                        h['date']=datetime.date.today()
                        history.append(h)
                        break
        else:
            print("No dues found")

#wallet balance
def user_wallet(a):
    os.system('cls')
    while(True):
        print("1.Check wallet balance\n2.Update balance\n3.Exit")
        k=int(input("Enter choice : "))
        if(k==1):
            os.system('cls')
            print("\t-----CHECK YOUR WALLET BALANCE-----")
            for i in users:
                if(i['name']==a['name']):
                    print("Your balance is",i['wallet'])
                    print("\n")
                    break
        elif(k==2):
            os.system('cls')
            print("\t-----UPDATE YOUR WALLET BALANCE-----")
            balance_amount=int(input("Enter wallet amount : "))
            for i in users:
                if(i['name']==a['name']):
                    i['wallet']+=balance_amount
                    print("Wallet amount updated successfully")
                    print()
        elif(k==3):
            break

#existing user---->user option ---->view transaction history
def user_transaction_history(a):
    os.system('cls')
    print("\t----- VIEW TRANSACTION HISTORY-----\n")
    for i in history:
        if(i['username']==a['name'] or i['friend name']==a['name']):
            print("Creater name :{}\nFriend name :{}\nExpense name :{}\nTotal Expense amount :{}\nYour share:{}\nStatus :{}\nPayment Type :{}\nDate :{}".format(i['username'],i['friend name'],i['expense name'],i['total expense amount'],i['your share'],i['user status'],i['payment type'],i['date']))
            print()                                                                                                                                            

#driver code       
while(True):
    print("\t----------SPLITWISE----------")
    print("\n1.Admin\n2.User\n3.Exit")
    a=int(input("Enter choice : "))
    if(a==1):
        os.system('cls')
        print("\t-----ADDMIN LOGIN-----")
        name=input("Enter admin's name : ")
        password=input("Enter admin's password : ")
        for i in admin:
            if(i['name']==name and i['pass']==password):
                print("Welcome",name)
    elif(a==2):
        os.system('cls')
        user()
    elif(a==3):
        exit()