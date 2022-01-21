import os
admin=[{'name':'admin1','pass':'1'},
        {'name':'admin2','pass':'2'},
        {'name':'admin3','pass':'3'}]
passengers=[{'id':1,'name':'passenger1','pass':'1','wallet':10000},
            {'id':2,'name':'passenger2','pass':'2','wallet':90},
            {'id':3,'name':'passenger3','pass':'3','wallet':10000},
            {'id':4,'name':'passenger4','pass':'4','wallet':20500},
            {'id':5,'name':'passenger5','pass':'5','wallet':30000}]
train=[{'Train_name':'train1','Stops':3,'Seats':2,'seatarray':[[0 for i in range(3)] for j in range(2)],'stopname':[chr(65+i) for i in range(3)]}]
waiting_list=[]
booking_history=[]
print("\tWELCOME TO BOOK YOUR RAILWAY TICKET!!!")
#admin login       
def adm():
    while(True):
        print("\t-----LOGIN TO CONTINUE-----")
        print("1.Login\n2.Logout")
        b=int(input("Enter choice : "))
        if(b==1):
            name=input("Enter admin's name : ")
            password=input("Enter password : ")
            for i in admin:
                if(i['name']==name and i['pass']==password):
                    print("Welcome",name,"!")
                    admin_options(name)
        elif(b==2):
            break  
#admins options--->add train,remove train,view train,add stops
def admin_options(name):
    while(True):
        os.system('cls')
        print("1.Add train,Routes and station\n2.Remove train\n3.Declare Seat Availability\n4.Exit")
        y=int(input("Enter your choice : "))
        if(y==1):
            os.system('cls')
            addtrain()
        elif(y==2):
            os.system('cls')
            removetrain()
        elif(y==3):
            os.system('cls')
            seatavailability_admin()
        elif(y==4):
            break
#add train by admin
def addtrain():
    d={}
    while(True):
        print("\t-----ADD TRAIN HERE!!!-----")
        print("1.Add train\n2.Exit")
        x=int(input("Enter your choice : "))
        print("\n")
        if(x==1):
            train_name=input("Enter train name : ")
            stop=int(input("Enter no stops between boarding and destination : "))
            seat=int(input("Enter total no of seats : "))
            seat_array=[[0 for i in range(stop)] for j in range(seat)]
            stop_name=[]
            for i in range(stop):
                name=input("Enter stop name : ")
                stop_name.append(name)
            train.append({"Train_name":train_name,'Stops':stop,'Seats':seat,'seatarray':seat_array,'stopname':stop_name})
         
        elif(x==2):
            break
#remove train
def removetrain():
    while(True):
        print("\t-----REMOVE TRAIN-----")
        print("1.Remove train\n2.Exit")
        w=int(input("Enter your choice : "))
        print("\n")
        if(w==1):
            name=input("Enter train name : ")
            if(len(train)!=0):
                for i in train:
                    if(i['Train_name']==name):
                        train.remove(i)
                        print("Train Removed successfully")
                        break
            else:
                print("No train is available")
        elif(w==2):
            break
#view train-->by admin
def viewtrain_user():
    os.system('cls')
    print("\t-----VIEW TRAINS------")
    while(True):
        print("\n")
        print("1.View train and seat availability\n2.Exit")
        v=int(input("Enter your choice : "))
        print("\n")
        if(v==1):
            if(len(train)!=0):
                for i in train:
                    print("\n------------")
                    print("\nTRAIN NAME : ",i['Train_name'])
                    print("\n")
                    print("SEAT AVAILABILITY IN",i['Train_name'])
                    
                    for j in i['seatarray']:
                        print(j)

                    print("\n")
                    print("\nSTOPS IN",i['Train_name'])
                    k=0
                    for x in i['stopname']:
                        k+=1
                        print("Stops",k,":",x)
            else:
                print("No train is available")
        elif(v==2):
            break
#to view available train by admin
def seatavailability_admin():
    print("\t-----VIEW TRAINS------")
    while(True):
        print("\n")
        print("1.View train and seat availability\n2.Exit")
        v=int(input("Enter your choice : "))
        print("\n")
        if(v==1):
            if(len(train)!=0):
                for i in train:
                    print("\n------------")
                    print("\nTRAIN NAME : ",i['Train_name'])
                    print("\n")
                    print("SEAT AVAILABILITY IN",i['Train_name'])
                    
                    for j in i['seatarray']:
                        print(j)

                    print("\n")
                    print("\nSTOPS IN",i['Train_name'])
                    k=0
                    for x in i['stopname']:
                        k+=1
                        print("Stops",k,":",x)
            else:
                print("No train is available")
        elif(v==2):
            break
# user
def user():
    while(True):
        print("1.New user\n2.Existing User\n3.Exit")
        n=int(input("Enter your choice: "))
        if(n==1):
            os.system('cls')
            new_user()
        elif(n==2):
            os.system('cls')
            existing_user()
        elif(n==3):
            break
#new user-->create account
def new_user():
    while(True):
        d={}
        print("CREATE NEW ACCOUNT")
        print("1.Create account\n2.Exit")
        a=int(input("Enter choice : "))
        if(a==1):
            name=input("Enter user name : ")
            passwd=input("Enter password : ")
            id=int(input("Enter id : "))
            flag=1
            for i in passengers:
                if(name==i['name'] and i['id']==id):
                    flag=0
            if(flag==1):
                d['name']=name
                d['pass']=passwd
                d['wallet']=20000
                d['id']=id
                passengers.append(d)
                print("User created successfully")
                    
            else:
                print("User name already exist..\n Please try again with another name")
        elif(a==2):
            break
#existing user-->def options()-->booking ticket,cancel,change password,exit
def existing_user():
    while(True):
        print("LOGIN TO CONTINUE")
        print()
        print("1.Login\n2.Logout")
        print()
        b=int(input("Enter choice : "))
        print()
        if(b==1):
            name=input("Enter username : ")
            password=input("Enter password: ")
            for i in passengers:
                if(i['name']==name and i['pass']==password):
                    os.system('cls')
                    print("Welcome",name,"!")
                    while(True):
                        print("1.Book Ticket\n2.Cancel Ticket\n3.Change Password\n4.Booking History\n5.Wallet\n6.View train and availability\n7.Exit")
                        c=int(input("Enter your choice : "))
                        if(c==1):
                            os.system('cls')
                            print("\tBOOK YOUR TICKET HERE")
                            book_ticket(name)
                        elif(c==2):
                            os.system('cls')
                            cancel_booking(name)
                        elif(c==3):
                            os.system('cls')
                            change_password()
                        elif(c==4):
                            os.system('cls')
                            user_booking_history(name)
                        elif(c==5):
                            for i in passengers:
                                if(i['name']==name):
                                    print(i['wallet'])
                        elif(c==6):
                            viewtrain_user()
                        elif(c==7):
                            break
                            print()
                        else:
                            print("Invalid input")
        elif(b==2):
            break    
#to change password by user
def change_password():
    print("\tWELCOME TO CHANGE PASSWORD!!")
    while(True):
        print("1.Change password\n2.Exit")
        d=int(input("Enter choice : "))
        if(d==1):
            e=input("Enter your current password: ")
            for i in passengers:
                if(i['pass']==e):
                    f=input("Enter new password")
                    i['pass']=f
                    print("Password changed successfully")
        elif(d==2):
            break
#to view booking history
def user_booking_history(name):
    os.system('cls')
    while(True):
        print("\tVIEW BOOKING HISTORY!!!")
        print("1.view history\n2.Exit")
        val=int(input("Enter choice : "))
        if(val==1):
            view_history(name)
        elif(val==2):
            break
#to book a ticket by existing user--->specifying boarding point and destination
def book_ticket(name):
    d={}
    wait={}
    val1=input("Enter Train name : ")
    k=0
    for w in passengers:
        if(w['name']==name):
            f=w['id']
            #to display stops
    for y in train:
        if(y['Train_name']==val1):
            for z in y['stopname']:
                k+=1
                print("Stops",k,":",z)
            #to alot seat
                #for p in range(1):
            s=int(input("Enter boarding point : "))
            e=int(input("Enter Destination : "))
            for i in range(y['Seats']):
                if(sum(y['seatarray'][i][s:e])==0):
                    print("Seat alloted is",i)
                    flag=1
                    for j in range(s-1,e):
                        y['seatarray'][i][j]=f
                    break
            else:
                print("Seat not available")
                flag=0
                wait['id']=f
                wait['passenger name']=name
                wait['boarding point']=s
                wait['destination']=e
                waiting_list.append(wait)
                print("\nYour booking is not conformed\nIt is in waiting list")
                print("\n")
        if(flag==1):
            d['id']=f
            d['passenger name']=name
            d['boarding point']=s
            d['destination']=e
            booking_history.append(d)
    print()
#to cancel booking
def cancel_booking(name):
    print("\tCANCEL YOUR BOOKING")
    while(True):
        print("1.Cancel booking\n2.Exit")
        val1=int(input("Enter choice :"))
        if(val1==1):
            view_history(name)
            a=int(input("Enter boarding point : "))
            b=int(input("Enter destination : "))
            r=int(input("Enter id : "))
            for i in booking_history:
                k=i['boarding point']
                v=i['destination']
                ab=i['id']
                ans1=abs(k-v)*r
                if(a==k and b==v and r==ab):
                    for y in train:
                        for i in range(y['Seats']):
                            if(sum(y['seatarray'][i][k:v])==ans1):
                                for j in range(k-1,v):
                                    y['seatarray'][i][j]=0
                                break
            for o in booking_history:
                if(o['passenger name']==name and o['boarding point']==a and o['destination']==b):
                    booking_history.remove(o)
            print("Booking cancelled successfully")
            for x in waiting_list:
                q=x['id']
                an=x['boarding point']
                c=x['destination']
                if(an==a and c==b):
                    for y in train:
                        for i in range(y['Seats']):
                            if(sum(y['seatarray'][i][an:c])==0):
                                for j in range(an-1,c):
                                    y['seatarray'][i][j]=q
                                break
                            print("Booking confirm")
        elif(val1==2):
            break
#view history
def view_history(name):
    if(len(booking_history)!=0):
        for i in booking_history:
            if(i['passenger name']==name):
                print("PASSENGER NAME : {}\nID : {},\nBOARDING POINT: {},\nDESTINATION: {} ".format(i['passenger name'],i['id'],i['boarding point'],i['destination']))
                print("\n")    
    else:
        print("You have no booking history")
#main coding'
while(True):
    print("\n")
    print("1.Admin\n2.User\n3.Exit")
    z=int(input("Enter your choice: "))
    if(z==1):
        os.system('cls')
        adm()
    elif(z==2):
        os.system('cls')
        user()
    elif(z==3):
        exit()